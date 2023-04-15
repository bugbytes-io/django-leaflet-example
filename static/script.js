function createMap(center, zoom) {
    let map = L.map('map').setView(center, zoom);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    return map
}

function updateMarkers(markerFeatureGroup) {
    // Send a request to the server to get the new latitude and longitude data
    fetch('/vehicle-positions/').then(response => response.json()).then(data => {
        let prevLatLons = []
        markerFeatureGroup.eachLayer(layer => layer.hasOwnProperty('_latlng') && prevLatLons.push(layer._latlng))
        
        markerFeatureGroup.clearLayers();

        data.vehicles.forEach((vehicle, idx) => {
            let prevLatLon = [prevLatLons[idx].lat, prevLatLons[idx].lng]
            let newLatLon = [vehicle.latitude, vehicle.longitude];
            L.marker(newLatLon).addTo(markerFeatureGroup);
            L.polyline([prevLatLon, newLatLon]).addTo(markerFeatureGroup)
        })
    })

}