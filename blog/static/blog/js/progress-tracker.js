$('body').progressTracker({
    horNumbering: false,
    horTitles: true,
    horMobileOnly: true,
    horTracker: true,
});

window.document.onscroll = function() {ScrollIndicator()};

function ScrollIndicator() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";
}
 
