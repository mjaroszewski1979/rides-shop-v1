## Rides Shop
### This is a Python application powered by Django and its Object-Relational Mapper to provide convenient access to stored data. In fact, Django's ORM is just a pythonical way to create SQL to query and manipulate your database and get results in a pythonic fashion. In this particular case users are able to view different car categories, as well as detailed informations about the very product they are interested in, and finally to narrow search results with filters.

--------------------------------------------------

### Features:
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Taking full advantage of Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Associating multiple records in a table with multiple records in another table ( many-to-many relationship ) to achieve optimal ORM performance
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Serving static files with WhiteNoise to accomplish high performance and efficiency without depending on nginx, Amazon S3 or any other external service
* Relying on Cloudinary to provide a secure and comprehensive API for easily uploading media files from server-side code
* Storing app’s secure credentials in environment variables
* Using django-filter which allows users to filter down a queryset based on a model’s fields and displaying the form to let them do this
* Implementing the paginator class - it takes in a queryset (such as a Django model) and splits it into Page objects that are then displayed across these pages while still using     the same HTML document
* Utilizing setUp method to handle especially expensive setup operations for all of the tests within a module
* Performing extensive selenium tests using 'page object pattern' instead of making raw WebDriver calls to have cleaner code:
  * Utilizing DRY (Don’t repeat yourself) principle to minimize code duplication by having all ID-locators in one place
  * Setting an interface between web page’s elements and tests
  * Avoiding usage of WebDriver APIs in test methods
  * Encapsulating the services of web pages, not only exposing their elements

--------------------------------------------------

### Code Coverage:
* Selenium and unit tests combined

```
coverage run -p manage.py test unit_tests && coverage run -p manage.py test selenium_tests && coverage combine && coverage html

```

<img src="https://github.com/mjaroszewski1979/rides-shop-v1/blob/main/cov_report.png">

------------------------------------------------

### Docker info:
* Pull an image from my Docker Hub - click on the icon below
* Create and start a container 
* Pass environment variables to your container
  * with the -e flag or using .env file

```
docker run -p 8000:8000 -e SECRET_KEY="<your secret key>"  <imagename>

```
```
docker run -p 8000:8000 --env-file .env <imagename>

```

--------------------------------------------------

![caption](https://github.com/mjaroszewski1979/rides-shop-v1/blob/main/rides_mockup.png)
  
Code | Docker | Technologies
---- | ------ | ------------
[<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/rides-shop-v1) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/rides_shop) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp;  <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/js1.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/cloudinary.png">
