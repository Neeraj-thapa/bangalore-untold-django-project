// Initialize the map
var map = L.map('map').setView([12.9716, 77.5946], 12);

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Marker Data (Sample)
var places = [
    { name: "KR Market", category: "markets", lat: 12.9618, lon: 77.5800, description: "One of the oldest markets in Bangalore." },
    { name: "Bangalore Fort", category: "historic", lat: 12.9634, lon: 77.5734, description: "Built by Kempe Gowda in the 16th century." },
    { name: "Rasta Café", category: "cafes", lat: 12.8341, lon: 77.6789, description: "Popular late-night café on Mysore Road." },
    { name: "Turahalli Forest", category: "nature", lat: 12.8755, lon: 77.5200, description: "Perfect for trekking and nature walks." }
];

// Store markers
var markers = [];

// Add markers to map
places.forEach(function (place) {
    var marker = L.marker([place.lat, place.lon]).addTo(map)
        .bindPopup("<b>" + place.name + "</b><br>" + place.description);
    
    marker.category = place.category;
    markers.push(marker);
});

// Filter function
function filterMarkers() {
    var selectedCategory = document.getElementById("category-filter").value;
    
    markers.forEach(marker => {
        if (selectedCategory === "all" || marker.category === selectedCategory) {
            map.addLayer(marker);
        } else {
            map.removeLayer(marker);
        }
    });
}

// Search function
function searchLocation() {
    var searchText = document.getElementById("search-box").value.toLowerCase();
    
    markers.forEach(marker => {
        if (marker.getPopup().getContent().toLowerCase().includes(searchText)) {
            marker.openPopup();
            map.setView(marker.getLatLng(), 14);
        }
    });
}
