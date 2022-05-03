
$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + MAP_KEY + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutocomplete())

})

function onCampusRoutes() {
  var RouteID = document.getElementById('On Campus').value;
  campusRoutes(RouteID);
}

function offCampusRoutes() {
  var RouteID = document.getElementById('Off Campus').value;
  campusRoutes(RouteID);
}

function campusRoutes(RouteID) {
  const ALL_ROUTES = JSON.parse(document.getElementById('ALL_ROUTES').textContent);
  var latLongList = [];
  for (var i = 0; i < ALL_ROUTES.length; i++) {
    // find the route identified by the dropdown
    if (ALL_ROUTES[i].ID == RouteID) {
      var thisRoute = ALL_ROUTES[i];
      var lastStop = thisRoute.Stops[thisRoute.Stops.length - 1].Number;
      // create all stops w/ latitude and longitude values
      for (var j = 0; j < lastStop; j++) {
        var latLong = {
          "lat": thisRoute.Stops[j].Lat,
          "long": thisRoute.Stops[j].Long,
        };
        latLongList.push(latLong);
      }
      // fill variables until w
      for (var j = lastStop; j < 23; j++) {
        var latLong = {
          "lat": thisRoute.Stops[0].Lat,
          "long": thisRoute.Stops[0].Long,
        };
        latLongList.push(latLong);
      }
      break;
    }
  }
  // fill correct variables with accumulated values
  var Lata = document.getElementById("id-lat-a");
  Lata.value = latLongList[0].lat;
  var Longa = document.getElementById("id-long-a");
  Longa.value = latLongList[0].long;
  var Latb = document.getElementById("id-lat-b");
  Latb.value = latLongList[22].lat;
  var Longb = document.getElementById("id-long-b");
  Longb.value = latLongList[22].long;
  var Latc = document.getElementById("id-lat-c");
  Latc.value = latLongList[1].lat;
  var Longc = document.getElementById("id-long-c");
  Longc.value = latLongList[1].long;
  var Latd = document.getElementById("id-lat-d");
  Latd.value = latLongList[2].lat;
  var Longd = document.getElementById("id-long-d");
  Longd.value = latLongList[2].long;
  var Late = document.getElementById("id-lat-e");
  Late.value = latLongList[3].lat;
  var Longe = document.getElementById("id-long-e");
  Longe.value = latLongList[3].long;
  var Latf = document.getElementById("id-lat-f");
  Latf.value = latLongList[4].lat;
  var Longf = document.getElementById("id-long-f");
  Longf.value = latLongList[4].long;
  var Latg = document.getElementById("id-lat-g");
  Latg.value = latLongList[5].lat;
  var Longg = document.getElementById("id-long-g");
  Longg.value = latLongList[5].long;
  var Lath = document.getElementById("id-lat-h");
  Lath.value = latLongList[6].lat;
  var Longh = document.getElementById("id-long-h");
  Longh.value = latLongList[6].long;
  var Lati = document.getElementById("id-lat-i");
  Lati.value = latLongList[7].lat;
  var Longi = document.getElementById("id-long-i");
  Longi.value = latLongList[7].long;
  var Latj = document.getElementById("id-lat-j");
  Latj.value = latLongList[8].lat;
  var Longj = document.getElementById("id-long-j");
  Longj.value = latLongList[8].long;
  var Latk = document.getElementById("id-lat-k");
  Latk.value = latLongList[9].lat;
  var Longk = document.getElementById("id-long-k");
  Longk.value = latLongList[9].long;
  var Latl = document.getElementById("id-lat-l");
  Latl.value = latLongList[10].lat;
  var Longl = document.getElementById("id-long-l");
  Longl.value = latLongList[10].long;
  var Latm = document.getElementById("id-lat-m");
  Latm.value = latLongList[11].lat;
  var Longm = document.getElementById("id-long-m");
  Longm.value = latLongList[11].long;
  var Latn = document.getElementById("id-lat-n");
  Latn.value = latLongList[12].lat;
  var Longn = document.getElementById("id-long-n");
  Longn.value = latLongList[12].long;
  var Lato = document.getElementById("id-lat-o");
  Lato.value = latLongList[13].lat;
  var Longo = document.getElementById("id-long-o");
  Longo.value = latLongList[13].long;
  var Latp = document.getElementById("id-lat-p");
  Latp.value = latLongList[14].lat;
  var Longp = document.getElementById("id-long-p");
  Longp.value = latLongList[14].long;
  var Latq = document.getElementById("id-lat-q");
  Latq.value = latLongList[15].lat;
  var Longq = document.getElementById("id-long-q");
  Longq.value = latLongList[15].long;
  var Latr = document.getElementById("id-lat-r");
  Latr.value = latLongList[16].lat;
  var Longr = document.getElementById("id-long-r");
  Longr.value = latLongList[16].long;
  var Lats = document.getElementById("id-lat-s");
  Lats.value = latLongList[17].lat;
  var Longs = document.getElementById("id-long-s");
  Longs.value = latLongList[17].long;
  var Latt = document.getElementById("id-lat-t");
  Latt.value = latLongList[18].lat;
  var Longt = document.getElementById("id-long-t");
  Longt.value = latLongList[18].long;
  var Latu = document.getElementById("id-lat-u");
  Latu.value = latLongList[19].lat;
  var Longu = document.getElementById("id-long-u");
  Longu.value = latLongList[19].long;
  var Latv = document.getElementById("id-lat-v");
  Latv.value = latLongList[20].lat;
  var Longv = document.getElementById("id-long-v");
  Longv.value = latLongList[20].long;
  var Latw = document.getElementById("id-lat-w");
  Latw.value = latLongList[21].lat;
  var Longw = document.getElementById("id-long-w");
  Longw.value = latLongList[21].long;
  CalcRoute();
}

