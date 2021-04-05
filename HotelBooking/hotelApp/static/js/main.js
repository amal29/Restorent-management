$(document).on("click", ".booknow", function () {
  var BookId = this.dataset.book;
  console.log(BookId);

  $.ajax({
    url: "book",
    dataType: "json",
    data: {
      BookId: BookId,
    },
    success: function (data) {
      console.log(data);
      $("#exampleModal .modal-content").html(data.html_form);
    },
  });

  $("#exampleModal").on("submit", ".create-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("data-url"),
      data: {
        d1: $("#myText").val(),
        d2: $("#myText2").val(),
        imgdata: $("#img_id").attr("src"),

        BookId: BookId,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      type: form.attr("method"),
      dataType: "json",
      success: function (data) {
        if (data.submited) {
          console.log(data);

          $("#exampleModal").modal("hide");
          alert("Room is Booked Successfully");

        } else {
          alert("Room is Full");
        }
      },
    });
    location.reload();

    return false;
  });
});

//MYroom///

$(document).on("click", ".room", function () {
  console.log("amalroom");

  $.ajax({
    url: "room",
    dataType: "json",
    data: {},
    success: function (data) {
      console.log(data);
      $("#myroom .modal-content").html(data.html_form);
    },
  });

  $(document).on("click", ".dbtn", function () {
    var roomid = this.dataset.room;

    console.log(roomid);
    $.ajax({
      url: "droom",
      dataType: "json",
      type: "post",
      data: {
        roomid: roomid,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        console.log(data);
        $("#myroom .modal-content").html(data.html_form);
      },
    });
  });
});

function ourroom() {
  jQuery("html").animate({
    scrollTop: jQuery("#room_id").offset().top,
  });
}

function mygallery() {
  jQuery("html").animate({
    scrollTop: jQuery("#gallery").offset().top,
  });
}

function prebook() {
  alert("Please Login Your Account");
}
