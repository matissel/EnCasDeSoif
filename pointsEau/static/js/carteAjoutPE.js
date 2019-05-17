function ajouterLocalisationActuelle(map)
{
    // Add geolocate control to the map.
    const geolocalisation = new mapboxgl.GeolocateControl({
        positionOptions: {
        enableHighAccuracy: true
        },
        trackUserLocation: true
        });
    
    // Add the control to the map
    map.addControl(geolocalisation)

    //Set a timeout. When 3sec elasped, click on the geolocalisation automatically 
    setTimeout(function() {
        $(".mapboxgl-ctrl-geolocate").click();
    },3000);


}

function addMap(){
    
    mapboxgl.accessToken = 'pk.eyJ1IjoibWF0aXNzb3UiLCJhIjoiY2plOGFtdWhvMDZuNzMzcHIxZTNuMXo0dSJ9.aPI9ecTNZg0-ExUGEPX14w';
    //mapboxgl.accessToken = "{{ mapbox_access_token }}"
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [5.761094, 45.178086],
        zoom: 12.3
        });
    
    ajouterLocalisationActuelle(map)
    
    var marker = new mapboxgl.Marker({
        draggable: true
        })
        .setLngLat([5.761094, 45.178086])
        .addTo(map);
         
        function onDragEnd() {
        var lngLat = marker.getLngLat();
        coordinates.style.display = 'block';
        coordinates.innerHTML = 'Longitude: ' + lngLat.lng + '<br />Latitude: ' + lngLat.lat;
        }
         
        marker.on('dragend', onDragEnd);

}


