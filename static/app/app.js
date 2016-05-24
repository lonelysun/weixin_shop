(function () {

    var app = angular.module('shopApp', ['ngRoute', 'ngTouch','ngSanitize','ui.bootstrap']);

    //购物车
    app.factory('memoryCart', function() {
    	  return {
    	    qty: 0
    	  }
	});

    app.config(['$routeProvider', function ($routeProvider) {
        var viewBase = '/born_weixin_shop/static/app/tpl/';
        $routeProvider
	        .when('/home', {
	            controller: 'HomeController',
	            templateUrl: viewBase + 'tpl.home.html',
	            controllerAs: 'vm'
	        })

            .otherwise({ redirectTo: '/home' });
    }]);
}());

