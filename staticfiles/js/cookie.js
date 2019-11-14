/**
 * Code credit to fellow student Sean Murphy,
 * created to demonstrate how to get csrf token from cookies
 */

/**
 * Retrieves csrftoken from document for use with fetch/ajax requests.
 * @param {string} name 
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// variable to use for fetch / ajax requests
let csrftoken = getCookie('csrftoken');