# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2015, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""
  Many git utilities needed by the pipelines
"""
import subprocess

from infrastructure.utilities import diagnostics
from infrastructure.utilities.cli import executeCommand
from infrastructure.utilities.exceptions import (CommandFailedError,
                                                 DetachedHeadError)
from infrastructure.utilities.path import changeToWorkingDir



def checkIfOptionSet(option, **kwargs):
  """
  Convenience function to check if a keyword arg exists and is set to True
  by the caller.

  :param option: The option that is being looked up.

  :param kwargs: Dict containing all the arguments passed to the function.

  :return: True if option is present in kwargs and is set to True.

  :rtype: boolean
  """
  return option in kwargs and kwargs[option]



def getCommitCount(path, logger):
  """
  Get the commit count from a git directory tree

  :param: path to git directory

  :param logger: logger for additional debug info if desired

  :raises: infrastructure.utilities.exceptions.CommandFailedError:
  if path isn't in a git checkout

  :returns: total commit count for the git directory

  :rtype: string
  """
  with changeToWorkingDir(path):
    return executeCommand("git rev-list HEAD --count", logger=logger)



def getGitRootFolder(logger):
  """
  Return the root folder of the current git repo

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError if
    the command fails

  :returns: The full path of the root folder of the current git repo

  :rtype: string
  """
  return executeCommand("git rev-parse --show-toplevel", logger=logger)



def getModifiedFilesBetweenRevisions(startSha, endSha, logger):
  """
  Get a list of all files modified between revisions

  :param startSha: SHA to start searching from

  :param endSha: SHA to search until

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError if
    the command fails; typically because you are not executing from within a
    git repository

  :returns: A `set` of modified files or None if the command fails

  :rtype: set
  """
  return set(executeCommand(
             "git diff --name-only %s...%s" % (startSha, endSha),
             logger=logger).split("\n"))



def getCurrentSha(logger):
  """
  Get the current SHA of a given repo

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError if
    the command fails; typically because you are not executing from within a
    git repository

  :returns: The current SHA

  :rtype: string
  """
  return executeCommand("git log -n1 --pretty=%H", logger=logger)



def getActiveBranch(logger):
  """
  Get the active branch name for the repository

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
      the command fails
    infrastructure.utilities.exceptions.DetachedHeadError: if the git checkout
      is in a detached head state

  :returns: The active branch name or the current SHA if in a detached head
    state

  :rtype: string
  """
  branch = executeCommand("git rev-parse --abbrev-ref HEAD", logger=logger)
  if branch == "HEAD":
    raise DetachedHeadError("There is no active branch; the head is detached.")

  return branch



def clone(gitURL, logger, **kwargs):
  """
  Clones the given git repository

  :param gitURL: The repository URL.

  :param logger: logger for additional debug info if desired

  :param kwargs: Various options to git clone gitURL can be passed as keyword
    arguments. For now only directory option is handled.
  e.g.
  clone(gitURL, directory=nameOfDirectory)

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :returns: The blob output of git clone

  :rtype: string
  """
  command = "git clone %s" % gitURL
  if checkIfOptionSet("directory", **kwargs):
    command += " " + kwargs["directory"]
  return executeCommand(command, logger=logger)



def checkout(pathspec, logger, **kwargs):
  """
  Switches to a given commit-ish

  :param pathspec: The name of the branch (commit-ish)

  :param logger: logger for additional debug info if desired

  :param kwargs:

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :returns: The text blob output of git checkout

  :rtype: string
  """
  command = "git checkout"
  if checkIfOptionSet("new", **kwargs):
    command += " -b "
  elif checkIfOptionSet("orphan", **kwargs):
    command += " --orphan"
  elif checkIfOptionSet("theirs", **kwargs):
    command += " --theirs"

  command += " %s" % pathspec
  return executeCommand(command, logger=logger)



def checkoutNewBranch(pathspec, logger):
  """
  Convenience function to create and switch to a new branch.

  :param pathspec: Name of the branch to be checked out.

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :returns: The text blob output of git checkout

  :rtype: string
  """
  return checkout(pathspec, new=True, logger=logger)



def checkoutOrphan(pathspec, logger):
  """
  Convenience function to create a orphan branch and switch to it.

  :param pathspec: Branch name.

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :returns: The text blob output of git checkout

  :rtype: string
  """
  return checkout(pathspec, orphan=True, logger=logger)



def reset(sha="", logger, **kwargs):
  """
  Resets the repository to a optional SHA. Optional argument for --hard

  :param kwargs:

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :returns: The exit code

  :rtype: int
  """
  command = "git reset "
  if checkIfOptionSet("hard", **kwargs):
    command += "--hard"
  command += " %s" % sha
  return executeCommand(command, logger=logger)



def resetHard(sha="", logger):
  """
  A convenience function that runs 'git reset --hard' for the given SHA.
  Calls reset(SHA, **kwargs).

  :params SHA: The SHA or commit-sh to which the code needs to be reset to.

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :returns: The exit code

  :rtype: int
  """
  return reset(sha, hard=True, logger=logger)



def revParse(commitish, logger, **kwargs):
  """
  Helper method to execute git rev-parse commands. Used to print the SHA1
  given a revision specifier (e.g HEAD). This function can return the output
  of the command executed or the exit code of the command executed if
  "exitcode" = True is passed as a keyword argument.

  :param commitish: The commit-ish.

  :param logger: logger for additional debug info if desired

  :param kwargs: Various options to git rev-parse can be passed as keyword
  arguments. The following options are currently supported:

  verify: Verify that exactly one parameter is provided, and that it
  can be turned into a raw 20-byte SHA-1 that can be used to access the object
  database.

  quiet: Only valid with verify. Do not output an error message if the
  first argument is not a valid object name; instead exit with non-zero status
  silently.

  abbrevRef: A non-ambiguous short name of the objects name

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :returns: A `string` representing a SHA or the exit code of the command.

  :rtype: string or int
  """
  command = "git rev-parse"
  if checkIfOptionSet("verify", **kwargs):
    command += " --verify"
  elif checkIfOptionSet("quiet", **kwargs):
    command += " --quiet"
  elif checkIfOptionSet("abbrevRef", **kwargs):
    command += " --abbrev-ref"

  command += " %s" % commitish
  return executeCommand(command, logger=logger)



def fetch(repository, refspec, logger):
  """
  Download objects and refs from another repository

  :param repository: Name of git repository (e.g origin)

  :param refspec: Name of the refspec (e.g. master)

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails
  """
  command = "git fetch %s %s" % (repository, refspec)
  return executeCommand(command, logger=logger)



def showRef(refList, logger, **kwargs):
  """
  List references in a local repository


  :param refList: Reference available in the local repository.

  :param logger: logger for additional debug info if desired

  :param kwargs: Optional switches to git show-ref. Following switches are
  supported at the moment.

    --verify: Enable stricter reference checking by requiring an exact
              ref path.
    --quiet: Aside from returning an error code of 1, it will also print an
             error message, if --quiet was not specified.

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError if
    the command fails
  """
  command = "git show-ref"
  if checkIfOptionSet("verify", **kwargs):
    command += " --verify"
  command += " %s" % refList
  return executeCommand(command, logger=logger)



def add(pathspec, logger):
  """
  Add file contents to the index

  :param pathspec: The file that is to be added to git.

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails
  """
  command = "git add %s" % pathspec
  return executeCommand(command, logger=logger)



def commit(message, logger, **kwargs):
  """
  Record changes to the repository
  Current implementation is supporting options like --amend
  This could be extended for other options as when required

  :param message: Commit message.

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails
  """
  command = "git commit "
  if checkIfOptionSet("amend", **kwargs):
    command += " --amend"
  command += " %s" % message
  return executeCommand(command, logger=logger)



def merge(path, message, logger, **kwargs):
  """
  Join two or more development histories together
  Current implementation supports --no-ff
  This could be extended for other options as when required.

  :param path:

  :param message: Merge commit message.

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails
  """
  command = "git merge "
  if checkIfOptionSet("noFF", **kwargs):
    command += " --no-ff"
  command += " -m %s %s" % (message, path)
  return executeCommand(command, logger=logger)



def removeFileFromGit(path, logger):
  """
  Remove files from the working tree and from the index.

  :param path: The file or path that has to be removed.

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :returns output of git rm

  :rtype: str
  """
  command = "git rm -rf %s" % path
  return executeCommand(command, logger=logger)



def getShaFromRemoteBranch(gitRemoteRepo, gitRemoteBranch, logger):
  """
  Get the actual SHA of the current HEAD of a remote repo / branch.

  :param gitRemoteRepo: The URL of the remote repo,
    e.g., git@github.com:numenta/nupic.git
  :param gitRemoteBranch: The name of the remote branch, e.g., master

  :param logger: logger for additional debug info if desired

  :raises:
    infrastructure.utilities.exceptions.CommandFailedError: if
    the command fails

  :return: A `String` representing the SHA

  :rtype: String
  """
  shaList = executeCommand("git ls-remote %s" % gitRemoteRepo, logger=logger)
  if gitRemoteBranch == "master":
    return shaList.split("\t")[0]
  else:
    formattedBranchName = "refs/heads/%s" % gitRemoteBranch
    for refShaPair in shaList.split("\n"):
      pair = refShaPair.split()
      if pair[1] == formattedBranchName:
        return pair[0]

  raise CommandFailedError("Could not find the specified branch %s on %s" %
                           gitRemoteBranch, gitRemoteRepo)
