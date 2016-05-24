(function () {

    var injectParams = ['$location', '$filter', '$window', '$timeout', 'dataService'];

    var homeController = function ($location, $filter, $window,
        $timeout, dataService ) {

        var vm = this;
        vm.products = [];
        vm.categorys = [];
        vm.slides = [];
        vm.myInterval=5000;
        
        function init() {
        	getCarousel();
        	getCategorys();
        }
        
        function getCarousel() {
            dataService.getCarousel('mobile_top')
            .then(function (data) {

            	vm.slides =data.items;
            	vm.myInterval=data.interval;
                $timeout(function () {
                    vm.cardAnimationClass = '';
                }, 1000);
            }, function (error) {
            	//toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        
        function getCategorys() {
            dataService.getCategorys()
            .then(function (data) {
                vm.categorys = data.results;
                $timeout(function () {
                    vm.cardAnimationClass = ''; //Turn off animation since it won't keep up with filtering
                }, 1000);
            }, function (error) {
            	//toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        init();
    };

    homeController.$inject = injectParams;
    angular.module('shopApp').controller('HomeController', homeController);

}());
