function showPage(n) {
    id = 'page' + n;
    hidePages();
    document.getElementById(id).style.display = 'inline';
}
function hidePages() {
    document.getElementById('page1').style.display = 'none';
    document.getElementById('page2').style.display = 'none';
    document.getElementById('page3').style.display = 'none';
    document.getElementById('page4').style.display = 'none';
    document.getElementById('page5').style.display = 'none';
}
