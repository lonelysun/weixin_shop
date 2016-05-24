(function () {

	var injectParams = ['$scope', '$location', '$routeParams',
	                        '$timeout', 'config', 'dataService', 'modalService','toaster'];

	var prolistController = function ($scope, $location, $routeParams,
	                                           $timeout, config, dataService, modalService,toaster) {
        var vm = this,
        categoryId = ($routeParams.categoryId) ? parseInt($routeParams.categoryId) : 0,
            timer,
            onRouteChangeOff;

        vm.products = [];
        
        function init() {
        	getProducts();
        }
        
        function getProducts() {
            dataService.getProducts(categoryId)
            .then(function (data) {
                vm.products = data;
                $timeout(function () {
                    vm.cardAnimationClass = ''; //Turn off animation since it won't keep up with filtering
                }, 1000);
            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        init();
    };

    prolistController.$inject = injectParams;
    angular.module('shopApp').controller('ProlistController', prolistController);

}());
