$(document).ready(function () {
    const contactForm = document.querySelector('#contact-form');

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const data = {
            service_id: "gmail",
            template_id: "thehouseofmouse",
            user_id: ejs,
            template_params: {
                "name": contactForm.name.value,
                "email": contactForm.email.value,
                "message": contactForm.message.value,
            }
        };

        $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json'
        }).done(function () {
            contact_form_success(contactForm.name.value);
            $('input').val('');
            $('textarea').val('');
            
        }).fail(function (error) {
            contact_form_error();
            console.log('Oops... ' + JSON.stringify(error));
        });
    });

    function contact_form_success(name) {
        let message = `Thank you ${name}.`;
        Swal.fire({
            type: 'success',
            title: message,
            text: "Your message has been sent successfully!",
            confirmButtonText: 'Ok',
            confirmButtonColor: '#47b7f8'
        }).then((result) => {
            if (result.value) {
                window.location.replace("/");
            }
        });
    }

    function contact_form_error() {
        let message = `Oops!`;
        Swal.fire({
            type: 'warning',
            title: message,
            text: "Something went wrong with our contact form, please try again",
            showConfirmButton: false,
            timer: 2000,
        })
    }
})