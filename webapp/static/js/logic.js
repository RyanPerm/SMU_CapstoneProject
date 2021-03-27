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
    var road_type = $("#road_type").val();
    var distance = $("#distance").val();
    var visibility = $("#visibility").val();


    // create the payload
    var payload = {
        "condition": condition,
        "temperature": temperature,
        "wind_speed": wind_speed,
        "pressure": pressure,
        "humidity": humidity,
        "side": road_side,
        "type": road_type,
        "distance": distance,
        "visibility": visibility
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
            makePlot(returnedData)
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });
}


function makePlot(returnedData) {

    var maxProb = parseInt(returnedData['prediction']['point']) - 1

    var colors = ["blue", "blue", "blue", "blue"];
    colors[maxProb] = "red";


    var barPlot = [{
        x: [1, 2, 3, 4],
        y: returnedData["prediction"]["proba"],
        type: 'bar',
        marker: {
            color: colors
        }
    }];

    var layout = {
        title: "Probability of Severity",
        xaxis: {
            title: "Severity Score",

        },
        yaxis: {
            title: "Probability"
        }
    }

    Plotly.newPlot('bar', barPlot, layout);
}