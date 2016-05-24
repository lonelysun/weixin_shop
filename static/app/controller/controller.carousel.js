(function () {
    var myController = function ($scope,$http) {
    	
    	
    	$scope.myInterval = 5000;
    	
        $scope.slides = [];
        $http({
            method: 'Get',
            url: '/api/carousel'
        }).success(function (data, status, headers, config) {
            $scope.slides=data.items;
            $scope.myInterval=data.interval;
        }).error(function (data, status, headers, config) {
            $scope.message = '连接失败';
        });
    };
    angular.module('shopApp').controller('myController', myController);

}());
