// Copyright © 2015, Numenta, Inc. Unless you have purchased from
// Numenta, Inc. a separate commercial license for this software code, the
// following terms and conditions apply:
//
// This program is free software: you can redistribute it and/or modify it under
// the terms of the GNU Affero Public License version 3 as published by the
// Free Software Foundation.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
// FOR A PARTICULAR PURPOSE. See the GNU Affero Public License for more details.
//
// You should have received a copy of the GNU Affero Public License along with
// this program. If not, see http://www.gnu.org/licenses.
//
// http://numenta.org/licenses/


/**
 * Fluxible Action keys
 * - File
 *  - DELETE_FILE: {@link DeleteFile}
 *  - LIST_FILES: {@link ListFiles}
 *  - UPLOADED_FILE: {@link FileUpload}
 *  - UPDATE_FILE: {@link FileUpdate}
 *
 * - File Errors
 *  - LIST_FILES_FAILURE
 *  - UPLOADED_FILE_FAILED
 *  - UPDATE_FILE_FAILED
 *
 * - Model
 *  - ADD_MODEL: {@link AddModel}
 *  - DELETE_MODEL: {@link DeleteModel}
 *  - START_MODEL: {@link StartModel}
 *  - STOP_MODEL: {@link StopModel}
 *  - SHOW_MODEL: {@link ShowModel}
 *  - HIDE_MODEL: {@link HideModel}
 *  - EXPORT_MODEL_RESULTS: {@link ExportModelResults}
 *
 * - Model Data
 *  - RECEIVE_MODEL_DATA: {@link ReceiveModelData}
 *
 * - Model Errors
 *  - START_MODEL_FAILED
 *  - STOP_MODEL_FAILED
 *  - DELETE_MODEL_FAILED
 *  - UNKNOWN_MODEL_FAILURE
 *
 * - File Detail
 *  - SHOW_FILE_DETAILS: {@link ShowFileDetails}
 *  - HIDE_FILE_DETAILS: {@link HideFileDetails}
 *
 * - Create Model Dialog
 *  - SHOW_CREATE_MODEL_DIALOG: {@link ShowCreateModelDialog}
 *  - HIDE_CREATE_MODEL_DIALOG: {@link HideCreateModelDialog}
 *  - UPDATE_PARAM_FINDER_RESULTS: {@link UpdateParamFinderResults}
 *
 * - Metric
 *  - LIST_METRICS: {@link ListMetrics}
 *  - LIST_METRICS_FAILURE
 *
 * - Metric Data
 *  - LOAD_METRIC_DATA: {@link LoadMetricData}
 *  - UNLOAD_METRIC_DATA: {@link UnloadMetricData}
 */
export const ACTIONS = Object.freeze({
  // File
  DELETE_FILE: 'DELETE_FILE',
  LIST_FILES: 'LIST_FILES',
  UPLOADED_FILE: 'UPLOADED_FILE',
  UPDATE_FILE: 'UPDATE_FILE',

  LIST_FILES_FAILURE: 'LIST_FILES_FAILURE',
  UPLOADED_FILE_FAILED: 'UPLOADED_FILE_FAILED',
  UPDATE_FILE_FAILED: 'UPDATE_FILE_FAILED',

  // Model
  ADD_MODEL: 'ADD_MODEL',
  DELETE_MODEL: 'DELETE_MODEL',
  START_MODEL: 'START_MODEL',
  STOP_MODEL: 'STOP_MODEL',
  SHOW_MODEL: 'SHOW_MODEL',
  HIDE_MODEL: 'HIDE_MODEL',
  EXPORT_MODEL_RESULTS: 'EXPORT_MODEL_RESULTS',

  // Model Data
  RECEIVE_MODEL_DATA: 'RECEIVE_MODEL_DATA',

  // Model Errors
  START_MODEL_FAILED: 'START_MODEL_FAILED',
  STOP_MODEL_FAILED: 'STOP_MODEL_FAILED',
  DELETE_MODEL_FAILED: 'DELETE_MODEL_FAILED',
  UNKNOWN_MODEL_FAILURE: 'UNKNOWN_MODEL_FAILURE',

  // File Detail
  SHOW_FILE_DETAILS: 'SHOW_FILE_DETAILS',
  HIDE_FILE_DETAILS: 'HIDE_FILE_DETAILS',

  // Create Model Dialog
  SHOW_CREATE_MODEL_DIALOG: 'SHOW_CREATE_MODEL_DIALOG',
  HIDE_CREATE_MODEL_DIALOG: 'HIDE_CREATE_MODEL_DIALOG',
  UPDATE_PARAM_FINDER_RESULTS: 'UPDATE_PARAM_FINDER_RESULTS',

  // Metric
  LIST_METRICS: 'LIST_METRICS',
  LIST_METRICS_FAILURE: 'LIST_METRICS_FAILURE',

  // Metric Data
  LOAD_METRIC_DATA: 'LOAD_METRIC_DATA',
  UNLOAD_METRIC_DATA: 'UNLOAD_METRIC_DATA'
});

