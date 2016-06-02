'use strict';

angular.module('app')
  .constant('JQ_CONFIG', {})
  .constant('MODULE_CONFIG', [
      {
          name: 'ui.grid',
          files: [
              '../libs/angular/angular-ui-grid/ui-grid.min.js',
              '../libs/angular/angular-ui-grid/ui-grid.min.css',
              '../libs/angular/angular-ui-grid/ui-grid.bootstrap.css'
          ]
      },
  ])
  .config(['$ocLazyLoadProvider', 'MODULE_CONFIG', function($ocLazyLoadProvider, MODULE_CONFIG) {
      $ocLazyLoadProvider.config({
          debug:  false,
          events: true,
          modules: MODULE_CONFIG
      });
  }])
;
