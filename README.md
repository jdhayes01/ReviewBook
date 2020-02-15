# ReviewBook
A web application built in Django that allows users to track and rate the books they've read. This project had specified requirements by SpaceBase for their interview process. This project meets the basic requirements along with 3 "Road Map" features using Bootstrap, Django, mySQL, and deployed in an AWS Elastic Beanstalk environment.

## ReviewBook Features
### Account management
  * Users can create an account 
  * Users can log in
  * Users can reset their password via email link
  * Users can reset their password within the user dashboard
### Book list
  * Users can view their own list of books 
  * Users can add books to their list 
  * Users can update/edit the books on their list 
  * Users can remove books from their list 
  * Users can rate their books on a scale of 1 to 5
  * A list of books can only be viewed by its owner 
  * Most of the functionality is within the user dashboard 
### Dashboard/Homepage 
  * The dashboard displays the top 5 highest rated books 
  * The dashboard displays the top 5 most read books 
  * The dashboard displays the 5 books added most recently
  * Both visitors and authenticated users can view the dashboard
### Extra Features
  * Deploy Application - This application is deployed in AWS Elastic Beanstalk and the mySQL DB is in AWS RDS.
  * CSV Export - This application has a CSV download within the user dashboard. Implemented using the Python CSV library.
  * Unit Testing - Unit test are important especially for an MVP to set a strong foundation within the code base. So using django.test.TestCase, I wrote unit tests for model, views, and forms within the dashboard application.

