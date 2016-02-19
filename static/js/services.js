/**
 * Created by Sandeep on 01/06/14.
 */

/*
http://127.0.0.1:8000/trabajos2/trabajos/
http://movieapp-13434.onmodulus.net/api/movies/
*/

angular.module('movieApp.services',[]).factory('Movie',function($resource){
    return $resource('http://127.0.0.1:8000/trabajos2/trabajos/:id',{id:'@id'},{
        update: {
            method: 'PUT'
        }
    });
}).service('popupService',function($window){
    this.showPopup=function(message){
        return $window.confirm(message);
    }
});