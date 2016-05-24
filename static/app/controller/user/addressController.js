(function () {

    var injectParams = ['$location', '$filter', '$window',
                        '$timeout', 'authService', 'dataService', 'modalService','toaster'];

    var addressController = function ($location, $filter, $window,
        $timeout, authService, dataService, modalService,toaster) {

        var vm = this;
        vm.address = [];
        
        function init() {
        	getAddress();
        }
            
        function getAddress() {
            dataService.getAddress()
            .then(function (data) {
                vm.address = data;
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);

            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        init();
    };

    addressController.$inject = injectParams;
    angular.module('shopApp').controller('AddressController', addressController);

}());