var auto_fields = ['a', 'b']

function initAutocomplete() {

  for (i = 0; i < auto_fields.length; i++) {
    var field = auto_fields[i]
    window['autocomplete_'+field] = new google.maps.places.Autocomplete(
      document.getElementById('id-google-address-' + field),
    {
       types: ['address'],
       componentRestrictions: {'country': [base_country.toLowerCase()]},
    })
  }

  autocomplete_a.addListener('place_changed', function(){
          onPlaceChanged('a')
      });
  autocomplete_b.addListener('place_changed', function(){
          onPlaceChanged('b')
      });
  
}

var sourceCoords = {};
var destCoords = {};

function onPlaceChanged (add){

  var auto = window['autocomplete_'+add]
  var el_id = 'id-google-address-'+add
  var lat_id = 'id-lat-' + add
  var long_id = 'id-long-' + add

  var geocoder = new google.maps.Geocoder()
  var address = document.getElementById(el_id).value

  geocoder.geocode( { 'address': address}, function(results, status) {

      if (status == google.maps.GeocoderStatus.OK) {
          var latitude = results[0].geometry.location.lat();
          var longitude = results[0].geometry.location.lng();

          if (add == 'a') {
            sourceCoords["Lat"] = latitude;
            sourceCoords["Long"] = longitude;
          }

          if (add == 'b') {
            destCoords["Lat"] = latitude;
            destCoords["Long"] = longitude;
          }

          $('#' + lat_id).val(latitude) 
          $('#' + long_id).val(longitude) 

          CalcRoute()
      } 
  });
}

function calcHypotenuse(a, b) {
  return (Math.sqrt((a * a) + (b * b)));
}

