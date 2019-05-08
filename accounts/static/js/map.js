
function addMap(allpe){
    var geojson =allpe;
        
    mapboxgl.accessToken = 'pk.eyJ1IjoibWF0aXNzb3UiLCJhIjoiY2plOGFtdWhvMDZuNzMzcHIxZTNuMXo0dSJ9.aPI9ecTNZg0-ExUGEPX14w';
    //mapboxgl.accessToken = "{{ mapbox_access_token }}"
    const map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/matissou/cjv81ltxb0drl1fo5f2as7tgk',
        center: [5.761094, 45.178086],
        zoom: 12.3
        });


    geojson.features.forEach(function(marker) {

        // create a HTML element for each feature
        var el = document.createElement('div');
        el.className = 'marker';

        // make a marker for each feature and add it to the map
        new mapboxgl.Marker(el)
            .setLngLat(marker.geometry.coordinates)
            .setPopup(new mapboxgl.Popup({offset: 25}) // add popups
                .setHTML('<h3>' + marker.properties.title + '</h3><p>' + marker.geometry.coordinates + '</p>'))
            .addTo(map); 
    });
        

}
