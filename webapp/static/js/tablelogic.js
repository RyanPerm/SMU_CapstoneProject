var table_data = the_data;

$(document).ready(function() {
    $('#severity-table').DataTable();
    buildFilters();
    buildTable();

    // 
    $("#filter-btn").on("click", function(e) {
        e.preventDefault();
        buildTable();
    });
    $("#filter-clear").on("click", function(e) {
        e.preventDefault();
        resetFilters();
    });
    $("#form").on("submit", function(e) {
        e.preventDefault();
        buildTable();
    });
});

function buildFilters() {
    // buildUniqueFilterHelper("Start_Time", "Start_Time");
    buildUniqueFilterHelper("County", "County");
    // buildUniqueFilterHelper("Severity", "Severity");
}

function resetFilters() {
    // $("#Start_Time").val("");
    // $("#Start_Time").text("");

    $("#County").val("");
    $("#County").text("");

    $("#Severity").val("");
    // $("#Severity").text("");
}

function buildUniqueFilterHelper(colName, filterID) {
    var unq_column = [...new Set(table_data.map(x => x[colName]))];
    unq_column = unq_column.sort();
    unq_column.forEach(function(val) {
        var newOption = `<option>${val.toUpperCase()}</option>`;
        $(`#${filterID}`).append(newOption);
    });
}

function buildTable() {
    // var dateFilter = $("#datetime").val(); //gets input value to filter
    var countyFilter = $("#County").val();
    var severityFilter = $("#Severity").val();

    //apply filters
    var filteredData = table_data;
    // if (dateFilter) {
    //     filteredData = filteredData.filter(row => Date.parse(row.datetime) === Date.parse(dateFilter));
    // }
    if (countyFilter) {
        filteredData = filteredData.filter(row => row.countyFilter === countyFilter.toLowerCase());
    }
    if (severityFilter) {
        filteredData = filteredData.filter(row => row.severityFilter === severityFilter.toLowerCase());
    }

    // see if we have any data left
    if (filteredData.length === 0) {
        alert("No Data Found!");
    };

    buildTableString(filteredData);
}

function buildTableString(the_data) {

    // JQUERY creates an HTML string
    var tbody = $("#severity-table>tbody");
    //clear table
    tbody.empty();

    //destroy datatable
    $("#severity-table").DataTable().clear().destroy();

    //append data
    the_data.forEach(function(row) {
        var newRow = "<tr>"
            // loop through each Object (dictionary)
        Object.entries(row).forEach(function([key, value]) {
            // set the cell data
            newRow += `<td>${value}</td>`
        });

        //append to table
        newRow += "</tr>";
        tbody.append(newRow);
    });

    //redraw
    $("#severity-table").DataTable({
        "pagingType": "full_numbers",
        dom: 'Bfrtip', //lbfrtip if you want the length changing thing
        buttons: [
            { extend: 'copyHtml5' },
            { extend: 'excelHtml5' },
            { extend: 'csvHtml5' },
            {
                extend: 'pdfHtml5',
                title: function() { return "UFO Observations"; },
                orientation: 'portrait',
                pageSize: 'LETTER',
                text: 'PDF',
                titleAttr: 'PDF'
            }
        ]
    });

}