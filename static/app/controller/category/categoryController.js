(function () {

    var injectParams = ['$location', '$filter', '$window',
                        '$timeout', 'authService', 'dataService', 'modalService','toaster'];

    var categoryController = function ($location, $filter, $window,
        $timeout, authService, dataService, modalService,toaster) {

        var vm = this;
        vm.categorys = [];
        vm.slides = [];
        vm.myInterval=5000;
        
        function init() {
        	getCarousel();
        	getCategory();
        }
        
        function getCarousel() {
            dataService.getCarousel('category_top')
            .then(function (data) {
            	vm.slides =data.items;
            	vm.myInterval=data.interval;
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);
            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        
        function getCategory() {
            dataService.getCategory()
            .then(function (data) {
                vm.categorys = data.results;
               
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);

            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        
        init();
    };

    categoryController.$inject = injectParams;
    angular.module('shopApp').controller('CategoryController', categoryController);

}());
