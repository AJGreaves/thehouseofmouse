<div align="center">
    <img src="https://i.ibb.co/1znc0qC/website-banner-simple-650.png" href="https://thehouseofmouse.herokuapp.com/" target="_blank" rel="noopener" alt="The House of Mouse, Tails of Joy" aria-label="The House of Mouse, Tails of Joy" />
</div>


[![Build Status](https://travis-ci.org/AJGreaves/thehouseofmouse.svg?branch=master)](https://travis-ci.org/AJGreaves/thehouseofmouse)

## Introduction

<div align="center">
    <img src="https://i.ibb.co/F3rct3F/all-products-responsive.png" href="https://thehouseofmouse.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how shop page looks on all screen sizes" aria-label="Image of how shop page looks on all screen sizes" />
</div>


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
    - [Flowcharts](#flowcharts)
    - [PDF](#pdf)

2. [Features](#features)
    - [Existing Features](#existing-features)
        <!-- - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [Activities Page](#activities-page)
        - [Listing Page](#listing-page)
        - [Create Account Page](#create-account-page)
        - [Log In Page](#log-in-page)
        - [Account Settings Page](#account-settings-page)
        - [Account Page](#account-page)
        - [Add new Listing Page](#add-new-listing-page)
        - [Preview Listing Page](#preview-listing-page)
        - [Edit Listing Page](#edit-listing-page)
        - [Contact Page](#contact-page)
        - [404 Page](#404-page)
        - [Permission Denied Page](#permission-denied-page) -->
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Storage Types](#data-storage-types)
    <!-- - [Collections Data Structure](#collections-data-structure)
        - [Users Collection](#users-collection)
        - [Activities Collection](#activities-collection) -->

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

8. [Contact](#contact)

9. [Disclaimer](#disclaimer)

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
- The search icon and shopping cart icons were used in the navigation bar as they are conventionally used in this setting and would be what the user expects to see.
- Yellow cheese icons are used as pointers between breadcrumb links on pages that have worked their way deeper into the hierarchical structure of the website information. These were used to add a little humour to a usually boring aspect of a website.
- On the home page the important facts about The House of Mouse are laid out using icons and simple text for quick assimilation of info (see image above).
- Star icons are used in the testimonials section of the home page, to emphasize the high level of reviews the shop already has on Etsy.
- The Facebook logo icon is included in the footer to lead visitors to The House of Mouse facebook page.


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

![Footer](https://i.ibb.co/KjFjjtP/footer.png)

- The footer features on every page except the cart and checkout pages. It was deliberately not included on those pages as that is the standard for online shops, to remove distractions and links that would take the user away from their cart once they decide to start the checkout process.

- The footer features The House of Mouse tagline at the top, designed to speak to those most likely to enjoy the products for sale. Underneath this is a list of the shops categories, making it easy for the user to find a section they are most interested in. On the right side a list of the most commonly used links. 

- The footer background of grey was chosen to provide some contrast and obvious separation between the footer and the rest of the content on the page. The Headings are displayed in pink with the links all in white. When the user hovers over a link it gently turns pink.

- The footer features the copyright information for The House of Mouse, with the 2nd year date automatically updated with Javascript as each new year begins.

- The footer also includes a link to The House of Mouse active social media channel on Facebook. If/When The House of Mouse reactivates their other social medial channels on twitter/instagram/pinterest then these can be added to the icons in the footer.

### Home Page

![Home page](https://i.ibb.co/SJCXN6H/home-responsive.png)

**Hero slider/carousel**
- The home page hero slider/carousel features 3 slides of promotional images from The House of Mouse. There are 4 images in total used as the last slides image is different for mobile and desktop. The reason for this was that the image gets too cropped when in a wide screen, while looks much better when the dimensions are taller than wide. So this image was saved for mobile screens, and another chosen for wider screens. 

**Introduction and brief pitch**
- Below the hero slider is a concise introduction to The House of Mouse, what it is, who created it and what their mission is.
- A "learn more" button leads a user to the About page where they can read the story behind The House of Mouse. 
- Icons are used to deliver information on the quality and scope of the shop quickly. The information here is deliberately short and to the point, as this page is most likely where a brand new customer would land first and it is important to use this space effectively to help convert sales.

**Shop categories**

![shop categories](https://i.ibb.co/rkRpHq8/sections.png)

- Below the site introduction are a selection of the shop categories, displayed with beautiful product photographs and clear headings. The user can click any of these images to be taken to the relevant sections of the shop.
- On desktop view these sections are displayed with 2 larger images and 4 smaller ones, to give some visual contrast. On smaller screens each section image is the same size, so save space.

**Testimonials carousel**

![Testimonials carousel](https://i.ibb.co/3fLPkQy/reviews.png)

- A carousel of 5 reviews from The House of Mouse customers on Etsy. Each displays a 5 star rating and the review written by a customer. At the bottom of the carousel is a "read more" button that links to The House of Mouse Etsy shop reviews section, where the user can read more of the reviews for this shop.

**Featured listings**

- At the bottom of the home page 4-6 products are selected from the products database from those with `featured = True` in their properties. 4 products are displayed on desktop, and 6 on mobile and tablet size screens.
- A "browse more" button is placed underneath the featured listing inviting the user to go to the shop page.


### Shop Page

![Shop page](https://i.ibb.co/F3rct3F/all-products-responsive.png)



## Features Left to Implement

1. Feature 1

    - password reset by email
    - Send email when new order made
    - staff pages to view all order info needed together for easier shipping process
    - gallery app
    - User favourites
    - newsletter signup

This section will continue to grow as the site is deployed to its own domain and implemented in the real word. New issues and needs will become apparent as the site is used.

# Information Architecture

### Database Choice

more info here

### Data Storage Types

The types of data stored in ... are:
- ObjectId
- String
- Boolean...

### Collections Data Structure

The House of Mouse webshop relies on two database collections:

#### Collection 1

<!-- example table from other project to use as template
 | Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Name | username | text, `maxlength="40"` | string
Email Address | email | email, `maxlength="40"` | string
Password | password | text, `maxlength="15"` | string -->

[Example JSON from collection 1]()

# Technologies Used

### Tools
- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
- [Imgbb](https://imgbb.com) to store all external images for this project.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Photoshop](www.adobe.com/Photoshop) to edit, crop and save images as well as ulitizing the colour picker to ensure color consistency over the entire project.
- [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices.
- [Am I Responsive](https://ami.responsivedesign.is/) to create the images in this readme file of each page displayed on different screen sizes.
<!-- - database info here -->
https://obfuscator.io/

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

Testing information can be found in separate [testing.md](testing.md) file

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
...
<!-- Other details here -->

### Instructions
1. Save a copy of the github repository located at xxx by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone xxx
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```
...
<!-- 
6. In your local IDE create a file called `.flaskenv`.

7. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `familyHub`, with 2 collections called `users` and `activities`. You will find example json structures for these collections in the [schemas](familyhubapp/data/schemas) folder.

8. You can now run the application with the command
```
python app.py
```

9. You can visit the website at `https://thehouseofmouse.herokuapp.com/` -->

## Heroku Deployment

To deploy The House of Mouse webshop to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:
...
<!-- 
| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed. -->

# Credits

## Content

## Media
### Animations

### Images

## Code

- Box shadow codes were taken from [Material Design Box Shadows](https://codepen.io/sdthornton/pen/wBZdXq).

## Acknowledgements

Special thanks to my mentor [Simen Daehlin](https://github.com/Eventyret) for his never-ending patience and willingness to teach me not only what code works, but what is expected of my websites and code in industry.

# Contact
To contact me feel free to email

 `gilhespy (dot) anna (at) gmail (dot) com`

## Disclaimer
The content of this website is educational purposes only.
