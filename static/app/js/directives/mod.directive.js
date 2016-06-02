'use strict';

app.directive('modInclude', ['$rootScope','shopService',   function($rootScope,shopService) {
    return {
        restrict: 'E',
        replace: true,
        compile: function(scope, element, attrs) {
            //alert(scope.app);
        },
        templateUrl: function(elem,attrs) {
            //$rootScope.mods=['js'];
           return attrs.url;
       },
    };
}]);