(function () {

    var injectParams = ['$location', '$filter', '$window',
                        '$timeout', 'authService', 'dataService', 'modalService','toaster'];

    var lineController = function ($location, $filter, $window,
        $timeout, authService, dataService, modalService,toaster) {

        var vm = this;
        vm.products = [];
        
        function init() {
        	getUserProducts();
        }
            
        function getUserProducts() {
            dataService.getUserProducts()
            .then(function (data) {
                vm.products = data.results;
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);

            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }

        init();
    };

    lineController.$inject = injectParams;
    angular.module('shopApp').controller('LineController', lineController);

}());
