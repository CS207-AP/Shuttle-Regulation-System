# Shuttle-Regulation-System
CS-207 (Advanced Programing)
7 December 2018
Final Term Project








Ashoka Shuttle Management System







											Submitted by: 
Sona M., Rathi K., Prashanthi R., and Shivangi K.

Project Report

You are returning to campus from the winter break. You are late for the last shuttle to leave for campus. Now you’re stuck in the cold with the 50 frustrated passengers waiting for the next shuttle to arrive. 

GITHUB LINK TO PROJECT: https://github.com/CS207-AP/Shuttle-Regulation-System

Scope of this project:
This group attempts to regulate shuttle service and help Ashokans commute comfortably. The Ashoka University Shuttle Management App gives its users the ability to book their shuttle seats.

2. Using Ashoka Shuttle Management:

1. The user enters their email id. 


2. Here, there is a drop-down menu with the list of shuttle timings out of which the user is requested to select the time as per their need.



3. Depending on the number of seats booked by other users, the user gets a confirmed or waitlisted message along with the waitlisted message. 

4. The system records the number of bookings which gives an estimate to the user and the shuttle incharge on the number of people desiring to take the shuttle to decide if they have to send another shuttle to accommodate the remaining people. 


3. Languages used

Flask
Python
SQLite 
HTML
CSS 

4. Methodology and Flow:

i) The first step was to set up the main website for Ashoka Shuttle Management App using Flask in a file main.py. In this file, we import the Flask class and created an instance of this class. We then used the route() decorator to tell flask which URL should trigger which function. The functions in this file were linked to the HTML pages which were displayed on the server. For this project, we used an externally visible server, the host of which was our computer’s IP address. (The landing page being 10.1.36.30:5000/).

ii) Our second step was to create the database which we implemented using SQLite. The schema for our database included a table which consisted of id as the primary key and Email and Shuttletime as the other columns. We linked the SQL database to the Flask server through another file models.py where we linked the SQL server to the Flask server using sql.connect(). This program also contained a list of functions that were implemented in our web application which are as follows: 

countFunction(): This function counted the number of users selecting a particular shuttle time. It prints Confirmed Seat when the count is less than twenty (number of seats in the shuttle) and Waitlist when the count is less than twenty. This function gives the user and the shuttle incharge an idea of the number of people taking a particular shuttle.\
insertUser(): To insert user information into the database. 
retrieveUsers(): To retrieve user data from the database. 

iii) Our next step was to create the HTML and CSS files that would serve as the graphic user interface. In order to navigate through these HTML files, we had to enclose them within a form with the form action specifying the route to the next HTML file corresponding to the route specified in main.py. The form method for all these files are specified as POST requests.

iv) The HTML files we created included homepage.html which served as the landing page for the web application. The users were then directed to index.html on clicking “Book your Shuttle” on the homepage where they could enter their email addresses and choose a Shuttle Time from the drop-down menu listbox, which was stored in the database using insertUser(). The user is then redirected to a page either confirming or waitlisting the user based on the count of people who have registered for the same shuttle. If the count of passengers, who have booked a particular shuttle was greater than 20, the user will be directed to the waitlisted.html page. Else, to confirmed.html. 
Further,  the admin can view the number of people who have booked for a shuttle at a particular time by visiting the URL 10.1.36.30:5000/admin. 
5. Challenges Faced and Tackled 

The members of the group had no prior knowledge of the languages used (except HTML and CSS). We learnt a major part of three new languages-- Flask, Python and SQLite for the sake of this project.
Defining and running functions was a huge challenge, especially functions which accessed the SQLite database. 
Linking web pages via Flask.
Understanding the concept of POST and GET and implementing them inside the HTML file.
We were able to figure out the majority of Google OAuth. However, we were not able to integrate it with our main web application.
Defining and executing functions in Flask.
Counting the number of bookings made for a given time.
Creating a page for the admin that displays count of the shuttle timings booked.

6. Scope for Expansion:

Authorising and restricting access to Ashoka mail accounts using Google OAuth.
Restricting users to provide input 45 minutes prior to the shuttle timing such that the admin has sufficient time to send another shuttle.
Currently, this app allows a user to book a shuttle of a particular time more than once. For example, a user can confirm more than one seat in a shuttle of the same time. Once logging in and logging out of accounts is enabled, this can be prevented. 
The admin can access the details using an HTML page: http://10.1.36.30:5000/admin. However, this gives everyone access to user information. This makes the web server insecure. Security of user data can be worked on.
An email from the shuttle email id to users who have been confirmed, 30 minutes prior to the shuttle time can be sent.  
This could be expanded to features like scheduling the shuttle time to optimise time, such as those in flight ticket booking portals.


7.  Division of work:

The members of this group put equal amount of effort in understanding and implementing the various concepts. There was a brainstorming session which helped us to come up with useful ideas with equal representation of each member of the team. 


A peek into one of our brainstorming session

Broadly the division of work was as follows:

Prashanthi R. and Shivangi K. focused on designing GUI and login. They worked on implementing Google OAuth into the login page of the web app. But, due to issues concerning the database, they were unable to execute it. However, they are persistent on making it work. They created the HTML pages and the CSS associated with them to give a good shape to the web application. 

 Rathi K. and Sona M. focused on the back-end which involved working with function execution, linking the web pages to the database using Flask, Python and SQLite. They worked on creating a database for shuttle timing and user login email id. They built functions in python to retrieve data from the database and store them for counting the number of bookings made at a given time. This was a great learning experience for both of them. 

8. Major Learnings from CS-207 used in the Project:

Concepts pertaining to Database and File Handling, that we learnt in class, helped us store data in the database and access it when necessary.
Working with Functions.
Object Oriented Programming: We put to use what we had learnt on parsing values as objects and accessing them.  
Patience and perseverance and logical thinking.


