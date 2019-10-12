/**
 * Sets copyright date in footer to current year
 */
$( document ).ready(function() {
    let date = new Date();
    $('#copyright-year').text( '2008 - ' + date.getFullYear())
});
