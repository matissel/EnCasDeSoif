var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  };

fixerLocalisationCourante = function(lat, long){
   
   navigator.geolocation.getCurrentPosition(function(pos){
       var crd = pos.coords;
       //set latitude value 
        var latitude = crd.latitude 
        var longitude = crd.longitude
       document.getElementById(lat.id).value = latitude.toFixed(8)
       //set longitude 
       document.getElementById(long.id).value = longitude.toFixed(8) 
    
   })
}