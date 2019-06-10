var myApp = angular.module('imageuploadFrontendApp', ['ngResource','ngFileUpload']);
myApp.config(function($resourceProvider){
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.controller('MainCtrl', function($scope, Images)
{
    console.log('In main Control');
    $scope.images = Images.query();
    $scope.newImage={};

    $scope.deleteImage = function(image)
    {
        image.$delete(
      function(response){
        $scope.images = Images.query();
      }
      );
    };

    $scope.uploadImage = function()
    {
      console.log('Upload image called');
      Images.save($scope.newImage).$promise.then(
      function(response){
        $scope.images.unshift(response);
      }
      );
    };
});

myApp.directive('filesModel', filesModelDirective)