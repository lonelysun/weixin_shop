(function () {

    var injectParams = ['$location', '$filter', '$window',
                        '$timeout', 'authService', 'dataService', 'modalService','toaster'];

    var CartController = function ($location, $filter, $window,
        $timeout, authService, dataService, modalService,toaster) {

        var vm = this;
        vm.carts = [];
        
        function init() {
        	getCarts();
        }
        
        vm.sum = function(items){
        	var total =0;
        	angular.forEach(items,function(data){
        	total += Number(data.qty)*Number(data.lst_price);
        	})
        	return total;
        };
        
        vm.countQty = function(items){
        	var total =0;
        	angular.forEach(items,function(data){
        		total += Number(data.qty);
        	})
        	return total;
        };
        
        function getCarts() {
            dataService.getCarts(vm.currentPage - 1, vm.pageSize)
            .then(function (data) {
                vm.totalRecords = data.totalRecords;
                vm.carts = data.results;
               
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);

            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        
        vm.addCartItem = function ($index,cart) {
	    	dataService.changeQty(cart).then(processError);
	    	vm.carts[$index].qty=vm.carts[$index].qty+1;
        };
        
        vm.subtractionCartItem = function ($index,cart) {
        	if(vm.carts[$index].qty-1>0){
		    	dataService.changeQty(cart).then(processError);
		    	vm.carts[$index].qty=vm.carts[$index].qty-1;
        	}else{
                var modalOptions = {
                    closeButtonText: '取消',
                    actionButtonText: '删除该商品',
                    headerText: '删除' + cart.product_name + '?',
                    bodyText: '您确人要从购物车中删除该商品吗?'
                };
                modalService.showModal({}, modalOptions).then(function (result) {
                    if (result === 'ok') {
                    	val={'id':cart.id}
                    	dataService.deleteCartItem(val).then(function () {}, processSuccess($index),processError);
                    }
                });
        	}
        };
        
        vm.checkout = function (cart) {
            dataService.checkout()
            .then(function (data) {
                $location.path('/orders/'+data+'/draft');
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);
            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        
        function processSuccess($index) {
        	vm.carts.splice($index, 1);
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
        
        init();
    };

    CartController.$inject = injectParams;
    angular.module('shopApp').controller('CartController', CartController);

}());
