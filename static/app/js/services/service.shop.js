(function () {

    var injectParams = ['$http', '$q'];

    var productsFactory = function ($http, $q) {
        var serviceBase = '/wxshop/', factory = {};
        
        factory.getProducts = function (category_id) {

            
            return "{'data':'1'}";
        };
        
        factory.getMods = function (category_id) {

            
            return category_id;
        };

        return factory;
    };

    productsFactory.$inject = injectParams;

    angular.module('app').factory('shopService', productsFactory);

}());