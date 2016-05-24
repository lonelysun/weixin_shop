(function () {

    var injectParams = ['$scope', '$location', '$routeParams',
                        '$timeout', 'config', 'dataService', 'modalService','toaster'];

    var paymentController = function ($scope, $location, $routeParams,
                                           $timeout, config, dataService, modalService,toaster) {
        var vm = this,
            orderId = ($routeParams.orderId) ? parseInt($routeParams.orderId) : 0,
            timer,
            onRouteChangeOff;
            
        vm.url='';
        vm.order = {};
        vm.errorMessage = '';
        vm.paymentResult = '';
        vm.paymentData = {};
        
        function getOrder() {
        	var url =location.href.split('#')[0];
        	vm.url=url;
            dataService.getOrder(orderId,url)
            .then(function (data) {
            	vm.order = data;
            	
                wx.config({
          	      debug: false,
          	      appId: vm.order.appId,
          	      timestamp: vm.order.timeStamp,
          	      nonceStr: vm.order.nonceStr,
          	      signature: vm.order.signature,
          	      jsApiList: [
          	        'chooseWXPay',
          	      ]
                });
                
                wx.ready(function () {
                	vm.paymentResult='ready';
                	vm.payment();
              	});
                
                $timeout(function () {
                    vm.cardAnimationClass = ''; 
                }, 1000);
            }, function (error) {
            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
            });
        }
        vm.payment = function () {
        	if(vm.paymentResult=='paying'){
        		
        		wx.chooseWXPay({
		    	      timestamp: vm.paymentData.timeStamp,
		    	      nonceStr: vm.paymentData.nonceStr,
		    	      package: 'prepay_id='+ vm.paymentData.prepay_id,
		    	      signType: 'MD5',
		    	      paySign: vm.paymentData.paySign,
		    	      success: function (res) {
          				vm.paymentResult = 'success';
				      		 var url =location.href.split('#')[0];
				      		 toaster.pop('success', "支付完成", "恭喜您订单支付完成！");
				      		 window.location.href=url+"#/orders?order_id="+orderId+"&state=payed";
				  		}
		    	    });
          		wx.error(function (res) {
      	    	  alert(res.errMsg);
      	    	});
        	}else{
        		
        		if(vm.paymentResult=='prepare'){
        			toaster.pop('info', "请稍候", "微信正在加载中，请稍后！");
        			return;
        		}
        		
        		vm.paymentResult='prepare';
	        	var url =location.href.split('#')[0];
	        	vm.url=url;
	            dataService.payment(orderId)
	            .then(function (data) {
	            	vm.paymentResult='paying';
	            	vm.paymentData = data;
	                $timeout(function () {
	                    vm.cardAnimationClass = ''; //Turn off animation since it won't keep up with filtering
	                }, 1000);
	            }, function (error) {
	            	toaster.pop('error', "处理失败", "很遗憾处理失败，由于网络原因无法连接到服务器！");
	            });
        	}
        };
        
        function init() {
        	getOrder();
        }
        init();
    };

    paymentController.$inject = injectParams;
    angular.module('shopApp').controller('PaymentController', paymentController);

}());