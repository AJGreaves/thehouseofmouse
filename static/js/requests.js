
/**
 * request function written by fellow student Sean Murphy to 
 * demonstrate how to send data to back end with csrf token
 */
const addToCart = document.querySelector('#listing-quantity-form');
addToCart.onsubmit = (event) => {
    console.log(event.target)
    event.preventDefault();
    const form = event.target;

    fetch('.', {
        method: 'POST',
        headers: new Headers({
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                    'X-Requested-With': 'XMLHttpRequest',
                }),
        body: JSON.stringify({quantity: form.listingId.value}),
        credentials: 'same-origin',
    })
        .then(res => res.text())
        .then(response => {
            console.log(response)
        })
        .catch(err => console.log('ERROR: ' + err))

};