/**
 * Database Errors. Use to check database error names returned by callbacks.
 * 	- NOT_FOUND: Record not found
 *
 * @type {string}
 */
export const DATABASE_ERRORS = {
  NOT_FOUND: 'NotFoundError'
};

/**
 * Supported timestamp formats
 * @type {Array}
 */
export const TIMESTAMP_FORMATS = [
  // ISO 8601
  'YYYY-MM-DDTHH:mm:ss.SSSZ',
  'YYYY-MM-DDTHH:mm:ss.SSS',
  'YYYY-MM-DDTHH:mm:ss.SSZ',
  'YYYY-MM-DDTHH:mm:ss.SS',
  'YYYY-MM-DDTHH:mm:ss.SZ',
  'YYYY-MM-DDTHH:mm:ss.S',
  'YYYY-MM-DDTHH:mm:ssZ',
  'YYYY-MM-DDTHH:mm:ss',
  'YYYY-MM-DDTHH:mmZ',
  'YYYY-MM-DDTHH:mm',

  // ISO 8601 no 'T'
  'YYYY-MM-DD HH:mm:ss.SSSZ',
  'YYYY-MM-DD HH:mm:ss.SSS',
  'YYYY-MM-DD HH:mm:ss.SSZ',
  'YYYY-MM-DD HH:mm:ss.SS',
  'YYYY-MM-DD HH:mm:ss.SZ',
  'YYYY-MM-DD HH:mm:ss.S',
  'YYYY-MM-DD HH:mm:ssZ',
  'YYYY-MM-DD HH:mm:ss',
  'YYYY-MM-DD HH:mmZ',
  'YYYY-MM-DD HH:mm',
  'YYYY-MM-DD',

  // US Date, 12h AM/PM time
  'MM-DD-YYYY hh:mm:ss.SSS A',
  'MM-DD-YYYY HH:mm:ss.SS A',
  'MM-DD-YYYY HH:mm:ss.S A',
  'MM-DD-YYYY hh:mm:ss A',
  'MM-DD-YYYY hh:mm A',

  // US Date, 24h time
  'MM-DD-YYYY HH:mm:ss.SSS',
  'MM-DD-YYYY HH:mm:ss.SS',
  'MM-DD-YYYY HH:mm:ss.S',
  'MM-DD-YYYY HH:mm:ss',
  'MM-DD-YYYY HH:mm',

  // US Date
  'MM-DD-YYYY',
  'MM-DD-YY',

  // EU Date and time
  'DD-MM-YYYY HH:mm:ss.SSS',
  'DD-MM-YYYY HH:mm:ss.SS',
  'DD-MM-YYYY HH:mm:ss.S',
  'DD-MM-YYYY HH:mm:ss',
  'DD-MM-YYYY HH:mm',

  // EU Date
  'DD-MM-YYYY',
  'DD-MM-YY',

  // US 12h AM/PM time
  'hh:mm:ss.SSS A',
  'hh:mm:ss.SS A',
  'hh:mm:ss.S A',
  'hh:mm:ss A',
  'hh:mm A',

  // EU 24h
  'HH:mm:ss.SSS',
  'HH:mm:ss.SS',
  'HH:mm:ss.S',
  'HH:mm:ss',
  'HH:mm'
];
