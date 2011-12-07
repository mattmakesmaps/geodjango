//Load JSON URL and fire callback creating map

var geoJSONBaseURL = "http://localhost:8000/company/geojson/boundary/";
var geoJSONURL = geoJSONBaseURL + boundary_id;

$.getJSON(geoJSONURL, makeMap);

function makeMap(data){
  //Assign GeoJSON to variable
  var sitePoly = data

  //Create map instance
  var map = new L.Map('map')
  var boundaryGeoJSON = new L.GeoJSON(sitePoly);

  var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/5df4a1ed4a8c41bd91725ad594aa6139/997/256/{z}/{x}/{y}.png'
  var cloudmadeAttrib = 'Map data &copy; 2011 OpenStreetMap contributors, Imagery &copy; 2011 CloudMade'
  var cloudmade = new L.TileLayer(cloudmadeUrl, {maxZoom: 18, attribution: cloudmadeAttrib});

  // See: http://developer.mapquest.com/web/products/open/map
  var mapQuestAerialURL = 'http://{s}.mqcdn.com/tiles/1.0.0/sat/{z}/{x}/{y}.png'
  var mapQuestAerialAttrib = 'Portions Courtesy NASA/JPL-Caltech and U.S. Depart. of Agriculture, Farm Service Agency. Thanks MapQuest!'
  var mapQuestAerial = new L.TileLayer(mapQuestAerialURL, {
                                                           maxZoom: 18, 
                                                           attribution: mapQuestAerialAttrib, 
                                                           subdomains: ['oatile1','oatile2','oatile3','oatile4']
                                                        });
  map.addLayer(cloudmade);
  map.addLayer(mapQuestAerial);
  map.addLayer(boundaryGeoJSON);
  map.fitBounds(bounds);

  // Group layers and add layerswitching
  // Requires leaflet master... WORD!!!
  var baseMaps = {"Road": cloudmade, "Aerial": mapQuestAerial};
  var overlayMaps = {"Client Boundary": boundaryGeoJSON};

  var layersControl = new L.Control.Layers(baseMaps, overlayMaps);
  map.addControl(layersControl);
}
