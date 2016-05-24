(function () {


	 var injectParams = ['$scope', '$location', '$routeParams',
	                        '$timeout', 'config', 'dataService', 'modalService','toaster'];
	var couponController = function ($scope, $location, $routeParams,
                $timeout, config, dataService, modalService,toaster) {
		
		var vm = this,
		orderId = ($routeParams.orderId) ? parseInt($routeParams.orderId) : 0,
		timer,
		onRouteChangeOff;
		vm.coupons = [];

        function init() {
        	getCoupons();
        }

        function getCoupons() {
            dataService.getCoupons(orderId)
            .then(function (data) {
                vm.coupons = data;
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);
            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        init();
    };

    couponController.$inject = injectParams;
    angular.module('shopApp').controller('CouponController', couponController);

}());
