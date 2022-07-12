# **Legato Music**

[View the live site here](https://paulmodaley-legatomusic.herokuapp.com/)

This website was built to fulfill the requirements of the Code Institute Milestone 5 Project. It is an e-commerce site designed for a fictional music retailer, Legato Music. 

Using the principles of UX design, this fully-responsive website was developed using HTML, CSS, Bootstrap, JavaScript, Python, Django. It uses an SQL database through PostgreSQL to provide backend functionality, including enabling store administrators to amend inventory, edit item details, and more.

Stripe provides some of the functionality for the website's payment system which is currently limited to accept test card details only. The full details of Stripe's test cards can be found [here](https://stripe.com/docs/testing#cards).

![Final project image home page](https://github.com/PaulModaley/guitarstore/blob/c329a72ba89a40bde0b6b226b937a09a0b512029/media/responsive.png)

## **Contents**

[User Experience (UX)](#user-experience-ux)

* [User Stories](#user-stories)

[Design](#design)
* [Colour Scheme](#colour-scheme)
* [Typography](#typography)
* [Imagery](#imagery)
* [Wireframes](#wireframes)
* [Features](#features)
* [Future Features](#future-features)

[Information Architecture](#information-architecture)
* [Database Design](#database-design)

[Technologies Used](#technologies-used)
* [Languages Used](#languages-used)
* [Site Design](#site-design)
* [Hosting](#hosting)
* [Databases Platform and Cloud Storage](#databases-platform-and-cloud-storage)
* [Frameworks and Libraries](#frameworks-and-libraries)
* [Other Technologies](#other-technologies)
* [Testing](#testing)

[Deployment](#deployment)
* [Requirements for Deployment](#requirements-for-deployment)
* [Initial Deployment](#initial-deployment)
* [How to Fork it](#how-to-fork-it)
* [Making a Local Clone](#making-a-local-clone)

[Testing and Project Barrier Solutions](#testing-and-project-barrier-solutions)

[Credits](#credits)
* [Code](#code)
* [Content](#content)
* [Media](#media)
* [Acknowledgements](#acknowledgements)

---

## **User Experience (UX)**

### User Stories

#### Viewing and Navigation
* As a shopper:
    * I wish to easily navigate the site through a system of menus so that I can easily find pages.
    * I wish to receive visual confirmations of actions having been completed.
    * I wish to view all the products within the store so that I can select ones I wish to purchase.
    * I wish to search for a specific product or product category so that I may find an item to purchase.
    * I wish to view full product information so that I can see the the price, description, product rating and product image of all the products available.
    * I wish to easily see my cart total so that I can see how much I am going to spend.

#### Registration and User Accounts
* As a shopper:
    * I wish to create an account so that I can save my details for speedier purchases and view order information/history.
    * I wish to be able to login or logout so that I can access and manage my profile and personal information.
    * I wish to be able to reset my password so that I can regain access to my account in the event that a password is lost/forgotten.

#### Reviews and Wishlist
* As a registered shopper:
    * I wish to be able to review products so that I may voice my opinions about products to other website visitors.
    * I wish to be able to save products to a wishlist so that I can view those products at a later date.
    * I wish to be able to remove products from my wishlist so that my I can change my mind about my preferred items. 

#### Sorting and Searching
* As a shopper:
    * I wish to be able to sort the list of available products by price or rating so that I can shop according to my budget or according to buyer ratings.
    * I wish to be able to sort a category of products by price or rating so that I can shop a category according to my budget or according to buyer ratings.
    * I wish to be able to search for a specific product so that I can quickly find items.
    * I wish to be able to view a list of search results so that I can see if the product I want is available to purchase.

#### Purchasing and Checkout
* As a shopper:
    * I wish to buy products through the website as a guest so that I can checkout without having to create an account.
    * I wish to modify the contents of my shopping cart so that I can adjust the shopping cart prior to submitting payment.
    * I wish to be able to enter my payment information to complete the checkout process. 
    * I wish to be able to provide payment and personal information securely so that I can purchase items with peace of mind regarding the security of my details.
    * I wish to view an order summary before completing my purchase so that I can avoid ordering the wrong item(s) and/or over/under spending.

#### Admin and Store Management
* As a Store Owner:
    * I wish to be able to add a new product to the inventory so that I can offer new products to website visitors.
    * I wish to be able to edit any product on the website so that I can ensure the information is accurate and iup-to-date.
    * I wish to be able to delete products from the inventory so that I can ensure that customers can only view what is currently available.
    
    
    
    #### Admin and Store Management
    
    GitHub's project boards were utilised throughout the development process to track progress against the above user stories by shifting user stories from 'to do' to 'in progress' and eventually to 'done' as applicable. At the end of the development process, all the user stories were marked 'done' and placed in the appropriate column.

[Back to Top](#legato-music)

---

## **Design**

### Colour Scheme
* The website uses a selection of colours from this [automatically generated palette](https://www.schemecolor.com/music-store.php). Two of the colours from this palette were chosen to complement one another while also providing sufficient contrast between backgrounds and text elements. ![music-store-by-schemecolor](https://github.com/PaulModaley/guitarstore/blob/8f95bb01c61ae0772f5911bf7c8dfbe371c3bd2b/media/music-store-colours.png)
* In addition to #711F31 and #E0AF3A, white (#ffff) is also employed on the website to complement and contrast the two main colours.

### Typography

* The website uses the [Comfortaa](https://fonts.google.com/specimen/Comfortaa#about) font from Google Fonts. It was selected for its clarity and flexibility at different sizes while also being free for personal and commercial use.

### Imagery

* The iconography on the site came from Font Awesome. They were selected to provide representations of certain website functions to the user. 
* The hero image of the site, which came from Getty Images, aims to invoke feelings about the thrill of live music and musical creativity. Extensive editing of the image was undertaken using Photoshop and Canva to remove the original background, recolour the image, and place it upon a custom background which was created in Canva. 
* The product imagery was taken from various sources, including from Getty Images. Manipulation of product imagery was undertaken using Canva and/or Photoshop.

### Wireframes
The wireframes below were created and used to loosely inform the development process.



Desktop![Desktop](https://github.com/PaulModaley/guitarstore/blob/0af6feb6c98f11f6fec7760e1ba69132d4b1de3b/media/Desktop.png)

Mobile![Mobile](https://github.com/PaulModaley/guitarstore/blob/dcec81588bc4e3a41a275051d5749a562108c8be/media/Mobile.png)


While the project relied on these wireframes, there are some differences between the wireframes and the final product due to time constraints and change of mind for different/better UI.


## Features

#### Home Page

Shown below on larger screen![Home](https://github.com/PaulModaley/guitarstore/blob/767912d0bca06699df433b36889ebb8c983a1cbd/media/home_page_hero.jpg)

![Home2](https://github.com/PaulModaley/guitarstore/blob/767912d0bca06699df433b36889ebb8c983a1cbd/media/home_page_smaller_screens.png)

#### Navigation

Shown below with active drop down menu![Nav](https://github.com/PaulModaley/guitarstore/blob/76027a471a2bce33f36a7b85d32378b43936ec16/media/navbar1.png)

Shown below with logged-in status of the user![Nav2](https://github.com/PaulModaley/guitarstore/blob/76027a471a2bce33f36a7b85d32378b43936ec16/media/navbar2_loggedin.png)


Shown below with logged-out status of the user![Nav3](https://github.com/PaulModaley/guitarstore/blob/6654a69dd05bda8f910d5e6b2f80af339bb6f051/media/navbar2_loggedout.png)

Mobile navigation![Nav3]
(https://github.com/PaulModaley/guitarstore/blob/6654a69dd05bda8f910d5e6b2f80af339bb6f051/media/nav_mobile.png)



### Future Features

* A 'Confirm to delete' modal, allowing the site users to confirm deletion of a product from their shopping cart to avoid accidental deletion.
* The ability for a registered user to delete their account with a 'Confirm to delete' modal.
* The ability for the logged in user to edit and delete their review(s).
* The ability for the logged in user to Add To Wishlist and Remove From Wishlist from the Listed Products page.
* The ability for the store owner to edit and delete Categories.
* A 'Confirm to delete' modal, allowing the store owner to confirm deletion of a product.or category in order to avoid accidental deletion.
* Pagination
* Contact Page

[Back to Top](#legato-music)

---

## **Information Architecture**

### Navigation bar

The navigation bar changes depending on user status and screen size:

| Nav Link                                      | Logged Out | Logged In (User) | Logged In (Admin) |
| --------------------------------------------- | ---------- | ---------------- | ----------------- |
| Logo (small screen)                           | &#10060;   | &#10060;         | &#10060;          |
| Logo (large screen)                           | &#9989;    | &#9989;          | &#9989;           |
| Home                                          | &#9989;    | &#9989;          | &#9989;           |
| Delicatessen with dropdown list of Categories | &#9989;    | &#9989;          | &#9989;           |
| Our Story                                     | &#9989;    | &#9989;          | &#9989;           |
| Contact                                       | &#9989;    | &#9989;          | &#9989;           |
| Search Our Site                               | &#9989;    | &#9989;          | &#9989;           |
| My Account                                    | &#9989;    | &#9989;          | &#9989;           |
| My Account dropdown - Login                   | &#9989;    | &#10060;         | &#10060;          |
| My Account dropdown - Register                | &#9989;    | &#10060;         | &#10060;          |
| My Account dropdown - Profile                 | &#10060;   | &#9989;          | &#9989;           |
| My Account dropdown - Log Out                 | &#10060;   | &#9989;          | &#9989;           |
| My Account dropdown - Add Category            | &#10060;   | &#10060;         | &#9989;           |
| My Account dropdown - Add Product             | &#10060;   | &#10060;         | &#9989;           |
| Wishlist                                      | &#10060;   | &#9989;          | &#9989;           |
| Shopping Basket Icon                          | &#9989;    | &#9989;          | &#9989;           |

### Database Design
The diagram below illustrates the database structure used in this project.
![Database Schema](documentation/database/database.png)

[Back to Top](#legato-music)

---

## **Technologies Used**

### Languages Used

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3#:~:text=CSS3%20is%20the%20latest%20evolution,flexible%20box%20or%20grid%20layouts.)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

### Site Design

* [Font Awesome](https://fontawesome.com/) was used to add the icons.
* [Coolers.co](https://coolors.co/a71313-3c3cdf-0f0f0f-ffffff-198754-ffca02) was used to generate the colour palette in the readme.
* [Google Fonts](https://fonts.google.com/) was used to import the _Suwannaphum_ and _Dancing Script_ font used within the site.
* [Favicon.io](https://favicon.io/favicon-converter/) was used to generate a favicon for the site using the site's logo.

### Hosting
* [GitHub](https://github.com/) is used to store the code for this project after being pushed from Git.
* [Heroku](https://www.heroku.com) was used to deploy the live site.

### Databases Platform and Cloud Storage
* [SQlite](https://www.sqlite.org/index.html) is the SQL database engine provided by default as part of Django and used during development.
* [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql) is the SQL database service provided directly by Heroku for storing the site's data.
* [Amazon AWS S3](https://s3.console.aws.amazon.com/s3) was used to host this project's images and static files.

### Frameworks and Libraries 

* [Django](https://www.djangoproject.com/) was used as a Python web framework for its rapid development and clean, pragmatic design
* [pip](https://pip.pypa.io/en/stable/) was used to install the required dependencies for this site.
* [Django-countries](https://pypi.org/project/django-countries/) was used for its pre-built country field containing all the valid country codes.
* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to manage rendering behaviour and layout of Django forms.
* [Gunicorn](https://gunicorn.org/) was used for WSGI HTTP Server to support deployment of Django application.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) was used to auto-populate the site with the contents of the database.
* [Stripe.js](https://stripe.com/docs/js) library was used for handling Stripe payment objects.
* [Bootstrap](https://getbootstrap.com/) was used to create a beautiful, responsive website.
* [jQuery](https://jquery.com/) was used to make the DOM traversal easier within the JavaScript.

### Other Technologies

* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to add and commit to Git and push to GitHub.
* [drawSQL](https://drawsql.app/) was used to design the schema of the relational database.
* [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.
* [Am I Responsive Design](http://ami.responsivedesign.is/) was used for the screenshot in this repository's README.md and TESTING.md.
* [Google DevTools](https://developer.chrome.com/docs/devtools/) was used to check site responsiveness, and as a general debugger.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse/) was used to check the site's Performance, Accessibility, Best Practices, and SEO.
* [Tinyjpg.com](https://tinyjpg.com/) was used to compress the images.
* [Gitpod](https://gitpod.io/) was used as a virtual IDE workspace to build this site.

### Testing

* [W3C Markup Validation Service](https://validator.w3.org/) was used to test that the HTML is valid.
* [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/) was used to test that the CSS is valid.
* [JSHint](https://jshint.com/) was used to test that the JavaScript is valid.
* [PEP8](http://pep8online.com/) was used to validate the python syntax.


[Back to Top](#legato-music)

---

## **Deployment**

### Requirements for Deployment

* An Integrated Development Environment (IDE) (e.g. GitPod or VSCode)
* Git (for version control)
* GitHub
* Python3
* pip, for Python package installation
* Heroku account
* AWS S3 account
* Stripe account
* Email account

#### This project was deployed in two stages:
### 1. Initial Deployment 
_Create a Heroku app, connect to Postgres database and deploy the app without static files._

* Gitpod Local environment
  | KEY         | VALUE |
  | ----------- | ----- |
  | DEVELOPMENT | True  |
  
* Create an env.py file in gitpod

    ```
  import os

  os.environ["SECRET_KEY"] = "#YOUR_SECRET_KEY#"
  os.environ["STRIPE_PUBLIC_KEY"] = "#YOUR_STRIPE_PUBLIC_KEY#"
  os.environ["STRIPE_SECRET_KEY"] = "#YOUR_STRIPE_SECRET_KEY#"
  os.environ["DATABASE_URL"] = "#YOUR_DATABASE_URL#"
  os.environ["STRIPE_WH_SECRET"] = "#YOUR_STRIPE_WH_SECRET#"
  os.environ["AWS_SECRET_ACCESS_KEY"] = "#YOUR_AWS_SECRET_ACCESS_KEY#"
  os.environ["AWS_ACCESS_KEY_ID"] = "#YOUR_AWS_ACCESS_KEY_ID#"
  os.environ["USE_AWS"] = True
  os.environ["EMAIL_HOST_PASS"] = "#YOUR_EMAIL_APP_PASS_CODE#"
  os.environ["EMAIL_HOST_USER"] = "#YOUR_EMAIL_ADDRESS#"
  ```

* To deploy this application on Heroku, Heroku needs to understand what dependencies are required, as well as which files to run for this project.
  * Create a requirements file: in the terminal type the following command:
    * `pip3 freeze --local > requirements.txt`
    * This file will hold a list of all dependencies required for this project.
  * Create a procfile: in the terminal type the following command:
    * `echo web: python run.py > Procfile` 
    * Make sure there is no blank line after the contents of this file.
* Commit and push these changes to GitHub.
* Login or sign up to [Heroku](https://www.heroku.com).
* Select '**Create New App**' in the top right of your dashboard.
* Choose a unique app name, and select the region closest to you, then click '**Create App**'.
* Go to the '**Deploy**' tab, find '**Deployment Method**', and select '**GitHub**'.
* Find your GitHub repository, and click '**Connect**'.
* Navigate to the '**Settings**' tab and click '**Reveal Config Vars**'.
* Enter key-value pairs that match those in your project files for the keys below:
  | KEY                   | VALUE                             |
  | --------------------- | --------------------------------- |
  | SECRET_KEY            | YOUR_SECRET_KEY                   |
  | STRIPE_PUBLIC_KEY     | YOUR_STRIPE_PUBLIC_KEY            |
  | STRIPE_SECRET_KEY     | YOUR_STRIPE_SECRET_KEY            |
  | DATABASE_URL          | YOUR_DATABASE_URL                 |
  | STRIPE_WH_SECRET      | YOUR_STRIPE_WH_SECRET             |
  | AWS_SECRET_ACCESS_KEY | YOUR_AWS_SECRET_ACCESS_KEY        |
  | AWS_ACCESS_KEY_ID     | YOUR_AWS_ACCESS_KEY_ID            |
  | USE_AWS               | YOUR_USE_AWS                      |
  | EMAIL_HOST_PASS       | YOUR_EMAIL_HOST_PASS              |
  | EMAIL_HOST_USER       | YOUR_EMAIL_HOST_USER              |
  | DISABLE_COLLECTSTATIC | 1 (Add this variable temporarily) |

* In Heroku, navigate to the '**Resources**' tab, and add on '**Heroku Postgres**' with the free plan.
* Back up your current sqlite database:
  * As this database was designed without fixtures, make sure manage.py file is connected to mysql database.
  * Backup the current database for each of desired model and load it into a db.json file: in the terminal type the following command:
  `python3 manage.py dumpdata your_model_name > db.json`
  * Repeat this action for each model you wish to transfer to the postgres database (alternatively you can backup your whole database)
* Load data from db.json file into postgres:
  * Create a temporary variable in your environement named: DATABASE_URL with the value of the Postgres URL from Heroku
  * Install the following packages and freeze the requirements: in the terminal type the following commands:
    * `pip3 install dj_database_url`
    * `pip3 install psycopg2-binary`
    * `pip3 freeze > requirements.txt`
  * In legato-music > settings.py, add `import dj_database_url` at top of the page
  * Connect your manage.py file to your postgres database  
    ```
    DATABASES = {
    'default':  dj_database_url.parse('DATABASE_URL')
    }
    ```
* Load your data from the db.json file into postgres: in the terminal type the following command:
  * `python3 manage.py loaddata <your_file>.json`
  * (if you have backed up several json files, repeat this action for each file)
* Make migrations to start using PostgreSQL: in the terminal type the following commands:
  * `python3 manage.py makemigrations`
  * `python3 manage.py migrate`
* Create a superuser to access the Django admin panel: in the terminal type the following command:
  * `python3 manage.py createsuperuser`
  * then add a username and password in the terminal
* Install the Heroku CLI and login: in the terminal type the following command:
  * `heroku login` or `heroku login -i`
* Remove `DISABLE_COLLECTSTATIC = 1` from your heroku config vars.
* Commit and push changes to GitHub.
* Add the hostname of your Heroku app to '**ALLOWED HOSTS**' in your settings.py file. This can be found in Heroku Settings > App Name.
* Navigate to the '**Deploy**' tab on your Heroku apps Dashboard, and click on '**Enable Automatic Deployment**'.
* Click open app to view the application in your browser, your app should display without any images and static files at this stage.

### 2. Amazon AWS
_Create and connect an Amazon bucket for storing images and static files._
#### S3 Bucket:
* Create a new bucket, give it a name, and choose the region closest to you.
* Go to 'Properties', turn on static website hosting, and type _index.html_ and _error.html_ for the index document & error document fields and save.
* Go to 'Permissions', and add the code block underneath this section into your CORS config to link Heroku and your S3 bucket.
* Go to the 'Permissions' tab and click on 'CORS configuration'.
* To link Heroku and your S3 bucket, paste in the following code into the area provided:
```
  [
  {
    "AllowedHeaders": [
      "Authorization"
    ],
    "AllowedMethods": [
    "GET"
    ],
    "AllowedOrigins": [
    "*"
    ],
    "ExposeHeaders": []
    }
  ]
```
* Still in the 'Permissions' tab, click 'Edit' on the 'Bucket Policy' and open the 'Policy Generator'.
* Use the following settings to setup the policy correctly:
  * _Type of Policy: 'S3 Bucket Policy'_
  * _Principal: '*' to allow all principles_
  * _Action: 'Get Object'_
  * _Amazon Resource Name (ARN): Paste your Bucket ARN and add * at the and of your Bucket Resource key arn:aws:s3:::bucket_name/_ 
  * Click 'Save'
* Still in the 'Permissions' tab, go to the 'Access Control List', Set the list of objects permission for everyone under the 'Public Access' section.

#### IAM
* Click on the 'Services' tab on the top left of the page and search for 'IAM'.
* Go to '**User Groups**', '**Create New Group**', enter a name, and click '**Create**'.
* Go to '**Policies**', '**Create New Policy**', '**JSON**', '**Import Managed Policy**', '**S3**', '**AmazonS3FullAccess**', '**Import**'.
* Get your ARN from '**S3 Permissions**', delete the `*` from '**Resource**', and add the code block underneath this section into the area.
* Click '**Next**', '**Review**', provide a name and description, and click '**Create Policy**'.
* Go to '**User Groups**', '**Find New Group**', '**Permissions**', '**Add Permissions**', '**Attach Policies**', find the policy you created, and click '**Add Permissions**'.
* Go to '**Users**', provide a name, and tick the checkbox beside '**Access key - Programmatic access**'.
* Click '**Next**', select the group you created in step 1, and click through to the end.
* Finally, click '**Create User**', and download the CSV file, which will contain your `AWS_SECRET_ACCESS_KEY` and your `AWS_ACCESS_KEY_ID`. This is the only time that this CSV file will be available, so it's very important to download it at this stage.

```python
"Resource": [
    "{YOUR ARN}",
    "{YOUR ARN}/*"
]
```

#### Final AWS Steps:
* Navigate to S3, you'll see that you have a '**static**' folder with all your static files in it.
* Create a '**media**' file in your S3 Bucket, click '**Upload**'.
* Click '**Add Files**', then add all your product images.
* Under '**Manage Public Permissions**', select '**Grant Public Read Access**'.
* Then click '**Upload**'.
* Finally, attempt to log in to the site using the superuser details, then access the '**admin**' panel on the live site, go to '**Email Addresses**', and select Primary and Verified on the superuser email address.

### How to Fork it

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [CarlaBuongiorno/la_fraschetta](https://github.com/CarlaBuongiorno/la_fraschetta).
3. In the top right, click "Fork".

### Making a Local Clone

1. Log in to [GitHub](https://www.github.com) and locate the [Repository](https://github.com/CarlaBuongiorno/la_fraschetta) for this site.
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should clone the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL that was copied in Step 4.
    * `git clone https://github.com/CarlaBuongiorno/la_fraschetta.git`
8. Press Enter, and your local clone will be created.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/CarlaBuongiorno/la_fraschetta)

[Back to Top](#legato-music)

---

## **Testing And Project Barrier Solutions**

All testing and project barriers and solutions has been documented here - [TESTING.md](https://github.com/CarlaBuongiorno/la_fraschetta/blob/master/TESTING.md)

[Back to Top](#legato-music)

---

## **Credits**

### Code

* [Code Institute](https://codeinstitute.net/) ecommerce walkthrough informed the creation of this project, including:
  * Code from Code Institute's, [Boutique Ado](https://boutique-ado-carla-buongiorno.herokuapp.com/) Mini Project Walkthrough by Chris Zielinski.
* [Stackoverflow](https://stackoverflow.com/) was referenced frequently to enable me to fix bugs and setup functionality.
* My mentor, Marcel Mulders, assisted me with deploying the project to Heroku and the set up of AWS.
* [CSS Tricks](https://css-tricks.com/snippets/css/css-triangle/) - enabled triangular pointers for toast 'success' messages. 
* [Django For Everybody - Full Python University Course](https://www.youtube.com/watch?v=o0XbHvKxw7Y&t=20867s) - referenced to enable me to implement functionality using the Django framework.
* [Bootstrap](https://getbootstrap.com/) was referenced to enable the responsivity, layout and styling of Legato Music. 
* [CSS Tricks](https://css-tricks.com/a-clever-sticky-footer-technique/) - Enabled me to position the footer at the bottom of the page.
* [Carla Buongiorno's La Fraschetta Repository](https://github.com/CarlaBuongiorno/la_fraschetta) - Code for the 'wishlist' features was borrowed and adapted from this repository. Moreover, the structure of the readme file form this repository has been used to inform the structure of this readme file. 
* Snippets of code taken from sources not listed here in the readme file are acknowledged and attributed throughout the source code using commented out text.  


### Media

* The hero image came from Getty Images but was edited by Paul Modaley using Canva and Photoshop.
* The product images came from various sources including Getty Images and Google. 

### Content

* All product descriptions were written by Paul Modaley. 
* All website copy, taglines and slogans was written by Paul Modaley.

### Acknowledgements

* Tutors and students of Code Institute and the Code Institute Slack Community for their assistance and support.
* My course mentor, Marcel Mulders, for his continuous support, assistance and dedication to enabling me to progress. 
* To my employer, Reputation, for giving me the opportunity to study coding and software development.
* Carla Buongiorno (former Code Institute student) whose repository was referenced in the creation of my project, including this readme file. 

[Back to Top](#legato-music)