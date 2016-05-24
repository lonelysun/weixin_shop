(function () {

    var injectParams = ['$location', '$filter', '$window',
                        '$timeout', 'authService', 'dataService', 'modalService','toaster'];

    var accountController = function ($location, $filter, $window,
        $timeout, authService, dataService, modalService,toaster) {

        var vm = this;
        vm.account = {};
        
        function init() {
        	getAccount();
        }
            
        function getAccount() {
            dataService.getAccount()
            .then(function (data) {
                vm.account = data;
                $timeout(function () {
                    vm.cardAnimationClass = ''; //Turn off animation since it won't keep up with filtering
                }, 1000);

            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        
        vm.saveAccount = function () {
            dataService.saveAccount(vm.account)
            .then(function (data) {
                vm.account = data;
                toaster.pop('success', "保存成功", "个人资料保存成功！");
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);

            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        };
        
        init();
    };

    accountController.$inject = injectParams;
    angular.module('shopApp').controller('AccountController', accountController);

}());
