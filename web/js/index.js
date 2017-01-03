function showPage(n) {
    id = 'page' + n;
    hidePages();
    document.getElementById(id).style.display = 'inline';
    menuHamberger();
}
function hidePages() {
    document.getElementById('page1').style.display = 'none';
    document.getElementById('page2').style.display = 'none';
    document.getElementById('page3').style.display = 'none';
    document.getElementById('page4').style.display = 'none';
    document.getElementById('page5').style.display = 'none';
}
/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function menuHamberger() {
    var x = document.getElementById("topnav");
    if (x.className === "topnav") {
	x.className += " responsive";
    } else {
	x.className = "topnav";
    }
}
