<div align="center">
    <img src="https://i.ibb.co/1znc0qC/website-banner-simple-650.png" href="https://thehouseofmouse.herokuapp.com/" target="_blank" rel="noopener" alt="The House of Mouse, Tails of Joy" aria-label="The House of Mouse, Tails of Joy" />
</div>


[![Build Status](https://travis-ci.org/AJGreaves/thehouseofmouse.svg?branch=master)](https://travis-ci.org/AJGreaves/thehouseofmouse)

## Introduction

![Home page](https://i.ibb.co/SJCXN6H/home-responsive.png)

[The House of Mouse webshop](https://thehouseofmouse.herokuapp.com/) was created by Anna Greaves. 

Introduction to purpose of project here.

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [Shop Page](#ashop-page)
        - [Search Page](#search-page)
        - [Listing Detail Page](#listing-detail-page)
        - [About Page](#about-page)
        - [Frequently Asked Questions Page](#frequently-asked-questions-page)
        - [Contact Page](#contact-page)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Account Page](#account-page)
        - [Log out Page](#log-out-page)
        - [Cart Page](#cart-page)
        - [Checkout](#checkout)
        - [Terms and Conditions / Privacy Policy pages](#terms-and-conditions-privacy-policy-pages)
    - [Features for Future Releases](#features-for-future-releases)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Models](#data-models)
        - [User](#user)
        - [Products App Model](#products-app-model)
        - [Cart App Models](#cart-app-models)

4. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

5. [Testing](#testing)
    - See separate [TESTING.md](TESTING.md) file.

6. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

8. [Contact](#contact)

----

# UX

## Goals

### Visitor Goals

The central target audience for The House of Mouse are:
- People who collect mouse ornaments or cute animal ornaments.
- Fans of Harry Potter, Star Wars or Doctor Who.
- People who value buying handmade.
- People searching for unique handmade gifts.
- People in touch with their inner child and who find joy in adorable art.

User goals are:
- Find a new mouse for my collection.
- Find a gift for my husband-who-has-everything.
- Enjoy browsing all the cute designs and stories.
- Be able to navigate the shop easily, find what I need and make a safe and secure purchase.
- Buy from a trustworthy online shop.

The House of Mouse online shop is a great way to meet these needs because:
- The website has been carefully designed with the years of experience this developer has had in running The House of Mouse through online marketplaces like Etsy.
- The navigation fits with conventions of well laid out online shops, products are professionally photographed and easy to find. All the information that the buyer needs is available and easy to find.
- The House of Mouse website can be searched by category, similar items and using text search, making it easy for customers to find specific things or enjoy browsing categories that interest them.

### Business Goals

The Goals of The House of Mouse business are:
- Provide a professional online shop that helps the user to feel safe that they are buying from a trustworthy source. 
- Build brand awareness by including all the branding photographs, colours, fonts and logo associated with The House of Mouse brand.
- Connect to fans of the shop through The House of Mouse social media channels.
- Build The House of Mouse newsletter subscriptions.
- Keep track of sales data to inform future product choices.
- Make sales of products easy for buyers to increase sales conversion.

## User Stories

As a visitor to The House of Mouse website I expect/want/need:

1. To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it. 

1. The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.

1. The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.

1. The site to be easily navigable from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.

1. To learn more about the shop owner and their process, so that I can be assured I am buying from a small handmade business. 

1. To be able to read reviews of this shop from previous customers, to build trust in my purchase.

1. For all information and images to be laid out in a clear and easy to understand way, on whatever size screen I am viewing the website on.

1. A completely custom mouse designed and created for me either for my own collection or as a gift. 

1. Plenty of high quality images of the products for sale, so I have a clear idea of what I am buying and can see the quality of the products up close.

1. To be able to easily find out all the information I need to make an informed purchase. I expect information about materials, measurements, safety and packaging to be available on every listing page.

1. To be informed if I try to order more items than are available in stock.

1. For recorded stock levels to be accurate, so there are no delays in receiving my order.

1. A text search function so that I can quickly narrow down my search when looking for something specific.

1. A clear terms and conditions and privacy policy.

1. There to be a frequently asked questions page for any further questions I might have about my order.

1. To be able to see a summary of my order on every page of the checkout process.

1. That once I am logged in I can access my account details and update them if I need to. 

1. To be able to find information on my past orders and how to cancel an order. 

1. To be able to connect to the businesses social media channels and/or newsletter, to keep up to date with new listings on the site. 

1. To be able to easily get in contact with the shop owner via a contact form.

1. Feedback from the website I am using when I interact with it, I expect pop ups and modals to inform me when my forms have been completed and sent correctly. Or to let me know when an error has ocurred and what to do next.

## Design Choices

The House of Mouse website has an overall child like, joyful feel, with emphasis on the high quality, artisan handmade feel of the products on sale. The following design choices were made with this in mind:

### Fonts
<div align="center">
    <img src="https://i.ibb.co/zP4PPRh/Clipboard01.jpg" alt="Fonts used on The House of Mouse website" aria-label="Fonts used on The House of Mouse website" />
</div>

- The primary font 'Lato' was chosen for the main text of the site because of it clear readability, clean style and complementary contrast with the secondary font. This font also looks good in uppercase with a little extra letter spacing, and so could serve nicely as a sub heading as well.

- The secondary font 'Emilys Candy' was chosen for the main headings because it is whimsical, childlike and the curled ends to some of the letters look like mouse tails.

### Icons
<div align="center">
    <img src="https://i.ibb.co/Cb3k6vM/Clipboard01.jpg" alt="Icons used on The House of Mouse Home Page" aria-label="Icons used on The House of Mouse Home Page" />
</div>

- In order to keep the site uncluttered only a few icons were utilized. 
- The **search** icon and **shopping cart** icons were used in the navigation bar as they are conventionally used in this setting and would be what the user expects to see.
- Yellow **cheese icons** are used as pointers between breadcrumb links on pages that have worked their way deeper into the hierarchical structure of the website information. These were used to add a little humour to a usually boring aspect of a website.
- On the home page the important facts about The House of Mouse are laid out using icons and simple text for quick assimilation of info (see image above).
- **Star icons** are used in the testimonials section of the home page, to emphasize the high level of reviews the shop already has on Etsy.
- The **Facebook logo** icon is included in the footer to lead visitors to The House of Mouse facebook page.

### Colours
<div align="center">
    <img src="https://i.ibb.co/kBR2r7K/THOM-Brand-colors.jpg" alt="The House of Mouse Brand Colours" aria-label="The House of Mouse Brand colours" />
</div>

- light pink: #FFE4E6
- pink: #FFBABE
- dark grey: #373737
- light grey: #E5E5E5
- light blue: #7ccfff

- The brand colours for this project were chosen because the two shades of pink and two shades of grey are taken from the felt mice ears and standard body color. This helps to pull the colours of the site together with the product photographs. 

The blue was chosen to provide a highlighting contrast for links, prices and important buttons for the user such as "add to cart" and "checkout now".

### Styling

- Subtle box shadowing and curved was applied to elements that needed a little extra emphasis and style. For example on product images, cart summary and form wrappers. 
- In cases when the an is clickable, for example product images or call to action buttons the shadow size is increased and animated when the user hovers over that element, this was done to make the area more tempting to click.
- Curved corner styling was chosen for its friendly feel, and as it is a common stylistic choice of bootstrap it blends well with styles used from that library on this project.

## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project. 

- [Home](https://i.ibb.co/wgpZ6Ch/Home-Page.png)
- [About](https://i.ibb.co/zVCP7K9/About-page.png)
- [FAQs](https://i.ibb.co/BGK7WCy/FAQs-page.png)
- [Account](https://i.ibb.co/ScwR6Zz/account-page.png)
- [Shop/Search Results](https://i.ibb.co/NpMFjpH/search-results-page.png)
- [Catagories](https://i.ibb.co/8NKbWTn/browse-categories-page.png)
- [Listing](https://i.ibb.co/GvLQ1Z1/listing-page.png)
- [Cart](https://i.ibb.co/Sm4g5w0/Cart-page.png)
- [Checkout - Info](https://i.ibb.co/5jW9tVD/info-page.png)
- [Checkout - Shipping](https://i.ibb.co/FbL5VWq/shipping-page.png)
- [Checkout - Payment](https://i.ibb.co/TgnPT7b/payment-page.png)
- [Checkout - Confirmed](https://i.ibb.co/QHg2bTg/payment-confirmed-page.png)

# Features
 
## Existing Features

### Elements on every page

#### Navbar:

<div align="center">
    <img src="https://i.ibb.co/K7fFpC8/navbar-desktop.png" alt="The House of Mouse Navbar on desktop devices" aria-label="The House of Mouse Navbar on desktop devices" />
</div>

- The navbar features on every page except the checkout pages. It was deliberately not included on those pages as that is the standard for online shops, to remove distractions and links that would take the user away from their cart once they decide to start the checkout process.

- The navigation bar features The House of Mouse logo on the far left, which links to the home page of the site.

- **In desktop view** on the left side of the navbar is a list of the key website pages: Home, Shop, About and FAQs. The Shop link is a dropdown menu which lists out the sections of shop products.

- On the right side of the navbar are the links to contact page, search page and shopping cart.

- A user who is currently logged out will also see options to register or log into the website.

- A user who is logged in will see options to view their account page or log out.

- The shopping cart icon is located to the far right of the navigation bar. Once a user has added at least one item to their cart a blue circle will appear with the total number of items in their cart displayed within it. If the total number is 10 or more then the circle will display "9+" to save from extending the text over the size of the blue circle indicator. 

    - The indicator was chosen to mimic notification icons users are used to seeing in online shops and social media etc.

    - The blue color was chosen because it contrasts well with the rest of the sites colors and draws the eye.

    - The shopping cart counter works even for a user who is not logged in. This is because all the information about which products the user has added to their cart is stored in their session data. This makes it possible for a new user to add things to their cart before being asked to log in or register. 

- When a user is on a page listed in the navbar the text for that page is highlighted with a deeper color, and `<span class="sr-only">(current)</span>` is added to the relevant html for screen readers to tell which page the user is on.


<div align="center">
    <img src="https://i.ibb.co/c2mT77b/navbar-mobile.png" alt="The House of Mouse Navbar on mobile devices" aria-label="The House of Mouse Navbar on mobile devices" />
</div>

- **In tablet and mobile view** the logo remains in the left side of the navigation bar, where users would expect it to be. 
- The shopping cart icon is displayed in the middle of the navigation bar, and the burger icon to display the full navigation menu is on the far left, again because that is where a user would expect to find it.

#### Footer

![Footer](https://i.ibb.co/n8k7swY/footer.png)

- The footer features on every page except the cart and checkout pages. It was deliberately not included on those pages as that is the standard for online shops, to remove distractions and links that would take the user away from their cart once they decide to start the checkout process.

- The footer features The House of Mouse tagline at the top, designed to speak to those most likely to enjoy the products for sale. Under this is a link to The House of Mouse newsletter signup form, hosted by Mailchimp.

- Underneath the newsletter signup button is a list of the shops categories, making it easy for the user to find a section they are most interested in. On the right side a list of the most commonly used links. 

- The footer background of grey was chosen to provide some contrast and obvious separation between the footer and the rest of the content on the page. The Headings are displayed in pink with the links all in white. When the user hovers over a link it gently turns pink.

- The footer features the copyright information for The House of Mouse, with the 2nd year date automatically updated with Javascript as each new year begins.

- The footer also includes a link to The House of Mouse active social media channel on Facebook. If/When The House of Mouse reactivates their other social medial channels on twitter/instagram/pinterest then these can be added to the icons in the footer.

### Home Page

**Hero slider/carousel**
- The home page hero slider/carousel features 3 slides of promotional images from The House of Mouse. There are 4 images in total used as the last slides image is different for mobile and desktop. The reason for this was that the image gets too cropped when in a wide screen, while looks much better when the dimensions are taller than wide. So this image was saved for mobile screens, and another chosen for wider screens. 

**Introduction and brief pitch**
- Below the hero slider is a concise introduction to The House of Mouse, what it is, who created it and what their mission is.
- A "learn more" button leads a user to the About page where they can read the story behind The House of Mouse. 
- Icons are used to deliver information on the quality and scope of the shop quickly. The information here is deliberately short and to the point, as this page is most likely where a brand new customer would land first and it is important to use this space effectively to help convert sales.

**Shop categories**

![Shop categories](https://i.ibb.co/rkRpHq8/sections.png)

- Below the site introduction are a selection of the shop categories, displayed with beautiful product photographs and clear headings. The user can click any of these images to be taken to the relevant sections of the shop.
- On desktop view these sections are displayed with 2 larger images and 4 smaller ones, to give some visual contrast. On smaller screens each section image is the same size, so save space.

**Testimonials carousel**

![Testimonials carousel](https://i.ibb.co/3fLPkQy/reviews.png)

- A carousel of 5 reviews from The House of Mouse customers on Etsy. Each displays a 5 star rating and the review written by a customer. At the bottom of the carousel is a "read more" button that links to The House of Mouse Etsy shop reviews section, where the user can read more of the reviews for this shop.

**Featured listings**

![Featured listings](https://i.ibb.co/TLZS3Gw/featured.png)

- At the bottom of the home page 4-6 products are selected from the products database from those with `featured = True` in their properties. 4 products are displayed on desktop, and 6 on mobile and tablet size screens.
- A "browse more" button is placed underneath the featured listing inviting the user to go to the shop page.


### Shop Page

**Category buttons**
- The main shop page features a collection of buttons leading to each section of the shop. These buttons are not visible on mobile view to save space, as they can also be accessed from the navbar.

**Sort results**
- The main shop page includes the option to sort its results by "featured", "price: high to low" and "price: low to high".

**Products list**
- Products in the shop are displayed as thumbnail images with their title and price displayed underneath each photograph.
- Shop results are paginated by 12 items at a time. This number was chosen because 12 can be evenly divided by 3 and 4 making is possible to display results 4 to a row on desktop, 3 to a row on tablet and 1 on top of each other on mobile screens.
- Each product in the list has a link to it;s respective product listing with more photographs and information.

**Pagination** 
- Pagination buttons are provided depending on the number of results returned from the database with options for "First", "previous", "next" and "last" as well as the page number the user is currently on.

### Category pages
- The category pages are built from the same template as the main shop page and displays the same buttons and sorting options.
- Pagination is not currently available for shop categories, as there is an unsolved bug with trying to then sort these results. As the number of products in a single category is never very large I opted to leave fixing this issue for a future release.

### Search Page
- The search page is built from the same template as the main shop page and shop categories pages. With the one addition of the search bar where users can enter a text search.
- On loading the search page there are no products displayed. Once the user has entered a text search the results are displayed below the search bar and paginated if more than 12 results are returned from the database.
- If no results for a text search are returned from the database then the text 
"There are currently no listings that match this search" provides feedback to the user.

### Listing Detail Page

![Listing detail page on different screen sizes](https://i.ibb.co/mS3dqQc/listing-responsive.png)

**Product images**
-  Each product detail page features at least 3 professional quality photographs of the product from different angles. 
- Sometimes a group photo is included as well to show off more mice from the same collection. 
- A photograph of the packaging is also included, to give users a clear idea of how their order will appear when it arrives. 
- Finally a photograph of one of the mice being held, to give a clear indication of scale for those users who may not read the measurements further down the listing.
- One main large image is presented at a time, with thumbnails along the side or bottom of the main image (depending on screen size) that are clickable. Every time a thumbnail image is clicked, the larger image is replaced with the one from the thumbnail. This gives the user the ability to fully inspect the product while not taking up too much space on the page.

**Product details**
- The product **title, price and description** are all clearly visible on the product listing page.
- Under the product description is standard information that is applicable to all orders in the shop. 
- A dropdown menu allows the user to select the quantity of a product they wish to purchase. The maximum number available for selection is in direct relation to the number currently in stock. 
- An "Add to cart" button is displayed right under the quantity selection.

**Notification modals**
- When a user adds an item to their cart, an animated modal appears to inform them that their item has been successfully added. They are then given the option to continue shopping or view their cart.
- If a user already has 2 of an item in their cart, and tries to add another 2 when there are only 3 available, a modal will appear alerting the user to the maximum number of this item available for them to buy. Their cart totals will be updated to reflect the maximum they can buy at this time.

**More like this**
- A collection of 4-6 listings from the same category as the detailed listing above, as well as a "browse more" button underneath it. These were included to keep the user engaged in the shop and looking at other products that might appeal to them.

### About page

- The About page features a photograph of the artist behind The House of Mouse and text about her story. To provide the user with more information and a way to connect with the creator of the handmade products.
- At the end a call to action button at the bottom of this page invites the user to visit the shop.

### Frequently Asked Questions Page

- The FAQs page highlights the questions in pink with heading font, making it easier for the user to scan the questions and find the relevant one.
- The answers to the questions are clearly given under each one.
- At the bottom of the page the user is encouraged to contact the shop owner via the contact page if they have further questions that were not already answered above.

### Contact Page

- The contact page contains a form for the user to fill in to send the shop owner an email.
- Name, email address and message are all required fields so that the shop owner receives all the information she needs to respond.
- If the user is logged in then their email address will already be populated in the email field.
- When the user clicks "send" the email is processed and sent via emailjs to The House of Mouse email address.

### Register Page

![Register page on different screen sizes](https://i.ibb.co/TvR9Rn8/register-responsive.png)

- A user who is not logged in can create a new account using the register page. The page on this form includes a username (which must be unique), email address, password and password conformation fields. 
- Information about what characters are accepted by these fields is displayed with the form.
- If a user who is already logged in tries to access this page, they are redirected to the home page.

### Login Page
- The login page features a standard login form asking for username and password.
- Validation for this form is handled in the back end and relevant feedback is sent to the user when they sign in.

### Account Page

![Account page on different screen sizes](https://i.ibb.co/27GrNtP/account-responsive.png)

- The users account page can only be accessed by a logged in user. Any user not logged in who tries to access this page will be redirected to the login page.
- The account page is split into two sections:
    - **Profile Info**, where the user can update their username and email address, and where they can add or update their first and last name.
    - **My Orders**, where a user can see a summary of all their previous orders. request a cancellation, and view the order status. 

### Log out page
- Any user who clicks on "Log out" from the navigation bar is automatically logged out and their session data cleared. They are taken to a page that informs them that they have been logged out and provides a link to log back in if they wish.

### Cart page

- The shopping cart page features a summary of all the items the user has added to their cart.
- Each list item includes a picture of the item, the item title and price.
- A cross symbol at the top right of each list item gives the user the ability to delete that item from their cart.
- A quantity field is displayed with each cart item, giving the user the ability to adjust the quantity in their cart. Any time a quantity is adjusted the subtotal displayed is updated to reflect the change.
- Information is provided for the user to tell them that tax is already included in the price they saw, and that the shipping cost will be calculated during checkout.

#### Checkout

![Checkout page on different screen sizes](https://i.ibb.co/vV2r6NL/checkout-responsive.png)

- Each checkout page features an order summary, which lists all the items in the users cart, title, price and quantity. A link is provided at the top of this for the user to return to the cart page to make changes to the order.
    - On mobile devices this order summary is part of a closed accordian, the top part of which displays the total cost. It can be clicked to open the full order details. This was done to save space on a smaller screen.
    - On tablet devices and larger screens, the order summary is displayed in full on the right side of the screen on all checkout pages.

- The checkout process is broken up into 4 stages. The reason for this was to break up the process into small steps as is common in online shops.

    1. **Info**
        - Here the user is asked to provide the shipping name and address to send their order to. They are also asked to select the country their order will go to, this is used to calculate the shipping price.
        - Not every country in the world is currently included on the list of shipping destinations. This was done in part to save time in making multiple entries into the database, and also because after running this shop for over 10 years the owner knows which destinations her products are usually shipped to. 
        - For the unlikely case that someone wishes to ship to a country not in the list, a link at the bottom of the form says "My country is not on the list?" and opens a modal encouraging the user to request their country be added to the shipping destinations.
        - The "Continue to shipping" button leads the user to the shipping page.

    2. **Shipping**
        - The shipping page includes all the information that the user has provided so far: Their contact email address (taken from when they created their account), the shipping name and address, and their order summary. A link is provided where the shipping address is displayed so that the user can return to the info page to update it.
        - This page provides the user with shipping options to choose from. At this point there is only one shipping option available, however this page and functionality have been left in so that other options such as expedited shipping may be added with a future release.
        - As a shipping method is automatically selected, the order summary now reflects the total cost including shipping. 
        - The "Continue to payment" button leads the user to the payment page hosted by Stripe.

    3. **Payment**
        - As stripe now offer a pre-built checkout in their latest version 3, I opted to use this as my payment page, as it hands over much of the back end coding needed for making payment to Stripe.
        - The Stripe payment page includes a summary of what the user is buying, and fields to enter credit card information.
        - All the validation and messages to the user on this page are handled by stripe.
        - On clicking the "Pay" button and on successful completion of payment, the user is redirected to the order confirmation page back on The House of Mouse website.

    4. **Confirmation of order**
        - The order confirmation page gives the customer all the information they need going forward. The shipping address and expected shipping time are provided. As well as links to the users account page and the contact page should they need to get in touch with the shop owner.
        - Finally the user is invited to return to the shop with a call to action button at the bottom of the page.

#### Terms and Conditions / Privacy Policy pages

- Every trustworthy online shop provides the legal documentation expected by the user on their site. Although these documents are a legal requirement of any online shop, including them also helps users to feel they can trust the outlet.


## Features for Future Releases

1. **Password reset by email.**
    - I already looked into this, but it required changing settings in my private gmail account to less secure ones. Which is not something I am willing to do at this moment. When/if this site is deployed to it's own domain and is being used as a fully functioning online store, then I will invest in a separate gmail account specifically for it and get this feature set up.
2. **Sending an email to customer when their new order has been placed.**
    - This feature also required the gmail settings mentioned above, and is one that would be included if/when the site is properly launched.
3. **Build staff pages to view all order info needed together for easier shipping process.**
    - Giving staff the ability to view all order information in one place, rather than having to visit the Stripe dashboard or admin panel to see the orders. Functionality for this page might include:
        - Ability to print out pre-formatted shipping labels
        - Update order as "shipped" in the database and add tracking information so that the customer is updated with this information at the same time.
        - Integration with DHL to follow tracking on packages sent.
        - Ability to handle cancellations and refunds.
4. **Coupons and discount codes.**
    - Checkout pages to include a field for customers to enter discount codes or coupons to adjust their final payment cost.
5. **Gallery app.**
    - A gallery of previously made custom orders. Many fans of The House of Mouse enjoy seeing the many weird and wonderful creations and artistic flair of the owner. A gallery of mice not for sale, would be enjoyed by many of these fans, and would inspire those looking for a custom order.
6. **User favourites.**
    - Another feature designed for The House of Mouse fan, who would return to the site many times and have a "dream collection" of mice they would like to own one day. 
    - This feature was originally included in the wireframes for this project, but unfortunately had to be clipped from the current release due to time constraints.
7. **Embedded Mailchimp newsletter signup form in footer.**
    - At the moment the footer contains a button to lead the user to the newsletter signup form, currently hosted by Mailchimp. 
    - For ease of use for the user, and to get rid of more clicks needed to sign up, I would like to add the signup form fully embedded into my own website in the footer.
8. **Additional payment methods.**
    - The current free version of Stripe checkout only allows for customers to pay via credit card. However this is not a popular form of payment in The Netherlands, with many more people preferring to pay via PayPal, bank transfer or iDeal. Stripe does offer these payment methods, and once this site is deployed for actual use these will be added to the options for customers to choose from.

This section will continue to grow as the site is deployed to its own domain and implemented in the real word. New issues and needs will become apparent as the site is used.

# Information Architecture

### Database Choice

- As a framework Django works with SQL databases. During development on my local machine I worked with the standard **sqlite3** database installed with Django.
- On deployment, the SQL database provided by Heroku is a **PostgreSQL** database. 

### Data Models

#### User

The User model utilized for this project is the standard one provided by `django.contrib.auth.models`

#### Products app model

Within the `products` app, the **Product** model holds all the data needed for the products in the shop.

**Product model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Title | title | max_length=100 | CharField
Shop category | category | choices=CATEGORY_CHOICES | CharField
Image 1 | product_image1 |  | ImageField
Image 2 | product_image2 | blank=True, null=True | ImageField
Image 3 | product_image3 | blank=True, null=True | ImageField
Image 4 | product_image4 | blank=True, null=True | ImageField
Image 5 | product_image5 | blank=True, null=True | ImageField
Description | description |  | TextField
Price | price | max_digits=6, decimal_places=2 | DecimalField
Tags | tags | max_length=300 | CharField
Stock qty | num_in_stock | validators=[MaxValueValidator(100)] | PositiveSmallIntegerField
Featured | featured | default=False | BooleanField

- Category choices are defined within the Product model.
- The Product model uses Pillow to store all image files in an AWS S3 bucket.

#### Cart app models

Within the `cart` app, the **ShippingDestination**, **Order** and **OrderItem** models hold the data needed for users to create and pay for their orders.

**ShippingDestination model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Country | country | max_length=50 | CharField
Shipping Price | shipping_price | max_digits=6, decimal_places=2 | DecimalField
Shipping Time | shipping_time | max_length=150, default="1 to 2 weeks" | CharField

- This table is used within the Django admin panel for shop staff to add all the countries the shop will ship to, the cost of that shipping and an estimated shipping time. 
- This data is then used to calculate the total cost of an order depending on the shipping destination selected, as well as provide the customer with the estimated shipping time when placing their order.

**Order model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
User | customer | on_delete=models.PROTECT | ForeignKey to User
Full Name | full_name | max_length=150 | CharField
Address line 1 | address_line_1 | max_length=150 | CharField
Address line 2 | address_line_2 | max_length=150, blank=True | CharField
Town / City | town_or_city | max_length=150 | CharField
County | county | max_length=150, blank=True | CharField
Postcode | postcode | max_length=10 | CharField
Country | country | on_delete=models.PROTECT | ForeignKey to ShippingDestination
Date ordered | date_ordered | default=datetime.date.today | DateField
Paid | paid | default=False | BooleanField
Shipped | shipped | default=False | BooleanField

- An instance of the Order model is created before any OrderItems, as the latter relies on the former for a ForeignKey.

**OrderItem model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Order | order | on_delete=models.CASCADE | ForeignKey to Order
Product | product | on_delete=models.PROTECT | ForeignKey to Product
Quantity | quantity | | PositiveSmallIntegerField

- An instance of OrderItem is created for each unique product in the users cart. It links to the already existing Order for this user, the relevant product and the quantity the user wishes to buy.

# Technologies Used

### Tools
- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [Travis](https://travis-ci.org/) for continuous integration.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/) to measure code coverage of python unittests.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
- [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) to allows the web app to serve its own static files.
- [Obfuscator](https://obfuscator.io/) to obscure emailjs user key from plain text code.
- [Imgbb](https://imgbb.com) to store external images for this project that were not entered into the database.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Photoshop](www.adobe.com/Photoshop) to edit, crop and save images as well as utilizing the colour picker to ensure color consistency over the entire project.
- [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices.
- Heroku for deployment
- [SweetAlert2](https://sweetalert2.github.io/) for beautiful responsive replacement to javascript popup boxes.

### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Jasmine](https://jasmine.github.io/) to run automated tests on JavaScript and jQuery code.
- [Jasmine-jQuery](https://github.com/velesin/jasmine-jquery) to make it possible to test jQuery code using Jasmine.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.


# Testing 

Testing information can be found in separate [TESTING.md](TESTING.md) file

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
- [Stripe](https://dashboard.stripe.com/register)
- [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [emailjs](https://www.emailjs.com/)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.

### Instructions
1. Save a copy of the github repository located at https://github.com/AJGreaves/thehouseofmouse by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/AJGreaves/thehouseofmouse
```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```  
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

6. Install all required modules with the command 
```
pip -r requirements.txt.
```

7. Set up the following environment variables within your IDE. 

- If using VSCode, locate the `settings.json` file within the .vscode directory and add your environment variables as below. Do not forget to restart your machine to activate your environment variables or your code will not be able to see them: 

```json
"terminal.integrated.env.windows": {
    "HOSTNAME": "<enter hostname here>",
    "DEV": "1",
    "SECRET_KEY": "<enter key here>",
    "STRIPE_PUBLISHABLE": "<enter key here>",
    "STRIPE_SECRET": "<enter key here>",
    "EMAILJS_USER_ID": "<enter key here>",
    "STRIPE_SUCCESS_URL": "<enter url here>",
    "STRIPE_CANCEL_URL": "<enter url here>",
    "AWS_ACCESS_KEY_ID": "<enter key here>",
    "AWS_SECRET_ACCESS_KEY": "<enter key here>",
    "AWS_STORAGE_BUCKET_NAME": "<enter bucket name here>",
}
```

- If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the following format: 
```
HOSTNAME="<enter key here>"
```
- `HOSTNAME` should be the local address for the site when running within your own IDE.
- `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.

9. Migrate the admin panel models to create your database template with the terminal command
```
python manage.py migrate
```

10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
```
python manage.py createsuperuser
```

11. You can now run the program locally with the following command: 
```
python manage.py runserver
```

12. Once the program is running, go to the local link provided and add `/admin` to the end of the ur. Here log in with your superuser account and create instances of ShippingDestination and Product within the new database.

13. Once instances of these items exist in your database your local site will run as expected.


## Heroku Deployment

To deploy The House of Mouse webshop to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
AWS_STORAGE_BUCKET_NAME | `<your AWS S3 bucket name>`
DATABASE_URL | `<your postgres database url>`
EMAILJS_USER_ID | `<your secret key>`
HOSTNAME | `<your heroku app hostname>`
SECRET_KEY | `<your secret key>`
STRIPE_CANCEL_URL | `<link to all-products page in your app>`
STRIPE_PUBLISHABLE | `<your secret key>`
STRIPE_SECRET | `<your secret key>`
STRIPE_SUCCESS_URL | `<link to checkout/confirm page in your app>`

8. From the command line of your local IDE:
    - Enter the heroku postres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

11. From the link provided add `/admin` to the end of the url, log in with your superuser account and create instances of ShippingDestination and Product within the new database.

12. Once instances of these items exist in your database your heroku site will run as expected.

# Credits

## Content
- Terms and conditions template provided by [Shopify](https://en.shopify.nl/tools/policy-generator/terms-and-conditions)
- Example privacy policy provided by [Cleverbox](https://www.cleverbox.co.uk/example-privacy-policy/)
- All other text, including but not limited to website introduction, product descriptions and marketing copy was written and provided with permission by The House of Mouse shop owner.

### Images
- All product photography was taken and provided with permission by The House of Mouse shop owner.
- Photographs of the shop owner were taken by [Rudi Wells Photography](https://www.rudiwells.com/)

## Code

- The following youtube video series provided much explanation about the use and operation of Django2
    - [Python Django Web Framework by freeCodeCamp.org](https://www.youtube.com/watch?v=F5mRW0jo-U4)
    - [Python Django Tutorial by Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)


## Acknowledgements

Special thanks to my mentor [Simen Daehlin](https://github.com/Eventyret) for his time, expertise and friendship through my entire journey through the CodeInstitute full stack web development course.

With thanks also to my many coding friends who have tested, helped troubleshoot and debug, saved me from mild panic, supported and encouraged me along the way: Jo, Sean, Tim, Anthony, Robin, John, John, Chris, Anthony, Matt, Bim, Shane, Sipo and Ailsa.

# Contact
To contact me feel free to email

 `gilhespy (dot) anna (at) gmail (dot) com`
