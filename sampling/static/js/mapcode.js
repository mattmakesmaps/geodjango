//Load JSON URL and fire callback creating map

var geoJSONBaseURL = "http://localhost:8000/geojson/boundary/";
var geoJSONURL = geoJSONBaseURL + boundary_id;

$.getJSON(geoJSONURL, makeMap);

function makeMap(data){
  //Assign GeoJSON to variable
  var sitePoly = data

  //Create map instance
  var map = new L.Map('map')
  var geojsonLayer = new L.GeoJSON(sitePoly);

  var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/5df4a1ed4a8c41bd91725ad594aa6139/997/256/{z}/{x}/{y}.png',
    cloudmadeAttrib = 'Map data &copy; 2011 OpenStreetMap contributors, Imagery &copy; 2011 CloudMade',
    cloudmade = new L.TileLayer(cloudmadeUrl, {maxZoom: 18, attribution: cloudmadeAttrib});

  var wa = new L.LatLng(47.6, -122);
  map.setView(wa, 08).addLayer(cloudmade);
  map.addLayer(geojsonLayer);
}
