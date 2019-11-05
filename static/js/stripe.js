// // All code in this file provided by https://stripe.com/docs/payments/cards/collecting/web

const s_pub = returnStripePublishableKey();

let stripe = Stripe(s_pub);
let elements = stripe.elements();

$('#submit-payment-btn').click(function() {
    startCheckout();
})

async function startCheckout() {
    const {error} = await stripe.redirectToCheckout({
        sessionId: s_id
    })

    if (error) {
        alert('Something went wrong with the payment, please try again.');
    }
}