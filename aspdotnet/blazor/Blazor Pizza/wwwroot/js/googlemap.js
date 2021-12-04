function initializeGoogleMap(lat, lon) {
    var latlng = new google.maps.LatLng(lat, lon);
    var options = {
        zoom: 16, center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById ("map"), options);
    new google.maps.Marker({
    position: latlng,
    map,
    title: "Cavenagh Hotel",
});
}
