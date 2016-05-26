'use strict';

app.directive('hello', ['$rootScope','shopService',   function($rootScope,shopService) {

    var mod_url='';

    return {
        restrict: 'E',

        link: function(scope, element, attrs) {
            //alert("link");
        },

        templateUrl: function(elem,attrs) {

            //alert("templateUrl");
            $rootScope.mods=['js'];

            if(attrs.type=='contact'){
                attrs.url='/born_weixin_shop/static/app/tpl/mod/mod_contact.html';
            }else{
                attrs.url='/born_weixin_shop/static/app/tpl/mod/mod_category.html';
            }
           return attrs.url;
       },


    };
}]);