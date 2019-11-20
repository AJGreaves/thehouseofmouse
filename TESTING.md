# The House of Mouse - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://thehouseofmouse.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation services](#validation-services)
    - [Jasmine](#jasmine)
    - [Python Testing](#python-testing)
    - [Coverage](#coverage)
    - [Travis](#travis)
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

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML. 

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

- [JSHint](https://jshint.com/) was used to validate JavaScript.

    - To save on loading times and to keep my JavaScript code organized I chose to break up the JS into several separate files. 
    - When running JSHint, the errors `undefined variable` and `unused variable` appear when one file either creates or uses a function that is utilized or created in another file. As validates one JS file at a time, it is not aware of the other files. 
    - To double-check that no errors occur with the entire files loaded I pasted in all the JavaScript code into JSHint and then it ran with no errors. 

- [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Pylint-django](https://pypi.org/project/pylint-django/) was used to validate Python.

If you wish to run any of these tests for yourself, befre going further please make sure you have already cloned this project from the [The House of Mouse GitHub repository](https://github.com/AJGreaves/thehouseofmouse) 
by following the steps in the [README.md](readme.md#how-to-run-this-project-locally) under "How to run this project locally" and that you have the entire project running on your own IDE.

### Jasmine

- [Jasmine-Jquery CDN](https://github.com/velesin/jasmine-jquery) has been imported into the jasmine testing to allow for jQuery within the JavaScript functions.

The files for jasmine testing The House of Mouse can be found here:
- HTML page to run jasmine tests from: [jasmine-testing.html](testing/jasmine/jasmine-testing.html)
- JavaScript specifications (tests): [familyhubSpec.js](testing/jasmine/spec/thehouseofmouseSpec.js)
- The House of Mouse JavaScript functions to be tested are in the [js directory](static/js)
    - [common.js](static/js/main.js)

#### How to run Jasmine tests

To run the Jasmine tests: 
1. Open [jasmine-testing.html](testing/jasmine/jasmine-testing.html).
2. Run the html file and view it in your browser to see the test results. 

#### How to create Jasmine tests

To create Jasmine tests: 
1. Open the [thehouseofmouseSpec.js](testing/jasmine/spec/thehouseofmouseSpec.js) file.
2. Write your own tests using the jasmine 3.1 framework.
3. Save [thehouseofmouseSpec.js](testing/jasmine/spec/thehouseofmouseSpec.js), and then run/refresh [jasmine-testing.html](testing/jasmine/jasmine-testing.html).

### Python Testing

#### How to run Python tests

To run the existing Python tests:
1. Activate your virtual environment.
2. In the terminal enter the following command:
```
python manage.py test
```
3. If you wish to run the tests within a specific app only you can specify with: 
```
python manage.py test <app name here>
```
4. The test results will be shown within the terminal.

_NOTE: The `python` part of these commands assumes you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_


### A note about TDD

This project did not utilize Test Driven Development. The reason for this was that I was learning how Django works and functions and found it impossible to write tests for methods and classes that I did not understand well as I went along. 

The automated tests for this project were created after the vast majority of the project was already complete, once I had a firmer grasp of how my code was working and what its expected output was. Now that I have a better understanding of how automated tests work, I intend to attempt TDD with my next project.

- coverage - command: coverage html, then open and run index.html file in the htmlcov directory created.
- travis

### Coverage

[Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/) was used to provide feedback during testing to check that enough of my code had been tested.

#### How to run coverage

1. Activate your virtual environment.
2. In the terminal enter the following command:
```
coverage html
```
3. Open the newly created `htmlcov` directory in the root of your project folder. 
4. Open the `index.html` file inside it.
5. Run the file in the browser to see the output.

### Travis

- [Travis](https://travis-ci.org/) was used throughout the unit testing of this project to provide continuous integration with the deployed site. The [Travis Documentation](https://docs.travis-ci.com/) provides all the info needed to set it up.
- I set the heroku deployment settings for this project to only allow deployment when the travis had passed the latest push to the master branch.

## User Stories Testing

The following section goes through the user stories identified in the [Ux section of README.md](README.md#UX) to check that the site meets those needs.

**As a visitor to The House of Mouse website I expect/want/need:**

1. **To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.**
    - Arrangement of site elements such as navbar, footer, icons, carousels, products lists, search, contact, FAQs and forms conform to expected placement. Breadcrumbs are provided on pages where the user has moved deeper into the hierarchical data structure of the website to make it easier for the user to tell where they are and how they can return to previous pages they were on.
    - The key pages of the site can be accessed from both the navigation bar and the footer, which can be found on all pages of the site (except the checkout pages).

1. **The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.**
    - As the user moves through the site from the surface layers like the home page, to more detailed pages like an individual listing page, the information needed at each stage is displayed at the appropriate level. 
    - At the main shop results page only product images, titles and prices are displayed so that all the information can be scanned quickly by a user to find what they are most interested in. 
    - Icons and images are used to help the user digest information quickly.
    - Common frequently asked question are put into a separate page, so that they can be found easily when needed.

1. **The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.**
    - Some points for this already covered in previous user story details.
    - Once the user moves to a listing detail page the user can access more detailed information on that product. 
    - Shop list pages can be sorted by category, price high to low or price low to high.
    - The search page allows the user to run a text search through all products titles, descriptions and tags to find what they are looking for.

1. **The site to be easily navigable from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.**
    - A lot of attention was paid to mobile-first design throughout the project, from wireframes to completion. 
    - All elements have been given a responsive design, so nothing to too squashed, squeezed or hard to read on any screen size a user might be using.
    - The use of the site has been extensively tested on desktop, tablet and phone size screens as well as all screen sizes available to simulate in Chrome Developer Tools.

1. **To learn more about the shop owner and their process, so that I can be assured I am buying from a small handmade business.** 
    - A short but compelling About page is included in the site. With enough information to satisfy a users curiosity without overloading them with more than they need.

1. **To be able to read reviews of this shop from previous customers, to build trust in my purchase.**
    - The home page featured 5 testimonials from past customers, displayed in a carousel. A button in this section leads the user to the Etsy feedback page where 100s of other reviews for this shop can be read.

1. **For all information and images to be laid out in a clear and easy to understand way, on whatever size screen I am viewing the website on.**
    - Attention has been paid to ensuring product images are clean and professional, never squashed or squeezed and that the users operation of the site pages work on all devices. Text is never too large or too small, buttons are always large enough to click with a finger easily on touch screen devices.

1. **Plenty of high quality images of the products for sale, so I have a clear idea of what I am buying and can see the quality of the products up close.**
    - Each product listing can hold up to 6 images, so the user can see the product, packaging and scale in detail. Image files have been optimized to keep the file size low while not sacrificing the professional image quality.

1. **To be able to easily find out all the information I need to make an informed purchase. I expect information about materials, measurements, safety and packaging to be available on every listing page.**
    - Information about product materials, measurements, safety and package are available on every listing page under the listing description.

1. **To be informed if I try to order more items than are available in stock.**
    - Whenever a user adds an item to their cart or adjusts the quantity in their cart the current stock level for that item is checked from its database entry. A modal will alert the user if they attempt to add more to their cart than is available in stock, and their cart will be updated to reflect the maximum number available.

1. **For recorded stock levels to be accurate, so there are no delays in receiving my order.**
    - Each listing detail quantity selection will only go up to the maximum number in stock. 
    - Whenever an item is purchased, the stock level for it in the database is updated.
    - The shop owner can access and update stock levels from the admin panel.

1. **A text search function so that I can quickly narrow down my search when looking for something specific.**
    - A text search is available on the search page. It searches through the products titles, description and tags to find and rank the results for the user.

1. **A clear terms and conditions and privacy policy.**
    - Terms and conditions, and privacy policy pages are included in the site and linked to in the footer of each page.

1. **There to be a frequently asked questions page for any further questions I might have about my order.**
    - A FAQs page is provided and linked to in the navigation and footer.

1. **To be able to see a summary of my order on every page of the checkout process.**
    - The order summary is indeed on every page of the checkout process, provided on the right side of the screen on large screens, and in a dropdown button on mobile.

1. **That once I am logged in I can access my account details and update them if I need to.** 
    - The Account page gives the logged in user the ability to update their username, email address, first and last names. 
    - At the moment the user cannot change their password - see [Features for Future Releases](README.md#features-for-future-releases) for more details.

1. **To be able to find information on my past orders and how to cancel an order.** 
    - The Account page provides a list of all the users previous purchases, with full details of their order, date it was placed, products, quantities and total amount paid. 
    - A link is provided in each order summary for the user to contact the seller to cancel their order.
    - Order summary's also include information on if the relevant order has been shipped yet.

1. **To be able to connect to the businesses social media channels and/or newsletter, to keep up to date with new listings on the site.**
    - The footer contains a link to the Mailchimp newsletter signup form for this shop.
    - The active social media channel for this shop is on Facebook, so an icon and link to that is provided in the footer. When/if this shop becomes active on social media again their other social media platforms can easily be added in the same place.

1. **To be able to easily get in contact with the shop owner via a contact form.**
    - The contact page is easily located from the navigation bar and footer.
    - The contact page is linked to in various relevant places throughout the site to encourage users to get in contact if they need to.
    - The contact form provides an easy on site way for the user to send an email to the shop owner.
    - The email sent to the shop owner includes all the needed info to reply directly to the sender.

1. **Feedback from the website I am using when I interact with it, I expect pop ups and modals to inform me when my forms have been completed and sent correctly. Or to let me know when an error has ocurred and what to do next.**
    - HTTP responses provide feedback to the user if there is a problem with their input values in forms.
    - Beautiful animated popups appear to inform the user when their forms are completed, contact message is sent or when items are added to their cart.
    - Error messages are also returned to the user when there is a problem with the site's functionality.

## Manual Testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

#### Elements on every page

1. Navbar 
    - Clicked each link in the navbar to confirm that it leads to the correct page.
    - Confirm that when logged out the options "Register" and "Log in" are visible and that "Account" and "Log out" are not.
    - Log into the site, confirm that options "Account" and "Log out" are visible and that "Register" and "Log in" are not.
    - Click the "Shop" link in the navbar, confirm that all sections of the shop are listed in the dropdown menu.
    - Add an item to the users cart, confirm that the counter appears over the shopping cart icon with the correct number of items displays.
    - Add more than 10 items to the cart, confirm that the counter shows `9+`.
    - Delete all items from the users cart, confirm that the counter is no longer visible in the navbar.

2. Footer
    - Click subscribe button, confirmed it opens a new tab and takes the user to the correct subscription page on the MailChimp website.
    - Hover over links in the footer, confirm the color change animation works as expected.
    - Click all links in the footer, confirm that they take the user to the relevant pages within the site.
    - Click the facebook icon, confirm that it opens a new tab and takes the user to The House of Mouse facebook page.
    - Check date of copyright information, confirm year displayed matches the current year.

#### Home Page

1. Hero Slider
    - Click slider buttons, confirm that they work as expected.
    - Adjust width of browser window, confirm image is always cropped in an attractive way.

2. Call to action buttons
    - Hover over all buttons, confirm the color change and shadow on hover appear as expected.
    - Click all buttons, confirm they take the user to the correct links and open new tabs when links go away from the website.

3. Shop section images
    - Hover over each section image, confirm shadow size increases and image looks as it if is being lifted up on the page.
    - Confirm all titles laid over on images can be easily read.

4. Testimonials carousel
    - Click carousel buttons, confirm that they work as expected.
    - Check each slide to be sure the elements fit within the slider.
    - Confirm all text can be easily read.

5. Featured listings
    - Confirm that on desktop 4 featured listings are visible in one row.
    - Confirm that on tablet 6 featured listings are visible over two rows.
    - Reload the page, confirm that a new random selection of featured listings are shown.
    - Click each listing picture, confirm that it takes the user to the relevant listing detail page.

#### Shop Page

1. Breadcrumbs
    - Click breadcrumb links, confirm they work and go to the correct locations.

2. Shop section buttons
    - Hover over section buttons, confirm the hover effects work as expected.
    - Click all section buttons, confirm they work and take the user to the correct pages.

3. Sorting options
    - Select the different sorting options from the menu one by one, confirm that the products are sorted in the orders selected.

4. Product cards
    - Hover over product cards, confirm the hover effect works as expected.
    - Confirm that the photos, images and prices displayed are correct.
    - Click multiple products, confirm that the user is taken to the correct product listing pages.
    - Confirm that one of each product is displayed in total. 
    - Check that there are no duplicates or missing products.

5. Pagination
    - Click all pagination links, confirm that they work as desired.

#### Search Page

1. Breadcrumbs
    - Click breadcrumb links, confirm they work and go to the correct locations.

2. Search bar
    - Load search page, confirm that the search bar is visible and no product listing results are shown.
    - Enter a search word that applies to many listings. 
        - Confirm that the listing returned match the search term.
        - Confirm that the results are paginated and that the pagination works correctly.
    - Enter a search word that does not apply to any listings. Confirm that the message "There are currently no listings that match this search" is displayed when hitting enter.

3. Footer on search page
    - Confirm that footer stays stuck to the bottom of the screen even when there are no listings to fill up the space.

#### Listing Page

1. Listing breadcrumbs
    - Check that breadcrumbs show the relevant category of the product listing in them.
    - Click all breadcrumb links, confirm that they take the user to the correct pages.

2. Listing details
    - Confirm that the listing title, price, and description match those in the database for the product.

3. Listing photographs
    - Click the thumbnails provided for extra images of the product. Confirm that the large photograph is updated to reflect the thumbnails clicked.
    - Confirm that the standard photograph of the product packaging, and the one provided to show scale are visible with the other listing photographs.

4. Listing information
    - Confirm that all information on measurements, materials, safety and customisations can be found on the listing detail page under the description. 
    - Click the contact page link in the listing info, confirm it takes the user to the contact page.

5. More like this
    - Check that the listings featured in the "more like this" section are from the same category as the listing detail currently open.
    - Check that the current listing is excluded from the selection of products shown.
    - Click the products in this section, confirm that their links and hover effects work as expected.
    - Click the "browse more" button, confirm it takes the user to the correct category section of the shop.

6. Quantity selection
    - Click the quantity selection. Confirm that the highest number available to select matches the number in stock of this product.

7. Add to cart button
    - Click the "add to cart" button. Confirm that the applicable modal is launched, stating the name of the product added to the cart, and that the cart counter in the navigation bar is updated to reflect the new quantity.
    - Confirm that the modal provides two buttons to the user: to go to cart or to continue shopping. Click both to confirm they operate as expected.
    - Add more to the cart from the same product, making the total go over the max number in stock. Confirm that the modal alerting the user to too many of the product in their cart is launch. Confirm that the quantity in the cart is reset to the max number in stock.

#### About Page

- Go to account page, confirm that the title and subheading displays as expected. 
- Check that the photograph is on the left side of the screen and the text on the right. 
- Check that the proportions of the page are as expected.
- Click the "visit shop" call to action button, confirm it takes the user to the main shop page.

#### FAQs Page

- Go to FAQs page. Confirm that each question is in the main heading font and pink, to make it easy for users to scan the questions to find the ones relevant to their needs.
- Check that the questions are clear and the answers given are sufficient.
- Click the "contact" and "subscribe" links provided on this page, confirm they take the user to the contact page.

#### Contact Page

- Go to the contact page. Confirm that the contact form is laid out as expected.
- Confirm that for a logged in user the email address field has already been populated. 
- Confirm that for a user who is not logged in the email address field is blank.
- Try to send the form with no fields filled in, confirm that the user is alerted to fill in the required fields.
- Try to enter a non-email address into the email field, confirm that the user is alerted to fill in an email address.
- Send a complete form, confirm that the message is sent to my email address with all the information included.

#### Register Page

- Try to go to the register url when already logged in, confirm that the user is redirected to the home page.
- Log out then go to the register page again. Confirm that the register form is displayed as expected.
- Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
- Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
- Go into devtools, change the `type` attribute on the email form to `text`, attempt to send the form. confirm that the Django validation catches the error and tells the user to enter an email address.
- Fill in the form with two different passwords, confirm the error is caught again and the user is informed of their mistake.
- Fill in the registration for correctly, confirm that the user is automatically directed to the login page, and the message "Your account has been created `<username>`. You can now log in." is displayed above the login page. 

#### Login Page

- Reload the login page, confirm that the message for a new account is not visible.
- Attempt to log in with a username not in the database, confirm the relevant error message is shown.
- Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
- Log in with a correct username and password, confirm that the user is logged in and that they are redirected to their cart page.
- Try to return to the login page url when already logged in, confirm that the user is redirected to the cart page.

#### Account Page

- Go to the account page of a newly created user. Confirm that te profile info form is populated with the users username and email address.
- Confirm that the first name and last name fields are also available.
- Fill in the form with a non-email address, confirm that the applicable error is shown to the user
- Fill in the form correctly, confirm that the "Your account info has been updated." message is shown to the user and that the reloaded form is now populated with the new data.
- Confirm that a user with no previous orders has the "no orders to show" text in the Orders section.
- Make 2 separate orders on the website. 
- Return to the account page, confirm that the orders are displayed in the Orders section of the account page. With the top order being the most recent and open to show the full details. Confirm that all orders after it in the list are closed accordions, but that can be opened with a click.
- Confirm that all data in the orders on the account page is accurate.
- Go into the admin panel, mark one of the orders as shipped. Confirm that the information to the user in their account page is updated to show that the order selected has been shipped.

#### Log Out Page

- Add a new product to the users cart. Click the "log out" link in the navigation bar. Confirm that the user is logged out and their cart has been cleared.
- Click the "Log in again" link on this page, confirm that the user is taken back to the login page.
- Confirm that the footer stays stuck to the bottom of the screen even when there is not enough content on the page to push it down.

#### Cart Page

- Go to the cart page when not logged in to the site, confirm that the user is taken to the login page to sign in.
- Log in and go to the cart page with nothing in the cart. Confirm that the message "Your cart is empty!" is shown and the call to action button "Let's go shopping" is provided.
- Click the button and confirm it takes the user to the main shop page.
- Add items to the cart and return to the cart page, confirm that all items in the cart are displayed correctly, with the correct amounts requested by the user.
- Adjust the quantity field, confirm that the shopping cart subtotal is updated to reflect the change.
- Adjust the quantity field up higher than the number of that item in stock. Confirm that a modal alerts the user to the maximum number available and adjust the cart to reflect that amount.
- Click the `x` delete button on a listing, confirm that the cart page is reloaded with that item removed from the cart.
- Delete all items from the cart, confirm that the cart page is reloaded to reflect the empty cart.

#### Checkout Pages

##### Info Page

##### Shipping Page

##### Payment Page

##### Confirmation Page

#### Terms and Conditions Page

#### Privacy Policy Page


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

5. **Duplicate listings showing up in All-Products view**
    - This was initially caused due to trying to sort results from the database by a boolean value (featured), but this turned out to be a known nofix issue with django. 
    - First I attempted to fix this by ordering by random, but the same problem continued.
    - Eventually I decided to order by id, so that the most recently added products to the database would be displayed first, which suits a shops "all products" view much better than a random collection that changes each time the page is loaded.

#### Unsolved bugs

1. **Sorting category results with pagination**



## Further testing: 
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.
2. FamilyHub viewed on all devices and orientations available in Chrome DevTools, as well at a local tech store.
