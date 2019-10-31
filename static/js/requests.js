$(document).ready(function () {
    /**
     * When user adds more of the same item to their cart,
     * sends request to database to check how many in stock. 
     * If number requested is more than number in stock, 
     * responds with modal informing user and resets quantity
     * in cart to max number in stock.
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


    /**
     * When user increases or decreases the number of items
     * in their cart, send request to database to check number of 
     * item in stock. If user requests more than is in stock,
     * launch modal to inform user and set value of input to max number available.
     */
    if (document.querySelector('#confirmCartForm')) {
        $('.numberinput').change(function () {
            const value = this.value
            const data = {
                idChangedInput: this.id,
                value: value,
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
                    if (response.max_num < value) {
                        alert_too_many_cart_page(
                            response.max_num,
                            response.title
                        );
                        this.value = response.max_num;
                    };
                    $('#subtotal-js').text(response.total)

                })
                .catch(err => console.log('ERROR: ' + err))

        })

        /**
         * Function starts when user clicks a X icon in cart to delete an item from 
         * their basket. Function checks id of icon (incremented in loop over cart items),
         * sets quantity of item from session variable to 0, and reloads the page.
         */
        $('.delete-icon').click(function () {
            const data = {
                orderItemId: this.id.slice(17),
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
                    $('#subtotal-js').text(response.total);
                    location.reload(); 
                })
                .catch(err => console.log('ERROR: ' + err))

        });
    };



    /**
     * settings for SweetAlert2 popup on successfully adding item to cart. 
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

    /**
     * settings for SweetAlert2 popup on individual listing page, if user tries to add
     * more of a product to their cart than there is in stock. 
     * @param {string} title 
     */
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

    /**
     * settings for SweetAlert2 popup on cart page, if user tries to increase number
     * in their order above what is in stock.
     * @param {string} title 
     */
    function alert_too_many_cart_page(num, title) {
        Swal.fire({
            type: 'info',
            title: `Sorry!`,
            text: `There are only ${num} of this ${title} in stock.`,
        })
    }
});