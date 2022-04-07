// Initialize and add map display
function initMap() {
    // College Station coords
    const cstatcoords = {lat: 30.626031, lng: -96.335160};
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: cstatcoords,
    });
}
