# The House of Mouse - Testing details

[Main README.md file](README.md)

[View website on Heroku]()

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation services](#validation-services)
    - [Jasmine](#jasmine)
    - [Python Testing](#python-testing)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)

## Automated Testing

### Validation Services
The following validation services and linter were used to check the validity of the website code.

- [W3C Markup Validation]( https://validator.w3.org/) was used to validate HTML.

    - **Important note** On the pages that use [Gijgo](https://gijgo.com/) date and time pickers (Add New Listing Page and Edit Listing Page), the W3c validator throws many errors to do with the html code that is inserted by Gijo.js. I have double-checked that I am using the most up to date version of Gijgo. These errors are due to code I have not written myself, and that is added when the page is rendered via the Gijgo JavaScript file. 

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

- [JSHint](https://jshint.com/) was used to validate JavaScript.

    <!-- - To save on loading times and to keep my JavaScript code organized I chose to break up the JS into several separate files. 
    - When running JSHint, the errors `undefined variable` and `unused variable` appear when one file either creates or uses a function that is utilized or created in another file. As validates one JS file at a time, it is not aware of the other files. 
    - To double-check that no errors occur with the entire files loaded I pasted in all the JavaScript code into JSHint and then it ran with no errors.  -->

- [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) was used to validate Python.

### Jasmine

- [Jasmine-Jquery CDN](https://github.com/velesin/jasmine-jquery) has been imported into the jasmine testing to allow for jQuery within the JavaScript functions.

The files for jasmine testing Family Hub can be found here:
- HTML page to run jasmine tests from: [jasmine-testing.html](testing/jasmine/jasmine-testing.html)
- JavaScript specifications (tests): [familyhubSpec.js](testing/jasmine/spec/familyHubSpec.js)
- The House of Mouse JavaScript functions to be tested are in the [js directory](static/js)
    - [common.js](static/js/common.js) // replace this

#### How to run Jasmine tests

Before going further please make sure you have already cloned this project from the [The House of Mouse GitHub repository](https://github.com/AJGreaves/thehouseofmouse) 
by following the steps in the [README.md](readme.md#how-to-run-this-project-locally) under "How to run this project locally" and that you have the entire project running on your own IDE.

To run the Jasmine tests: 
1. Open [jasmine-testing.html](testing/jasmine/jasmine-testing.html).
2. Run the html file and view it in your browser to see the test results. 

#### How to create Jasmine tests

To create Jasmine tests: 
1. Open the [thehouseofmouseSpec.js](testing/jasmine/spec/thehouseofmouse.js) file.
2. Write your own tests using the jasmine 3.1 framework.
3. Save [thehouseofmouseSpec.js](testing/jasmine/spec/thehouseofmouseSpec.js), and then run/refresh [jasmine-testing.html](testing/jasmine/jasmine-testing.html).

### Python Testing

#### How to run Python tests

### A note about TDD

This project did not utilize Test Driven Development for Jasmine or Python while it is a student project. The reason for this was that I am still very new to both JavaScript and Python and found it impossible to write tests for languages I did not understand well. 

The automated tests for this project were created after the vast majority of the project was already complete, once I had a firmer grasp of how my functions were working and what their expected output was. Now that I have a better understanding of how automated tests work, I intend to attempt TDD with my next project.

## User Stories Testing

## Manual Testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

#### Elements on every page

1. Navbar 

2. Footer


#### Home Page

1. Hero Image
    - Confirm that hero image loads at a reasonable speed, and that the image is sharp and clear. 
    - Confirm the heading for the page is easy to read.

### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile and tablet specific elements on my Samsung phone and tablet, in both the firefox browser and samsung internet browser.

Responsive design waw also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar 
- Open the website on mobile, confirm that the navbar is collapsed into a burger icon
- click the burger icon, confirm that the navbar list appears are expected.

### Bugs discovered: 
#### Solved bugs

1. **On running the python server, large errors appeared in terminal**
    - Any time a page was loaded, the terminal filled with around 100 lines of errors. This turned out to be a bug with Python 3.7.3 [See bug report on bugs.python.org](https://bugs.python.org/issue27682)
    - Bug was partially resolved by upgrading my version of python to python 3.7.5, although this threw new errors at me.
    - Bug finally fixed by replacing my `python manage.py runserver` command with `python manage.py runserver 8000` (with thanks to Chris Zielinski, Code Institue Mentor for this solution)

2. **Duplicate items added to OrderItems database**
    - As I was using a nested loop to compare the items in my sessions storage cart to the items in the database Order, I was ending up with duplicate items when more than 1 item was already in the database.
    - After multiple different attempts to fix the problem the solution was pretty simple: if the Order already existed I deleted all the OrderItems from the database and rebuilt them from the session variable instead.
```python
order = Order.objects.filter(customer=request.user, paid=False).first()
checkout_cart = request.session['cart']

# if new order, create instance of order
if not order:
    order = Order.objects.create(customer=request.user)

# if unpaid order exists in database already:
else:
    # get items in session storage cart
    session_cart = checkout_cart['orderItems']

    # get items currently in Order
    items_in_order = OrderItem.objects.filter(order=order)

    # delete all orders in the list
    for orderitem in items_in_order:
        orderitem.delete()

    # loop through all cart items and create new instances of OrderItem for them
    for item in session_cart:
        _id = int(item['listingId'])
        quantity = int(item['quantity'])

        # filter out items in session storage that have had their quantities reduced to 0
        if quantity > 0:
            product = Product.objects.filter(id=_id).first()
            order_item = OrderItem(order=order, product=product, quantity=quantity)
            order_item.save()
```

5. **Django code for search vectors not working with sqlite3 database**
    - The more refined search functions from `django.contrib.postgres.search`, such as `SearchQuery, SearchRank, SearchVector` would not work with my local sqlite3 database.
    - Temporarily solved this by using this simpler search code:

    ```python
    from django.db.models import Q
    results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query))
    ```

    - Once my site was deployed, I connected to the postgres database and then replaced the above code with the more robust and accurate django postgres search code.

    ```python
    from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

    vector = SearchVector('title', weight='A') + SearchVector('description', weight='B') + SearchVector('tags', weight='C')
    query = SearchQuery(query)
    results = Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.1).order_by('rank')
    ```


4. **VScode unable to access postgreSQL database for testing**
    - Due to the free Hobby-dev postgres package selected when setting up the heroku database, I was not able to set the permissions necessary to alow Django to create a test database when running `manage.py test`. 
    - To fix this I reverted to accessing my sqlite3 database on my local machine for testing, and checked Travis regularly to check my tests written locally were passing when tested against the production database too.

#### Unsolved bugs

1. **On running the python server, large errors appear in terminal**
    - Any time a page is loaded, the terminal filled with around 100 lines of errors, although the page does still load. This appears to be an existing bug with Python 3 [See bug report on bugs.python.org](https://bugs.python.org/issue27682).


## Further testing: 
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.
2. FamilyHub viewed on all devices and orientations available in Chrome DevTools, as well at a local tech store.
