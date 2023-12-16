// This is your test publishable API key.
const stripe = Stripe("pk_test_51OFgV1HNBgyzsvZ1qRisfwGEnGbMjo5DsdHGL3DgaVFZ8DISR7jUmuR3NwJxg9vjymJpdcejvHXAzvpVggxgHhHI00X7FF4L5H");
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);


initialize();

// Create a Checkout Session as soon as the page loads
async function initialize() {
  const response = await fetch("/create-checkout-session", {
    method: "POST",

  });
  alert("i'm here")
  const { clientSecret } = await response.json();

  const checkout = await stripe.initEmbeddedCheckout({
    clientSecret,
  });

  // Mount Checkout
  checkout.mount('#checkout');
}