// // All code in this file provided by https://stripe.com/docs/payments/cards/collecting/web

let stripe = Stripe('pk_test_HBIRLDOMqTFcuRZWxR4BjsNf00a93m4id3');
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