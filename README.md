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

[Search Engine Optimisation](#search-engine-optimisation)

[Marketing](#marketing)

[Social Media](#social-media)

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


While the project development was guided by these wireframes, there are differences between the wireframes and the final product which came about as a result of creative experimentation and design changes to ensure a better user experience.


## Features

### Home Page

Featuring a distinctive hero image and tagline, the home page presents the user various options to access product categories and other functions on the website. By clicking the logo/website title displayed at the top of the screen, the user can return to the home page from any other page of the website. Organised into several rows and sections, the home page design ensures ease-of-navigation for the user.

Shown below on larger screen![Home](https://github.com/PaulModaley/guitarstore/blob/767912d0bca06699df433b36889ebb8c983a1cbd/media/home_page_hero.jpg)

Shown here on smaller screen![Home2](https://github.com/PaulModaley/guitarstore/blob/767912d0bca06699df433b36889ebb8c983a1cbd/media/home_page_smaller_screens.png)

### Navigation

The website features responsive navigation bars. On larger screens, one navigation bar on the left side of the screen, enables users to go to particular product categories while the navigation bar to the upper-right of the screen enables the user to login/logout, access their profile, view the wishlist and checkout.

On smaller screens, the navigation bars collapse to a single hamburger menu but all the functionality of the navigation bars is retained. 

Crucially, the navigation's drop down items change to indicate the logged-in/out status of the user. 

Shown below with active drop down menu![Nav](https://github.com/PaulModaley/guitarstore/blob/76027a471a2bce33f36a7b85d32378b43936ec16/media/navbar1.png)

Shown below with logged-in status of the user![Nav2](https://github.com/PaulModaley/guitarstore/blob/76027a471a2bce33f36a7b85d32378b43936ec16/media/navbar2_loggedin.png)


Shown below with logged-out status of the user![Nav3](https://github.com/PaulModaley/guitarstore/blob/6654a69dd05bda8f910d5e6b2f80af339bb6f051/media/navbar2_loggedout.png)

Mobile navigation![Nav3](https://github.com/PaulModaley/guitarstore/blob/6654a69dd05bda8f910d5e6b2f80af339bb6f051/media/nav_mobile.png)

### Footer

The footer adapts to fit screens of various sizes. Placed within the footer are social media icons, which direct to social media pages, and a newsletter sign up form.

Footer on smaller screens![Footer1](https://github.com/PaulModaley/guitarstore/blob/09c6e7d457718d2584e53b766c9613991964a6ea/media/footer_smaller_screen.png)

Footer on larger screens![Footer2](https://github.com/PaulModaley/guitarstore/blob/09c6e7d457718d2584e53b766c9613991964a6ea/media/footer_large_screen.png)

### Registration

Non-registered users may open an account view the 'Register' page accessible via the navigation at top, right hand side. During the registration process, users are asked to confirm their chosen password (desktop view).

Once successfully regsitered, users when returning to the site may login via the navigation bar on the right hand side at the top of the page (desktop view).

The same functioanlity can be accessed via the hamburger menu icon in mobile view. 

Sign-in page![Login](https://github.com/PaulModaley/guitarstore/blob/eb1407f30f471c276e898c0a71f53949c18f1b9a/media/sign_in.png).

Registration page![Register](https://github.com/PaulModaley/guitarstore/blob/eb1407f30f471c276e898c0a71f53949c18f1b9a/media/register.png)

### Product Page

The user can view categories of products and sort them according to rating or by price using a dropdown menu. Individual products are displayed within cards which the user may click to view product details. 

Product page displaying items including sort button![Products](https://github.com/PaulModaley/guitarstore/blob/09c6e7d457718d2584e53b766c9613991964a6ea/media/products.png)

### Shopping Cart Page

From the shopping cart page, the user can view items they have added to the shopping cart prior to checkout. Displaying items in a tabular format, the checkout page features buttons to add or remove items from the shopping cart while the subtotal and total costs of items displays lower down the page.

Shopping cart containing an item![Cart1](https://github.com/PaulModaley/guitarstore/blob/bf0efb835bb47b6568654e3e080b465f7d1a7507/media/shopping_cart.png)

Empty shopping cart![Cart2](https://github.com/PaulModaley/guitarstore/blob/33b05a61eac3d47fd2fd14548dbdce0c132f0fde/media/empty_shopping_cart.png)

### Checkout Page

To checkout and make payment for items, the user must complete a form including payment information. Upon successful completion of the form, the page redirects to a confirmation page and a 'success' message is displayed to the user.

Checkout page on larger screen![Checkout](https://github.com/PaulModaley/guitarstore/blob/33b05a61eac3d47fd2fd14548dbdce0c132f0fde/media/checkout.png)

### Contact Us Page

Users may submit the contact form for general queries.

Contact us page featuring form rendered using crispy forms![Contact](https://github.com/PaulModaley/guitarstore/blob/064037f3387af44074b7ef5f9423f48fac68fcd2/media/contact_us.png)

### Wishlist Page

Users may add items to the wishlist from any product details page. 

Wishlist page showing a user's saved item![Wish](https://github.com/PaulModaley/guitarstore/blob/fe035f75f00c4f57fa98be876e5b98cb1cc04bed/media/wishlist.png)

### Toasts

Example of 'success message' displayed upon completion of a user action![Toasts](https://github.com/PaulModaley/guitarstore/blob/fe035f75f00c4f57fa98be876e5b98cb1cc04bed/media/toast_example.png)

### Newsletter Signup Form

Newsletter signup form located within the site footer![Newsletter](https://github.com/PaulModaley/guitarstore/blob/03865539ad67ec8ac5caa01e635c8879ed84116f/media/newsletter.png)

### Future Features

* A 'confirm to delete' modal to enable site users to confirm deletion of a product from their shopping cart and avoid accidental deletion.
* The ability for a registered user to delete their account with a 'confirm to delete' modal.
* The ability for the logged-in user to edit and delete their review(s).
* The ability for the logged-in user to add and remove items to/from the Wishlist directly from the list of products rather than only the product details page.
* The ability for the store owner to edit and delete categories without having to access Django's admin panel.
* A 'Confirm to delete' modal, allowing the store owner to confirm deletion of a product.or category in order to avoid accidental deletion.
* A 'Register' modal to encourage non-registered users to open an account.
* The ability to create custom wishlist names so that the user may create wishlists based on a product type or around seasonality (e.g. a Christmas wishlist)

[Back to Top](#legato-music)

---

## **Information Architecture**

### Database Models

Profile model:

```python
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label="Country", null=True, blank=True)

    def __str__(self):
        return self.user.username
```
Product model:
```python
class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
```


Order model:
```python
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_cart = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default="")

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum("lineitem_total"))[
            "lineitem_total__sum"
        ]
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
```
Order line item model:
```python
class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    product_size = models.CharField(
        max_length=2, null=True, blank=True
    )  # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.product.sku} on order {self.order.order_number}"
```


Category model:
```python
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
```

Review model:
```python
class Review(models.Model):
    """
    Stores review details in the database
    """

    RATING = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)
    review = models.TextField(max_length=1500)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_profile} | Product: {self.product} | \
                Rating: {self.rating}"
```

Wishlist model:
```python
class WishList(models.Model):
    """
    Model to show all product items within the users wishlist
    """

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"WishList ({self.user_profile})"
```

Contact model:
```python
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=500)
```

Newsletter model:
```python
class Subscribe(models.Model):
    email = models.EmailField(max_length=250)
```

[Back to Top](#legato-music)

---

## **Technologies Used**

### Languages Used

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3#:~:text=CSS3%20is%20the%20latest%20evolution,flexible%20box%20or%20grid%20layouts.)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

### Site Design

* [Bootstrap](https://getbootstrap.com/) was used to ensure the website's responsivity and faster development.
* [Font Awesome](https://fontawesome.com/) was used to add various icons, including the cart and wishlist icons.
* [Scheme Color](https://www.schemecolor.com/music-store.php) was used to generate the colour palette in the readme.
* [Google Fonts](https://fonts.google.com/) was used to import the 'Comfortaa' font used throughout the site.

### Hosting
* [GitHub](https://github.com/) is used to store the code respository for this project after being commited from Git.
* [Heroku](https://www.heroku.com) was used to deploy the live site.

### Databases Platform and Cloud Storage
* [SQlite](https://www.sqlite.org/index.html) is the SQL database engine provided by default as part of the Django framework. It provides the database and backend functionality for Legato Music's functionality, including the product catalogue.
* [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql) is the SQL database service provided directly by Heroku for storing the site's data.
* [Amazon AWS S3](https://s3.console.aws.amazon.com/s3) was used to host this project's images and static files.

### Frameworks and Libraries 

* [Django](https://www.djangoproject.com/) was used as a Python web framework to enable speedy development.
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
* Adobe Photoshop was used for image editing.
* [Canva](https://www.canva.com/) was also used for image editing. 
* [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.
* [Am I Responsive Design](http://ami.responsivedesign.is/) was used for the screenshot in this repository's README.md file.
* [Google DevTools](https://developer.chrome.com/docs/devtools/) was used to check site responsiveness, and as a general debugger.
* [Snipboard.io](https://snipboard.io/) was used to store and edit screenshots before adding them to the readme file.
* [Gitpod](https://gitpod.io/) was used as a virtual IDE workspace to build this site.
* [Black](https://black.readthedocs.io/en/stable/#) was used to speed up the process of formatting Python code.

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
2. On GitHub, go to [PaulModaley/musicstore](https://github.com/PaulModaley/musicstore).
3. In the top right, click "Fork".

### Making a Local Clone

1. Log in to [GitHub](https://www.github.com) and locate the [Repository](https://github.com/PaulModaley/musicstore) for this site.
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should clone the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL that was copied in Step 4.
8. Press Enter, and your local clone will be created.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/PaulModaley/musicstore)

[Back to Top](#legato-music)

---

## **Testing**

* [W3C Markup Validation Service](https://validator.w3.org/) was used to test that the HTML is valid.
* [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/) was used to test that the CSS is valid.
* [JSHint](https://jshint.com/) was used to test that the JavaScript is valid.
* [PEP8](http://pep8online.com/) was used to validate the python syntax.

#### HTML

All HTML pages were put through W3C and no errors were found.

![HTML](https://github.com/PaulModaley/guitarstore/blob/6b9a5c6ed786e9b8628777b1be93ddd7193363e4/media/paul-legatomusic_home.png)

#### CSS

My root CSS file was put through W3C and no errors were found.

![CSS](https://github.com/PaulModaley/guitarstore/blob/6b9a5c6ed786e9b8628777b1be93ddd7193363e4/media/CSS.png)

#### JavaScript

JSHint was used to check my JavaScript files for errors. Although several warnings were issued, no errors were detected.

![JavaScript](https://github.com/PaulModaley/guitarstore/blob/6b9a5c6ed786e9b8628777b1be93ddd7193363e4/media/JShint.png)

#### Python

All Python code was put through PEP8 online. No errors were detected.

[Back to Top](#legato-music)

## Manual Testing

I have tested my site extensively within Google Chrome on multiple devices, including
-   iPhone 5, 6, 7, 8, 9, X
-   Samsung Galaxy S8+, S20 Ultra
-   iPhone XS Max
-   iPad Pro
-   MacBook Pro

Please find below my testing process for all pages via mobile and web:

### Navigation Bar

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | Clicking "Legato Music" in the navigation bar redirects to the home page. | PASS
All products page | When clicking the "All Products" link in the navigation bar, the category shows a dropdown list so I have access to more sort/filter options. The page heading indicates the users location on the site. | PASS
Register page | Clicking the "register" link in the navigation bar redirects to the register page. The page heading indicates the users location on the site. | PASS
Login / Logout page | Clicking the "login" or "logout links in the navigation bar redirects to the login or logout page. | PASS
Cart page | When clicking the "cart" icon in the navigation bar, the browser redirects me to the cart page. The page heading indicates the users location on the site. | PASS
Wishlist page | When clicking the "wishlist" icon in the navigation bar, the browser redirects me to the wishlist page. The page heading indicates the users location on the site. | PASS
Contact page | When clicking the "contact" icon in the navigation bar, the browser redirects me to the contact page. The page heading indicates the users location on the site. | PASS
My Profile page | When clicking the "My profile" link in the navigation bar, the browser redirects me to my profile page. The page heading indicates the users location on the site. | PASS
Product management page | When clicking the "product management" link as a superuser in the navigation bar, the browser redirects me to the product management page. The page heading indicates the users location on the site. | PASS
Search bar | When searching for a keyword, the results will show products that contain the keyword in the product name or description. | PASS
Foreground & background colour | Checked foreground information is not distracted by background elements. | PASS
Text | Checked that all fonts and colours used are consistent. | PASS


### Footer

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Subscribe to newsletter | Completion of the newsletter form in the footer results in the display of a success message. | PASS
Facebook | Clicking the Facebook icon opens a new tab and redirects to the Facebook website, specifically Legato Music's Facebook page. | PASS
Twitter | Clicking the Twitter icon opens a new tab and redirects to the Twitter website. | PASS
Instagram | Clicking the Instagram icon opens a new tab and redirects to the Instagram website. | PASS
LinkedIn | Clicking the LinkedIn icon opens a new tab and redirects to the LinkedIn website. | PASS

### Home page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no (or minimal) pixelation or stretched images and are responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS

### Products page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and are responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Sort filter | Check the sort/filter functionality by selecting each option. Each option reloads the page and sorts the products in the corresponding order. | PASS
Edit Button (SuperUser only) | Check the edit button is only accessible if the user is logged in as a SuperUser. | PASS
Delete Button (SuperUser only) | Check the delete button is only accessible if the user is logged in as a SuperUser. | PASS

### Products details page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and are responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Quantity Selector | Check the quantity selector functionality by selecting minus and plus buttons where applicable. Adding a product to the basket to confirm the correct quantity selected is correct. | PASS
Edit Button (SuperUser only) | Check the edit button is only accessible if the user is logged in as a SuperUser. | PASS
Delete Button (SuperUser only) | Check the delete button is only accessible if the user is logged in as a SuperUser. | PASS

### Shopping cart page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no (or minimal) pixelation or stretched images and are responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Remove item from cart | Clicking the remove link on an item removes the item from the cart. | PASS
Quantity Selector | Check the quantity selector functionality by selecting min and plus buttons where applicable. Adding a product to the cart to confirm the correct quantity selected is correct. | PASS
Free delivery threshold | Adding products to the cart where the grand total value is under £50, the cart shows the free delivery warning message. The message disappears when the grand total is over £50. | PASS

### Checkout page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and are responsive on all devices. | PASS
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Checkout form | Filling in the form with the correct validation processes the order. | PASS
Checkout form | Filling in the form with the incorrect validation shows errors messages. | PASS
Save details checkout | Selecting the "Save this delivery information to my profile" checkbox, this saves/updates my profile details. | PASS
Card authentication | Used the Stripe test card details and purposely failed authenticated to check for error messages. | PASS

### Checkout success page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Order history | When clicking on an order number in the order history section, this takes me to a past order confirmation summary page. | PASS
Updating my profile | When updating the default delivery information, this reflects on the checkout page. | PASS

### Product management page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Adding a product | When filling out the form to add a new product, the product is added to the relevant category and is searchable via the search bar. | PASS
Uploading an image | When uploading an image to a new product, the site shows the name of the file that will be uploaded. When checking the product details page, the image also shows. | PASS

### Wishlist page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Adding an item to wishlist | When the wishlist (heart) icon is clicked on a product details page, the item is added to the user's wishlist. | PASS
Removing an item from wishlist | When the remove (dustbin) icon is clicked on the wishlist page, the item is removed from the wishlist and a success message appears. The user is taken to the product detail page. | PASS

### Contact page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on the page for consistent scalability in mobile, tablet and desktop view.| PASS
Submitting the contact form | When all the fields are filled correctly and the user clicks 'submit', a success message appears. | PASS
Incorrect or missing fields on contact form | When the user inputs invalid information or there is a missing field in the form, the form will not submit. Tooltips appear to notify the user of their error. | PASS

---
## **Search Engine Optimisation**

To optimise the site for search engines, I employed the following strategies and techniques:

* Added numerous long-tail and short-tail keywords to the meta tag within the projects base.html file
* Keywords were selected based on their relevance to the products and the target audience as well as their search volumes and levels of competition around those keywords
* To enable search engines to crawl the website, I have included a sitemap.xml file


## **Marketing**

Legato Music was created with the 5Ps of the marketing mix in mind:

PRODUCT/SERVICE - An e-commerce site selling musical instruments and equipment for beginners, intermediate and advanced players. 


PRICE - Products are priced competitively yet realistically reflecting the quality and range of goods available.


PROMOTION - Legato Music shall be promoted through its SEO (keyword strategy), email marketing (newsletter), and social media promotion (Facebook page).


PLACE - Legato Music exists solely online.


PEOPLE - Legato Music sells products to musicians and beginners musicians who want the convenience of online shopping. 

## **Social Media**

![Facebook Page](https://github.com/PaulModaley/guitarstore/blob/0f79d252f44f81c772cfc0c3b92cdfd2cc1e34d3/media/facebook.png)

Legato Music aims to use Facebook to promote its products, services and offers to a wider audience. 

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
* [Carla Buongiorno's La Fraschetta Repository](https://github.com/CarlaBuongiorno/la_fraschetta) - Code for the 'wishlist' feature was adapted from this repository. Moreover, the structure of the readme file form this repository has been used to inform the structure of this readme file. 
* [iKelvvv's MS5 Repository](https://github.com/iKelvvv/MS5/blob/main/README.md) - Readme file was referenced to inform the structure and development of my readme file for this project. 
* [30 Seconds of Code](https://www.30secondsofcode.org/css/s/hover-underline-animation) - CSS for the underline animation of the navigation buttons.
* Other snippets of code taken from sources not listed here in the readme file are acknowledged and attributed throughout the source code using commented out text.  


### Media

* The hero image came from Getty Images but was edited by Paul Modaley using Canva and Photoshop.
* The product images came from various sources including Getty Images and Google. 

### Content

* All product descriptions were written by Paul Modaley. 
* Website copy, taglines and slogans were written by Paul Modaley.

### Acknowledgements

* To my family and my wife in particular for being incredibly supportive and encouraging.
* Tutors and students of Code Institute and the Code Institute Slack Community for their assistance and support.
* My course mentor, Marcel Mulders, for his continuous support, assistance and dedication to enabling me to progress. 
* To my employer, Reputation, for giving me the opportunity to study coding and software development.
* Carla Buongiorno (former Code Institute student) whose repository was referenced in the creation of my project, including this readme file. 

[Back to Top](#legato-music)