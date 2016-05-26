'use strict';

angular.module('app')
  .constant('JQ_CONFIG', {})
  .constant('MODULE_CONFIG', [])
  .config(['$ocLazyLoadProvider', 'MODULE_CONFIG', function($ocLazyLoadProvider, MODULE_CONFIG) {
      $ocLazyLoadProvider.config({
          debug:  false,
          events: true,
          modules: MODULE_CONFIG
      });
  }])
;
