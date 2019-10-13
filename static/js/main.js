/**
 * Sets copyright date in footer to current year
 */
$( document ).ready(function() {
    let date = new Date();
    $('#copyright-year').text( '2008 - ' + date.getFullYear())

    /**
     * Function to increment value in listing quantity input fields
     * Credit: http://jsfiddle.net/laelitenetwork/puJ6G/
     */
    $('.qtyplus').click(function(e){
        e.preventDefault();
        fieldName = $(this).attr('field');
        var currentVal = parseInt($('input[name='+fieldName+']').val());
        if (!isNaN(currentVal)) {
            $('input[name='+fieldName+']').val(currentVal + 1);
        } else {
            $('input[name='+fieldName+']').val(0);
        }
    });

    /**
     * Function to decrement value in listing quantity input fields
     */
    $(".qtyminus").click(function(e) {
        e.preventDefault();
        fieldName = $(this).attr('field');
        var currentVal = parseInt($('input[name='+fieldName+']').val());
        if (!isNaN(currentVal) && currentVal > 0) {
            $('input[name='+fieldName+']').val(currentVal - 1);
        } else {
            $('input[name='+fieldName+']').val(0);
        }
    });
    /**End credit */

});
