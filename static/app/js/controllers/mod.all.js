'use strict';

/* Controllers */
app.controller('ModCarousel', ['$scope', '$http', '$state', 'shopService',
    function ($scope, $http, $state, shopService) {
        $scope.interval = 5000;
        $scope.slides = [];
        shopService.getCarousel('mobile_top').then(function (result) {
            if (result.errcode==0) {
                $scope.slides = result.data.items;
                $scope.interval = result.data.interval;
            }
        }, function (error) {
            console.log(error);
        });
    }]
);

app.controller('ModContact', ['$scope', '$http', '$state', 'shopService',
    function ($scope, $http, $state, shopService) {
        $scope.company = {};
        shopService.getContact().then(function (result) {
            if (result.errcode==0) {
                $scope.company = result.data;
                
            }
        }, function (error) {

        });
    }]
);
app.controller('ModNav', ['$scope', '$http', '$state', 'shopService',
    function ($scope, $http, $state, shopService) {
        console.info('sss');
        $scope.items = [];

        shopService.getNav('mobile_nav').then(function (data) {
            $scope.items=data.items;
        }, function (error) {

        });
    }]
);