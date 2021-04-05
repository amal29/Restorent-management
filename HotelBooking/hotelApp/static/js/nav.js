function openNav() {
  document.getElementById("myNav").style.width = "100%";
  //   document.getElementById("myNav").style.visibility = "visible";
  console.log("hai opn");
  document.getElementById("btnclose").style.display = "block";

  document.getElementById("btnid").style.display = "none";
}

function closeNav() {
  console.log("hai close");
  document.getElementById("myNav").style.display = "none";
  window.location.reload();
}

// document.getElementById("btnclose").style.display = "none";

$(".js-counter").countTo();
