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
1. [**Manual Testing**](#manual-testing)
1. [**Testing User-Stories**](#testing-user-stories)
1. [**Post Development Testing**](#post-development-testing)
1. [**Deployment**](#deployment)
    *[***Local Deployment***](#local-deployment)
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
* Tasks displayed in a list alongside a delete button
* Text area to add new tasks  

### **Sign Up**
* Name, Email Address, Password enter form to register
* Link to switch to login page

### **Login**
* Email Address and Password entry form to login
* Link to switch to sign up page

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

## **Deployment**
* The final website was deployed to a Linux server running nginx to server up the website's HTML pages and gunicorn to handle the Python code.
* The .env and database.db files have been chmod to 600 for further security
* This can be reached by the following address http://todo.danryan.uk/login
* A test user can be used to access the website, with the following credentials:
    * Username: test@test.com
    * Password: Letmein1!

### **Local Deployment**
* The website can be deployed locally, once a virtual enviroment has been setup, Pip install the requirements.txt file in the main directory.
* Then run main.py to start the local server and run the web app.

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

