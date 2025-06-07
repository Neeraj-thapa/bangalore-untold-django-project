document.addEventListener("DOMContentLoaded", function () {
    var map = L.map('map').setView([12.9716, 77.5946], 12); // Center on Bangalore

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // Example markers for locations
    var locations = [
        { name: "Yediyuru Lake Park", coords: [12.9250, 77.5763] },
        { name: "Uttari Betta", coords: [13.1029, 77.4772] },
        { name: "Mavathur Waterfalls", coords: [12.5603, 77.4623] }
    ];

    locations.forEach(function (location) {
        L.marker(location.coords).addTo(map)
            .bindPopup(`<b>${location.name}</b>`);
    });
});