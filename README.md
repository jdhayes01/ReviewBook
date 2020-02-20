# ReviewBook
A web application built in Django that allows users to track and rate the books they've read.  
Stack: Bootstrap, Django, mySQL, and deployed in an AWS Elastic Beanstalk environment.
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
  * Deploy Application - This application is deployed in AWS Elastic Beanstalk and the mySQL DB is in AWS RDS. Users can't access the application otherwise so I thought deploying the app was very important.
  * CSV Export - This application has a CSV download within the user dashboard. Implemented using the Python CSV library. Users needed an option to export their book list and it's always good to earn a hypothetical client from a simple feature.
  * Unit Testing - Unit test are important especially for an MVP to set a strong foundation within the code base. So using django.test.TestCase, I wrote unit tests for model, views, and forms within the dashboard application.

