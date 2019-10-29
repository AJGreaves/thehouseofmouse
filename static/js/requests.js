$(document).ready(function () {
    /**
     * request function written by fellow student Sean Murphy to 
     * demonstrate how to send data to back end with csrf token
     */
    if (document.querySelector('#listing-quantity-form')) {

        const addToCart = document.querySelector('#listing-quantity-form');
        addToCart.onsubmit = (event) => {
            event.preventDefault();
            const form = event.target;

            const data = {
                listingId: form.listingId.value,
                quantity: form.quantity.value
            }

            fetch('.', {
                    method: 'POST',
                    headers: new Headers({
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                        'X-Requested-With': 'XMLHttpRequest',
                    }),
                    body: JSON.stringify(data),
                    credentials: 'same-origin',
                })
                .then(res => res.json())
                .then(response => {
                    if (response.too_many) {
                        alert_too_many_listing_page(response.title);
                    } else {
                        alert_success(response.title);
                    }

                })
                .catch(err => console.log('ERROR: ' + err))

        };
    };

    if (document.querySelector('#confirmCartForm')) {
        $('.numberinput').change(function () {
            const value = this.value
            const data = {
                idChangedInput: this.id,
            };

            fetch('.', {
                    method: 'POST',
                    headers: new Headers({
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                        'X-Requested-With': 'XMLHttpRequest',
                    }),
                    body: JSON.stringify(data),
                    credentials: 'same-origin'
                })
                .then(res => res.json())
                .then(response => {
                    if(response.max_num < value) {
                        alert_too_many_cart_page(
                            response.max_num, 
                            response.title
                        );
                        this.value = response.max_num;
                    };

                })
                .catch(err => console.log('ERROR: ' + err))
        })
    };

    /**
     * settings for SweetAlert2 popup. 
     * @param {string} title 
     */
    function alert_success(title) {
        message = `${title} has been added to your cart.`
        Swal.fire({
            type: 'success',
            title: message,
            text: "Go to checkout?",
            showCloseButton: true,
            confirmButtonColor: '#47b7f8'
        }).then((result) => {
            if (result.value) {
                window.location.replace("/cart/");
            }
        })
    }

    function alert_too_many_listing_page(title) {
        Swal.fire({
            type: 'warning',
            title: `Oops! The total number of ${title} in your cart was more than we have in stock`,
            text: `Your cart has been adjusted and now contains the maximum number available. Go to checkout?`,
            showCloseButton: true,
            confirmButtonColor: '#47b7f8'
        }).then((result) => {
            if (result.value) {
                window.location.replace("/cart/");
            }
        })
    }

    function alert_too_many_cart_page(num, title) {
        Swal.fire({
            type: 'info',
            title: `Sorry!`,
            text: `There are only ${num} of this ${title} in stock.`,
        })
    }
});