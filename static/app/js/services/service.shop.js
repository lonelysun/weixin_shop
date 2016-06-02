(function () {

    var injectParams = ['$http', '$q'];

    var shopFactory = function ($http, $q) {
        var serviceBase = window.document.location.pathname;
        var factory = {};

        /** mod carousel **/
        factory.getCarousel = function (position) {
            return $http.get(serviceBase + '_get_carousel', {
                params : {
                    position:position
     			}
            }).then(function(results) {
                return results.data;
            });
        };
        /** mod carousel **/
        factory.getNav = function (position) {
            return $http.get(serviceBase + '_get_nav', {
                params : {
                    position:position
     			}
            }).then(function(results) {
                return results.data;
            });
        };

        /** mod contact us **/
        factory.getContact = function (position) {
            return $http.get(serviceBase + '_get_contact', {
                params : {
     			}
            }).then(function(results) {
                return results.data;
            });
        };



        return factory;
    };

    shopFactory.$inject = injectParams;
    angular.module('app').factory('shopService', shopFactory);

}());