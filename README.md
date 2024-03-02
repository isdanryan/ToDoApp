# ToDoApp
A simple To Do List built using Python, Flask, HTML and CSS/Bootstrap.

![Logo](/screenshots/MockupMultiple-ToDo.jpeg)

## **Site Overview**
A simple To Do List, web application to track a dynamically changing list of jobs and/or tasks.


# Table of contents 
1. [**Site Overview**](#site-overview)
1. [**(UX) User Experience**](#ux-user-experience)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Site Aims***](#site-aims)
    * [***How This Will Be Achieved***](#how-is-this-will-be-achieved)
    * [***Colour Scheme***](#colour-scheme)
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
1. [**Future Enhancement**](#future-enhancements)
1. [**Credits**](#future-enhancements)

## **(UX) User Experience**
### **Target Audiences:**
* The target audience is anyone that is looking to organise their work or personal life.
* Anyone that needs or requires the ability to track a list of objectives, wether it's for a school project, personal project or just for life in general.

### **User Stories:**
As a user I want to...
* Continually add to the list.
* Delete things from the list as they are accomplished.
* Easily refer back to the list to see what still needs to be completed.

### **Site Aims:**
* To provide a simple way for users to keep track of task to be completed.
* Save the tasks for each individual user to a database, so the user can keep coming back.
* Allow the user to view the web app from Desktop, Laptop, Tablet or Mobile.
* Be easy to use with clear and simple functionality.
* Only allow viewing of users list once logged in.

### **How This Will Be Achieved:**
* Create a dynamically generated list, where tasks can be created and deleted.
* Create a way for a user to login and store any tasks created against the users login profile.
* Use bootstrap to create a responsive layout that can adjust to any platform.
* The web app will have clear and obvious buttons to carry out the relevant functions.
* It will also feature a clean and modern layout to help avoid any distractions.
* Confirmation messages will be shown to help show the user either a succesful or unsuccessful function.
* The web app will feature a sign up/login requirement to secure each users tasks.
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
* See the requiremnets.txt for full list of modules

## **Page Content & features**
## **My To Do's**
* Tasks displayed in a list along side delete button
* Text area to add new tasks  

## **Sign Up**
* Name, Email Address, Password enter form to register
* Link to switch to login page

## **Login**
* Email Address and Password entry form to login
* Link to switch to sign up page

### **Manual Testing:**
* During testing, I used five different browsers to ensure cross-compatibility. The desktop browsers used myself were:

  1. Chrome
  2. firefox  
  3. Opera
  4. Edge
  5. Safari

* I then used the dev tools to simulate different screen sizes/devices from 320 px up to 4000 px in width. 
* In addition to this, I also asked several people to test using iPhones and Apple Mac laptops/desktops. These users reported no issues or bugs.

### **Testing User Stories**
## Continually add to the list.

    - I can continuosly add To Do's to the list, with the list updating instantly each time.

## Delete things from the list as they are accomplished.

    - I can easily delete any To Do from the list by using the trash can button. The list updates instantly

## Easily refer back to the list to see what still needs to be completed.

    - I can easily log on to website to view my list. The site remembers my session and automatically logs me in, unless i've logged out.

### **Post Development Testing**
* During post development, the site was checked using a HTML, CSS and JS validator along with the use of a Python PEP8 checker to make sure everything follows the current standards for each of the code bases.
* Any errors or violations found were fixed.

### **Deployment**
* The final website was deployed to a linux server running nginx to handle server up the websites html pages and gunicorn to handle the python code.
* The site can be ran in a vertual enviroment on a local machine. To deploy 

### **Future Enhancements**
* I would like add the ability for a user to reset their password. this could be achieved by implementing a reset page, tied with a link that would be emailed to the user's email address they entered upon sigining up.
* Add the ability to set due by dates
* Add the ability to add a priority and sort by priority.

### **Credits**
* Style and layout using Bootstrap - [Bootstrap](https://www.bootstrap.com)
* Fonts are from Google Fonts - [Google Fonts](https://fonts.google.com)
* Header Image/Background Image - [Pexels](https://www.pexels.com)
* Header Image/Background Image adjustments done in Adobe Photoshop - [Adobe](https://www.adobe.com)
* CSS Validator - [CSS Portal](https://www.cssportal.com/css-validator/)
* HTML Validator - []
* JS Validator - [JSHint](https://jshint.com/)


