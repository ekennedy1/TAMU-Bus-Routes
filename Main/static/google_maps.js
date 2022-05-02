
$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + MAP_KEY + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initMap)

})


function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map-route'), {
        zoom: 7,
        center: {lat: lat_a, lng: long_a}
    });
    directionsDisplay.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsDisplay);

}

const waypts = [
        {location: {lat: lat_c, lng: long_c},
        stopover: true},
        {location: {lat: lat_d, lng: long_d},
        stopover: true},
        {location: {lat: lat_e, lng: long_e},
        stopover: true},
        {location: {lat: lat_f, lng: long_f},
        stopover: true},
        {location: {lat: lat_g, lng: long_g},
        stopover: true},
        {location: {lat: lat_h, lng: long_h},
        stopover: true},
        {location: {lat: lat_i, lng: long_i},
        stopover: true},
        {location: {lat: lat_j, lng: long_j},
        stopover: true},
        {location: {lat: lat_k, lng: long_k},
        stopover: true},
        {location: {lat: lat_l, lng: long_l},
        stopover: true},
        {location: {lat: lat_m, lng: long_m},
        stopover: true},
        {location: {lat: lat_n, lng: long_n},
        stopover: true},
        {location: {lat: lat_o, lng: long_o},
        stopover: true},
        {location: {lat: lat_p, lng: long_p},
        stopover: true},
        {location: {lat: lat_q, lng: long_q},
        stopover: true},
        {location: {lat: lat_r, lng: long_r},
        stopover: true},
        {location: {lat: lat_s, lng: long_s},
        stopover: true},
        {location: {lat: lat_t, lng: long_t},
        stopover: true},
        {location: {lat: lat_u, lng: long_u},
        stopover: true},
        {location: {lat: lat_v, lng: long_v},
        stopover: true},
        {location: {lat: lat_w, lng: long_w},
        stopover: true}
        ];

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    directionsService.route({
        origin: origin,
        destination: destination,
        waypoints: waypts,
        optimizeWaypoints: false,
        travelMode: google.maps.TravelMode.DRIVING,
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);


      } else {

        alert('Directions request failed due to ' + status);
        window.location.assign("/route")
      }
    });
}