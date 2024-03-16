# ToDoApp
A simple To-Do List built using Python, Flask, HTML, and CSS/Bootstrap.

![Logo](/screenshots/MockupMultiple-ToDo.jpeg)

## **Site Overview**
A simple To-Do List, a web application to track a dynamically changing list of jobs and/or tasks.

# Table of contents 
1. [**Site Overview**](#site-overview)
1. [**(UX) User Experience**](#ux-user-experience)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Site Aims***](#site-aims)
    * [***How This Will Be Achieved***](#how-is-this-will-be-achieved)
    * [***Colour Scheme***](#colour-scheme)
1. [**Mock Ups**](#mock-ups)
1. [**Technologies Used**](#technologies-used)
    * [***Languages***](#languages)
    * [***Modules & Imports***](#modules--imports)
1. [**Page Content & Features**](#page-content--features)
    * [***My To Do's***](#my-to-dos)
    * [***Sign Up***](#sign-up)
    * [***Login***](#login)
1. [**Models & Schema**](#models--schema)
    * [***Database***](#database)
    * [***Process***](#process)
1. [**Manual Testing**](#manual-testing)
1. [**Testing User-Stories**](#testing-user-stories)
1. [**Post Development Testing**](#post-development-testing)
    * [***Testing with PyTest***](#testing-with-pytest)
1. [**Deployment**](#deployment)
    * [***Local Deployment***](#local-deployment)
    * [***Security***](#security)
1. [**Future Enhancement**](#future-enhancements)
1. [**Credits**](#future-enhancements)

## **(UX) User Experience**
### **Target Audiences:**
* The target audience is anyone that is looking to organise their work or personal life.
* Anyone who needs or requires the ability to track a list of objectives, whether it's for a school project, personal project, or just for life in general.

### **User Stories:**
As a user, I want to...
* Continually add to the list.
* Delete things from the list as they are accomplished.
* Easily refer back to the list to see what still needs to be completed.

### **Site Aims:**
* To provide a simple way for users to keep track of tasks to be completed.
* Save the tasks for each user to a database, so the user can keep coming back.
* Allow the user to view the web app from a Desktop, Laptop, Tablet, or Mobile.
* Be easy to use with clear and simple functionality.
* Only allow viewing of the users list once logged in.

### **How This Will Be Achieved:**
* Create a dynamically generated list, where tasks can be created and deleted.
* Create a way for a user to log in and store any tasks created against the user's login profile.
* Use Bootstrap to create a responsive layout that can adjust to any platform.
* The web app will have clear and obvious buttons to carry out the relevant functions.
* It will also feature a clean and modern layout to help avoid any distractions.
* Confirmation messages will be shown to help show the user either a successful or unsuccessful function.
* The web app will feature a signup/login requirement to secure each user's tasks.
* The main To Do Task page will only be available once the user has logged in.

### **Colour Scheme**
The main background for each page will mainly be white with a header to add some variety.
Each of the buttons will be coloured to help identify their function, e.g. Red = Delete.
The success messages will be coloured green, and the unsuccessful messages will be coloured red to further help identify their intended message at a glance.

## **Mock-ups**
![Image](/screenshots/ToDoAppDesktop.jpg)

## **Technologies Used**
### **Languages**
* HTML
* CSS
* Python
* Javascript

### **Modules & Imports**
* Bootstrap
* Flask
* SQL-Alchemy
* See the requiremnets.txt for a full list of modules

## **Page Content & features**
### **My To Do's**
* Text area to add new tasks  
* Tasks displayed in a list alongside a 'mark as complete' and 'delete' button

### **Sign Up**
* Name, Email Address, Password enter form to register
* Link to switch to login page

### **Login**
* Email Address and Password entry form to login
* Link to switch to sign up page

## **Models & Schema**
### **Database**
* For the implementation of the ToDo Application, I required the use of a database to store both the user information once they had created their account and any notes each idividual user created.
* As the database itself won't be very resources intensive or data heavy, I have opted to use SQLite for simplicity.
* Below is a breakdown of the database models used in this application.

### **User**

| Column | Type | Unique | Primary Key | Foriegn Key |
| - | - | - | - | - |
| id  | Integer  | True | True | . |
| email  | String  | True | . | . |
| firstName | String | False | . | . |
| password | String | False | . | . |

### **Note**

| Column | Type | Unique | Primary Key | Foriegn Key |
| - | - | - | - | - |
| id  | Integer  | True | True | . |
| data | String  | False | . | . |
| done | Boolean | False | . | . |
| user_id | Integer | False | . | user.id |

* Once the user has register on the site, their sign up information is stored along with a unique ID in the database.
* Everytime the user creates a note, this unique ID is stored alonside that note in a seperate 'notes' table.

### **Process**
#### **Creating a note**
* A user has the ability to create any number of notes/todos, once the required text has been entered into the entry form click the 'Add Note' button and the note will be added to the database.

#### **Update a note**
* From the existing notes, the user has the option to toggle whether it has been completed or not.
* A tick is presented to the user alongside each note. Hovering over, provides a tooltip that this will mark the note as completed. Clicking on the tick will change the note, marking the done field as 'True' and showing the text as stiked through.
* The tick will change to a cross, and the tooltip will change to say 'Mark as Uncomplete'. Pressing this again, will mark the done field as 'False' and unstrike the text.

#### **Delete a note**
* The user also has the option of deleting the note completely.
* Along side each note, the user is presented with a trash can icon and a tooltip that this will 'Delete note'.
* Clicking this will remove that note from the database. 

## **Manual Testing:**
* During testing, I used five different browsers to ensure cross-compatibility. The desktop browsers used myself were:

  1. Chrome
  2. firefox  
  3. Opera
  4. Edge
  5. Safari

* I then used the dev tools to simulate different screen sizes/devices from 320 px up to 4000 px in width. 
* In addition to this, deployed the site to a cloud server and asked several people to test using iPhones and Apple Mac laptops/desktops. These users reported no issues or bugs.

## **Testing User Stories**
### Continually add to the list.

    - I can continuously add To-Do's to the list, with the list updating instantly each time.

### Delete things from the list as they are accomplished.

    - I can easily delete any To Do from the list by using the trash can button. The list updates instantly

### Easily refer back to the list to see what still needs to be completed.

    - I can easily log on to the website to view my list. The site remembers my session and automatically logs me in unless I've logged out.

## **Post Development Testing**
* During post-development, the site was checked using an HTML, CSS, and JS validator along with the use of a Python PEP8 checker to make sure everything follows the current standards for each of the code bases.
* Several violations were found on the PEP8 checker, these were simple fixes such as reducing the character length on a single line to below 79. Along with a few white space fixes.
* The HTML checker found several errors, however, these were pieces of Python code embedded within the HTML.
* Carrying out a lighthouse test passed everything apart from the best practices, however, this was from the test server not having an SSL certificate. In a real-world scenario, the server would be running one.
* The background images used were converted into the newer Webp format to help improve scores.

![image](/screenshots/lighthouse.png)

### **Testing with PyTest**
* Several tests were built using PyTest in order to test the full functionality of the web application. And can be ran using the 'pytest' command.
* These tests include emulations of:
    1. Signing up as a new user; including replicating various types of errors at sign up.
    2. Attempting to access the application without signing up.
    3. Logging in.
    4. Adding a note.
    5. Toggling a note as completed.

* The results and output of each test can be found in the [test_results.txt](/tests/test_results.txt)

## **Deployment**
* The final website was deployed to a Linux server running nginx to server up the website's HTML pages and gunicorn to handle the Python code.
* This can be reached by the following address http://todo.danryan.uk/login
* A test user can be used to access the website, with the following credentials:
    * Username: test@test.com
    * Password: Letmein1!

### **Local Deployment**
* The website can be deployed locally, once a virtual enviroment has been setup, Pip install the requirements.txt file in the main directory.
* Then run main.py to start the local server and run the web app.

### **Security**
* During the build process I was aware that the user would need to create an account to user the application. So the password is hashed on sign up.
* When logging in, this password is again hased then compared against the stored hash password in the database.
* The .env and database.db files have been chmod to 600 for further security.

## **Future Enhancements**
* I would like to add the ability for a user to reset their password. this could be achieved by implementing a reset page, tied with a link that would be emailed to the user's email address they entered upon signing up.
* Add the ability to set due-by dates
* Add the ability to add a priority and sort by priority.

## **Credits**
* Style and layout using Bootstrap - [Bootstrap](https://www.bootstrap.com)
* Fonts are from Google Fonts - [Google Fonts](https://fonts.google.com)
* Header Image/Background Image - [Pexels](https://www.pexels.com)
* Header Image/Background Image adjustments done in Adobe Photoshop - [Adobe](https://www.adobe.com)
* CSS Validator - [CSS Portal](https://www.cssportal.com/css-validator/)
* HTML Validator - [W3C](https://validator.w3.org/)
* JS Validator - [JSHint](https://jshint.com/)
* Python PEP8 Checker - [Python Checker](https://www.pythonchecker.com/)
* Grammarly for spelling and punctuation checking - [Grammarly](https://www.grammarly.com)

