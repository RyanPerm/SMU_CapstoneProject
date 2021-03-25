$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        makePredictions();
    });
});

// call Flask API endpoint
function makePredictions() {
    var condition = $("#condition").val();
    var temperature = $("#temp").val();
    var wind_speed = $("#windSpeed").val();
    var pressure = $("#pressure").val();
    var humidity = $("#humid").val();
    var road_side = $("#side").val();


    // create the payload
    var payload = {
        "condition": condition,
        "temp": temp,
        "windSpeed": windSpeed,
        "severity": severity,
        "humid": humid
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            // need to make if statment 
            if (returnedData["prediction"] == 1) {
                $("#output").text("You Survived!");
            } else {
                $("#output").text("You Died!");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}