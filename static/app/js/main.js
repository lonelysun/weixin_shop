'use strict';

/* Controllers */

angular.module('app')
  .controller('AppCtrl', ['$scope',   '$localStorage', '$window',
    function(              $scope,     $localStorage,   $window ) {

      // config
      $scope.app = {
        name: 'Ds',
        path:'/born_weixin_shop/static/app/tpl/mod/mod_contact.html',

        version: '1.0.0',
        // for chart colors
        color: {
          primary: '#7266ba',
          info:    '#23b7e5',
          success: '#27c24c',
          warning: '#fad733',
          danger:  '#f05050',
          light:   '#e8eff0',
          dark:    '#3a3f51',
          black:   '#1c2b36'
        },
        settings: {
          themeID: 1,
          navbarHeaderColor: 'bg-black',
          navbarCollapseColor: 'bg-white-only',
          asideColor: 'bg-black',
          headerFixed: true,
          asideFixed: false,
          asideFolded: false,
          asideDock: false,
          container: false
        }
      }

  }]);
