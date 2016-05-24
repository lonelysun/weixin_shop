(function () {

    var injectParams = ['$http', '$q','memoryCart'];

    var productsFactory = function ($http, $q,memoryCart) {
        var serviceBase = '/wxshop/',
            factory = {};
        
        factory.getProducts = function (category_id) {
        	 return $http.get(serviceBase + 'products', {
     			params : {
        		 category_id:category_id
     				}
     			}).then(function(results) {
     				return results.data;
     			});
        };
        
        function getCartsQty(){
        	 $http.get(serviceBase + 'cartsQty', {
     			params : {
     				}
     			}).then(function(results) {
     				memoryCart.qty=results.data;
     			});
        }

        function getPagedResource(baseResource, pageIndex, pageSize) {
            var resource = baseResource;
            resource += (arguments.length == 3) ? buildPagingUri(pageIndex, pageSize) : '';
            return $http.get(serviceBase + resource).then(function (response) {
                var custs = response.data;
                //extendCustomers(custs);
                return {
                    totalRecords: parseInt(response.headers('X-InlineCount')),
                    results: custs
                };
            });
        }
        
        factory.getProduct = function (id) {
            return $http.get(serviceBase + 'product/' + id).then(function (results) {
                //extendCustomers([results.data]);
                return results.data;
            });
        };
        
        factory.getAccount = function (id) {
            return $http.get(serviceBase + 'account').then(function (results) {
                return results.data;
            });
        };
        
        factory.saveAccount = function (account) {
            return $http.post(serviceBase + 'saveAccount/' + account.id, account).then(function (status) {
                return status.data;
            });
        };
        
        factory.getOrder = function (id,url) {
        	return $http.get(serviceBase + 'order', {
    			params : {
    				url :url,
    				order_id:id
    				}
    			}).then(function(results) {
    				return results.data;
    			});

        };
        factory.payment = function (id) {
        	return $http.get(serviceBase + 'payment', {
    			params : {
    				order_id:id
    				}
    			}).then(function(results) {
    				return results.data;
    			});
        };
        
        factory.updateOrder = function (order_id,state) {
            return $http.get(serviceBase + 'updateOrder', {
    			params : {
	            	order_id:order_id,
	            	state:state
    				}
    			}).then(function(results) {
    				return results.data;
    			});
        };
        
        factory.getCategorys = function () {
            return getPagedResource('categorys', 0, 100);
        };
        
        
        factory.getUserProducts = function () {
            return getPagedResource('userProducts', 0, 100);
        };
        
        factory.getCoupons = function (orderId) {
        	
        	 return $http.get(serviceBase + 'coupons', {
     			params : {
        		 orderId:orderId,
     				}
     			}).then(function(results) {
     				return results.data;
     			});
        	 
        };
        
        
        factory.getOrders = function (order_id,state) {
            return $http.get(serviceBase + 'orders', {
    			params : {
            	order_id:order_id,
            	state:state
    				}
    			}).then(function(results) {
    				return results.data;
    			});
        };
        
        factory.getCarousel = function (type) {
            return $http.get(serviceBase + 'carousel', {
    			params : {
            	position:type
    				}
    			}).then(function(results) {
    				return results.data;
    			});
        };
        
        factory.getCategory = function () {
            return getPagedResource('category', 0, 100);
        };
        
        
        factory.getCarts = function () {
            return getPagedResource('carts', 0, 100);
        };
        
        factory.getAddress = function () {
            return getPagedResource('address', 0, 100);
        };
        
        factory.getProfile = function () {
        	return $http.get(serviceBase + 'profile', {
    			params : {
    				}
    			}).then(function(results) {
    				return results.data;
    			});
        };
        
        factory.addCart = function (customer) {
            return $http.post(serviceBase + 'addCart', customer).then(function (results) {
            	getCartsQty();
                return results.data;
            });
        };
        
        factory.addFollow = function (product) {
            return $http.post(serviceBase + 'follow', product).then(function (results) {
                return results.data;
            });
        };
        
        
        factory.checkout = function (customer) {
            return $http.post(serviceBase + 'checkout', customer).then(function (results) {
            	getCartsQty();
                return results.data;
            });
        };
        
        factory.deleteCartItem = function (id) {

            return $http.post(serviceBase + 'deleteItem', id).then(function (results) {
            	getCartsQty();
                return results.data;
            });
        };
        
        factory.changeQty = function (item) {
            return $http.post(serviceBase + 'changeQty', item).then(function (results) {
                return results.data;
            });
        };
        
        function buildPagingUri(pageIndex, pageSize) {
            var uri = '?$top=' + pageSize + '&$skip=' + (pageIndex * pageSize);
            return uri;
        }
        
        getCartsQty();

        return factory;
    };

    productsFactory.$inject = injectParams;

    angular.module('shopApp').factory('shopService', productsFactory);

}());