document.getElementById("mapNavigate").addEventListener("click", function() {
  // for source:
  const ALL_ROUTES = JSON.parse(document.getElementById('ALL_ROUTES').textContent);
  var minDistanceSource = 999999999.9;
  var minRouteSource = 1;
  var minStopSource = 1;
  for (var i = 0; i < ALL_ROUTES.length; i++) {
    var thisRoute = ALL_ROUTES[i];
    // iterate through each stop of each route
    for (var j = 0; j < thisRoute.Stops.length; j++) {
      var thisStop = thisRoute.Stops[j];
      // get the lat and long
      var thisLat = thisStop.Lat;
      var thisLong = thisStop.Long;
      // calculate the difference (via hypotenuse)
      var distance = calcHypotenuse(sourceCoords.Lat - thisLat, sourceCoords.Long - thisLong);
      // store minimum & related values -> nearest source stop
      if (distance < minDistanceSource) {
        minDistanceSource = distance;
        minRouteSource = i;
        minStopSource = j;
      }
    }
  }

  // determine which routes contain the source stop name
  var minStopName = ALL_ROUTES[minRouteSource].Stops[minStopSource].Name;
  console.log("Stop name: " + minStopName);
  var routeList = [];
  for (var i = 0; i < ALL_ROUTES.length; i++) {
    for (var j = 0; j < ALL_ROUTES[i].Stops.length; j++) {
      if (ALL_ROUTES[i].Stops[j].Name == minStopName) {
        console.log("Adding route " + ALL_ROUTES[i].Name);
        routeList.push(i);
        break;
      }
    }
  }

  // for destination:
  var minDistanceDest = 999999999.9;
  var minRouteDest = minRouteSource;
  var minStopDest = 1;
  // iterate through each route with the same stop name as the source stop
  for (var i = 0; i < routeList.length; i++) {
    currRoute = ALL_ROUTES[routeList[i]];
    // iterate through each stop of each route
    for (var j = 0; j < currRoute.Stops.length; j++) {
      var thisStop = currRoute.Stops[j];
      // get the lat and long
      var thisLat = thisStop.Lat;
      var thisLong = thisStop.Long;
      // calculate the difference (via hypotenuse)
      var distance = calcHypotenuse(destCoords.Lat - thisLat, destCoords.Long - thisLong);
      // store minimum & related values -> nearest dest stop
      if (distance < minDistanceDest) {
        minDistanceDest = distance;
        minRouteDest = routeList[i];
        minStopDest = j;
      }
    }
  }

  $.ajax({
    url: "/update_stop",
    type: "GET",
    data: {
      routeName: ALL_ROUTES[minRouteDest].Name,
      routeNumber: ALL_ROUTES[minRouteDest].Number,
      sourceStop: minStopName,
      destStop: ALL_ROUTES[minRouteDest].Stops[minStopDest].Name,
    },
  });

  // output -> call route display for given route ID
  console.log("Route: " + ALL_ROUTES[minRouteDest].Name);
  console.log("Source: " + ALL_ROUTES[minRouteDest].Stops[minStopSource].Name + "; distance " + minDistanceSource);
  console.log("Dest: " + ALL_ROUTES[minRouteDest].Stops[minStopDest].Name + "; distance " + minDistanceDest);

  if (ALL_ROUTES[minRouteDest].Area == "On Campus") {
    document.getElementById("On Campus").value = ALL_ROUTES[minRouteDest].ID;
    onCampusRoutes()
  } else {
    document.getElementById("Off Campus").value = ALL_ROUTES[minRouteDest].ID;
    offCampusRoutes()
  }

  // tell user which stops to take
});

function validateForm() {
  var valid = true;
  $('.geo').each(function () {
      if ($(this).val() === '') {
          valid = false;
          return false;
      }
  });
  return valid
}


function CalcRoute(){

    if ( validateForm() == true){
      var params = {
          lat_a: $('#id-lat-a').val(),
          long_a: $('#id-long-a').val(),
          lat_b: $('#id-lat-b').val(),
          long_b: $('#id-long-b').val(),
          lat_c: $('#id-lat-c').val(),
          long_c: $('#id-long-c').val(),
          lat_d: $('#id-lat-d').val(),
          long_d: $('#id-long-d').val(),
          lat_e: $('#id-lat-e').val(),
          long_e: $('#id-long-e').val(),
          lat_f: $('#id-lat-f').val(),
          long_f: $('#id-long-f').val(),
          lat_g: $('#id-lat-g').val(),
          long_g: $('#id-long-g').val(),
          lat_h: $('#id-lat-h').val(),
          long_h: $('#id-long-h').val(),
          lat_i: $('#id-lat-i').val(),
          long_i: $('#id-long-i').val(),
          lat_j: $('#id-lat-j').val(),
          long_j: $('#id-long-j').val(),
          lat_k: $('#id-lat-k').val(),
          long_k: $('#id-long-k').val(),
          lat_l: $('#id-lat-l').val(),
          long_l: $('#id-long-l').val(),
          lat_m: $('#id-lat-m').val(),
          long_m: $('#id-long-m').val(),
          lat_n: $('#id-lat-n').val(),
          long_n: $('#id-long-n').val(),
          lat_o: $('#id-lat-o').val(),
          long_o: $('#id-long-o').val(),
          lat_p: $('#id-lat-p').val(),
          long_p: $('#id-long-p').val(),
          lat_q: $('#id-lat-q').val(),
          long_q: $('#id-long-q').val(),
          lat_r: $('#id-lat-r').val(),
          long_r: $('#id-long-r').val(),
          lat_s: $('#id-lat-s').val(),
          long_s: $('#id-long-s').val(),
          lat_t: $('#id-lat-t').val(),
          long_t: $('#id-long-t').val(),
          lat_u: $('#id-lat-u').val(),
          long_u: $('#id-long-u').val(),
          lat_v: $('#id-lat-v').val(),
          long_v: $('#id-long-v').val(),
          lat_w: $('#id-lat-w').val(),
          long_w: $('#id-long-w').val(),
      };

      var esc = encodeURIComponent;
      var query = Object.keys(params)
          .map(k => esc(k) + '=' + esc(params[k]))
          .join('&');

      url = '/map?' + query
      window.location.assign(url)
    }

}
