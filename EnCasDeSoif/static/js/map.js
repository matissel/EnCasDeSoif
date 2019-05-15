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

function addMap(allpe){
    var geojson =allpe;
    
    mapboxgl.accessToken = 'pk.eyJ1IjoibWF0aXNzb3UiLCJhIjoiY2plOGFtdWhvMDZuNzMzcHIxZTNuMXo0dSJ9.aPI9ecTNZg0-ExUGEPX14w';
    //mapboxgl.accessToken = "{{ mapbox_access_token }}"
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [5.761094, 45.178086],
        zoom: 12.3
        });
    
    ajouterLocalisationActuelle(map)

    map.on('load', function() {
        // Add a new source from our GeoJSON data and set the
        // 'cluster' option to true. GL-JS will add the point_count property to your source data.
        map.addSource("pointsEau", {
        type: "geojson",
        // Point to GeoJSON data. This example visualizes all M1.0+ pointsEau
        // from 12/22/15 to 1/21/16 as logged by USGS' Earthquake hazards program.
        data: geojson,
        cluster: true,
        clusterMaxZoom: 14, // Max zoom to cluster points on
        clusterRadius: 50 // Radius of each cluster when clustering points (defaults to 50)
        });
         
        map.addLayer({
        id: "clusters",
        type: "circle",
        source: "pointsEau",
        filter: ["has", "point_count"],
        paint: {
        // Use step expressions (https://docs.mapbox.com/mapbox-gl-js/style-spec/#expressions-step)
        // with three steps to implement three types of circles:
        //   * Blue, 20px circles when point count is less than 100
        //   * Yellow, 30px circles when point count is between 100 and 750
        //   * Pink, 40px circles when point count is greater than or equal to 750
        "circle-color": [
        "step",
        ["get", "point_count"],
        "#51bbd6",
        100,
        "#f1f075",
        750,
        "#f28cb1"
        ],
        "circle-radius": [
        "step",
        ["get", "point_count"],
        20,
        100,
        30,
        750,
        40
        ]
        }
        });
         
        map.addLayer({
        id: "cluster-count",
        type: "symbol",
        source: "pointsEau",
        filter: ["has", "point_count"],
        layout: {
        "text-field": "{point_count_abbreviated}",
        "text-font": ["DIN Offc Pro Medium", "Arial Unicode MS Bold"],
        "text-size": 12
        }
        });
         
        map.addLayer({
        id: "unclustered-point",
        type: "circle",
        source: "pointsEau",
        filter: ["!", ["has", "point_count"]],
        paint: {
        "circle-color": "#11b4da",
        "circle-radius": 8,
        "circle-stroke-width": 1,
        "circle-stroke-color": "#fff"
        }
        });
         
        // inspect a cluster on click
        map.on('click', 'clusters', function (e) {
        var features = map.queryRenderedFeatures(e.point, { layers: ['clusters'] });
        var clusterId = features[0].properties.cluster_id;
        map.getSource('pointsEau').getClusterExpansionZoom(clusterId, function (err, zoom) {
        if (err)
        return;
         
        map.easeTo({
        center: features[0].geometry.coordinates,
        zoom: zoom
        });
        });
        });
         
        map.on('mouseenter', 'clusters', function () {
        map.getCanvas().style.cursor = 'pointer';
        });
        map.on('mouseleave', 'clusters', function () {
        map.getCanvas().style.cursor = '';
        });
        });
        
        map.on('click', 'unclustered-point', function (e) {
            var coordinates = e.features[0].geometry.coordinates.slice();
            var description = e.features[0].properties.description;
            var nom = e.features[0].properties.title
             
            // Ensure that if the map is zoomed out such that multiple
            // copies of the feature are visible, the popup appears
            // over the copy being pointed to.
            while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
            }
             
            new mapboxgl.Popup()
            .setLngLat(coordinates)
            .setHTML("<h3>" + nom + "</h3><p>" +  description + "</p>")
            .addTo(map);
            });

     

}
