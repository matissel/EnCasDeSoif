function addMap(lat,long){

    mapboxgl.accessToken = 'pk.eyJ1IjoibWF0aXNzb3UiLCJhIjoiY2plOGFtdWhvMDZuNzMzcHIxZTNuMXo0dSJ9.aPI9ecTNZg0-ExUGEPX14w';
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [5.761094, 45.178086],
        zoom: 12.3
        });

    // Add geolocate control to the map.
    const geolocControl = new mapboxgl.GeolocateControl({
        positionOptions: {
        enableHighAccuracy: true
        },
        trackUserLocation: true
        });
    
    // Add the control to the map
    map.addControl(geolocControl)

   
    marker = new mapboxgl.Marker({draggable:true})
    
    geolocControl.on('geolocate', function(e) {
        var lon = e.coords.longitude;
        var lat = e.coords.latitude
        marker.setLngLat([lon,lat])
    });

     //Set a timeout. When 3sec elasped, click on the geolocalisation automatically 
     setTimeout(function() {
        $(".mapboxgl-ctrl-geolocate").click();
        marker.addTo(map);
    },3000);
    
    function onDragEnd() {
        var lngLat = marker.getLngLat();
        document.getElementById(lat.id).value = lngLat.lat.toFixed(8)
        document.getElementById(long.id).value = lngLat.lng.toFixed(8)        
    }
    
    marker.on('dragend', onDragEnd);

}


