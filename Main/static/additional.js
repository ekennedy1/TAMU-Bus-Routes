// Initialize and add map display
function initMap() {
    // College Station coords
    var cstatcoords = {lat: 30.626031, lng: -96.335160};
    var mapOptions = {
        center: cstatcoords,
        zoom: 14
    };
    const map = new google.maps.Map(document.getElementById("map"), mapOptions);
}
