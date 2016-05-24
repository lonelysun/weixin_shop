(function () {

    var injectParams = ['$scope', '$location', '$routeParams',
                        '$timeout', 'config', 'dataService', 'modalService','toaster'];

    var detailController = function ($scope, $location, $routeParams,
                                           $timeout, config, dataService, modalService,toaster) {
        var vm = this,
            productId = ($routeParams.productId) ? parseInt($routeParams.productId) : 0,
            timer,
            onRouteChangeOff;
        vm.product = {};
        
        vm.addCart = function () {
        	dataService.addCart(vm.product)
            .then(function (data) {
            	toaster.pop('success', "添加购物车成功", "恭喜您添加购物车成功，点击购物车去结账吧！");
            }, function (error) {
            	toaster.pop('warning', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        };
        
        vm.addFollow = function () {
        	dataService.addFollow(vm.product)
            .then(function (data) {
            	toaster.pop('success', "关注", "恭喜您添加关注成功！");
            }, function (error) {
            	toaster.pop('warning', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        };
        
        function getProduct() {
            dataService.getProduct(productId)
            .then(function (data) {
            	vm.product = data;
                $timeout(function () {
                }, 1000);
            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        
        function init() {
        	getProduct();
        }

        init();
    };

    detailController.$inject = injectParams;
    angular.module('shopApp').controller('DetailController', detailController);

}());