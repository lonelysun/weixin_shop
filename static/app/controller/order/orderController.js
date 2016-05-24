(function () {

    var injectParams = ['$scope', '$location', '$routeParams',
                        '$timeout', 'config', 'dataService', 'modalService','toaster'];

    var orderController = function ($scope, $location, $routeParams,
                                           $timeout, config, dataService, modalService,toaster) {
    	var vm = this,
    	order_id = ($routeParams.order_id) ? parseInt($routeParams.order_id) : 0,
    	state = $routeParams.state,		 
    	timer,
    	onRouteChangeOff;
         
        vm.orders = [];
        
        function getOrders() {
            dataService.getOrders(order_id,state)
            .then(function (data) {
            	vm.orders =data;
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);
            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        
        vm.updateOrder = function ($index,state) {
        	
        	var order =vm.orders[$index]
        	
        	var str='';
        	if(state=='cancel'){
        		str="取消";
        	}else if(state=='unlink'){
        		str="删除";
        	}else if(state=='draft'){
        		str="确认";
        	}
        	var modalOptions = {
                closeButtonText: '取消',
                actionButtonText: '确认',
                headerText: '系统提示',
                bodyText: "您确认要"+str+"该订单吗?"
            };
        	
            modalService.showModal({}, modalOptions).then(function (result) {
                if (result === 'ok') {
                	dataService.updateOrder(order.id,state)
                    .then(function (data) {
                    	if(state=='cancel'){
                    		toaster.pop('success', "取消订单成功", "您已成功取消订单！");
                    	}else if(state=='unlink'){
                    		toaster.pop('success', "删除订单成功", "您已成功删除了订单！");
                    	}else if(state=='unlink'){
                    		toaster.pop('draft', "重新确认订单成功", "您已成功激活了订单！");
                    	}
                    	getOrders();
                    }, function (error) {
                    	toaster.pop('warning', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
                    });
                }
            });
        };
        
        function processSuccess() {
            $scope.editForm.$dirty = false;
            vm.updateStatus = true;
            startTimer();
        }

        function processError(error) {
            vm.errorMessage = error.message;
            startTimer();
        }

        function startTimer() {
            timer = $timeout(function () {
                $timeout.cancel(timer);
                vm.errorMessage = '';
                vm.updateStatus = false;
            }, 3000);
        }
        
        function init() {
        	getOrders();
        }
        
        init();
        
    };

    orderController.$inject = injectParams;
    angular.module('shopApp').controller('OrderController', orderController);

}());