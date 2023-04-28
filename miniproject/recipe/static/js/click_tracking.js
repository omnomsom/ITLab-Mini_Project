// script.js
$(document).ready(function () {
  var selectedDivs = [];

  $(".square").click(function () {
    $(this).toggleClass("selected");

    var divId = $(this).attr("id");
    var index = selectedDivs.indexOf(divId);

    if (index === -1) {
      selectedDivs.push(divId);
    } else {
      selectedDivs.splice(index, 1);
    }
  });

  $("#submit").click(function () {
    $("#result").val("Selected Divs: " + JSON.stringify(selectedDivs));
    $.ajax({
      type: "POST",
      url: "/process_selected_divs/",
      data: {
        selected_divs: selectedDivs,
        csrfmiddlewaretoken: "{{ csrf_token }}",
      },
      success: function (response) {
        // Handle the response from the server
        console.log(response);
      },
      error: function (xhr, status, error) {
        console.error("Error processing selected divs: " + error);
      },
    });
  });
});
