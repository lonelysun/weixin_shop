(function () {

    var injectParams = ['$location', '$filter', '$window',
                        '$timeout', 'authService', 'dataService', 'modalService','toaster'];

    var userController = function ($location, $filter, $window,
        $timeout, authService, dataService, modalService,toaster) {

        var vm = this;
        vm.user = {};
        
      
        function init() {
        	getProfile();
        }
            
        function getProfile() {
            dataService.getProfile()
            .then(function (data) {
                vm.user = data;
                $timeout(function () {
                    vm.cardAnimationClass = ''; //Turn off animation since it won't keep up with filtering
                }, 1000);

            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        init();
    };

    userController.$inject = injectParams;
    angular.module('shopApp').controller('UserController', userController);

}());
