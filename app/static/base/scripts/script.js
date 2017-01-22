console.log("elo kurwa");
var myApp = angular.module('myApp',[]);
myApp.controller('GreetingController', function($scope, $http) {
    console.log("wysylam kurwa");
    $http({
            method : "GET",
            url : "/api/books.json"
        }).then(function success(response) {
            console.log("success kurwa");
            $scope.greeting=response;
        }, function error(response) {
            console.log("error kurwa "+response);
        });
    $scope.greeting = 'Hola!';
});