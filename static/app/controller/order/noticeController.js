(function () {

    var injectParams = ['$scope', '$location', '$routeParams',
                        '$timeout', 'config', 'dataService', 'modalService'];

    var noticeController = function ($scope, $location, $routeParams,
                                           $timeout, config, dataService, modalService) {
        var vm = this,
            orderId = ($routeParams.orderId) ? parseInt($routeParams.orderId) : 0,
            timer,
            onRouteChangeOff;
        vm.order = {};
        vm.errorMessage = '';

        function init() {
        }
        init();
    };

    noticeController.$inject = injectParams;
    angular.module('shopApp').controller('NoticeController', noticeController);

}());