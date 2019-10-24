$(document).ready(function () {

    const addToCartForm = document.querySelector('#listing-quantity-form');

    addToCartForm.addEventListener('submit', (event) => {
        // prevents default behaviour of submit button to refresh page
        event.preventDefault();

        const listingId = document.querySelector('#listing-id').value;
        const quantity = document.querySelector('#quantity').value;
        const csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').attr('value')

        const data = {
            listingId: listingId,
            quantity: quantity,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        };
        console.log(data)

        $.ajax('/cart/', {
                type: 'POST',
                data: JSON.stringify(data),
                contentType: 'application/json'
            }).done(function () {
                console.log("success")
            }).fail(function (error) {
                console.log('Oops... ' + JSON.stringify(error));
            });
    });

})