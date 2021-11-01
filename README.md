![Picture of deployed project](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/screenMockUp/claimsCorner.png)

# [Claims Corner](https://claims-corner.herokuapp.com/) - Milestone Project Three

## Table of Contents

- [**About**](#About)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Research](#Research)
  - [Styling](#Styling)
  - [Wireframes](#Wireframes)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
    - [Game Controls](#Game-Controls)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
- [**Testing**](#Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Responsive Testing](#Responsive-Testing)
  - [Additional Testing](#Additional-Testing)
  - [HTML And CSS Validation](#HTML-And-CSS-Validation)
  - [Interesting Bugs Or Problems](#Interesting-Bugs-Or-Problems)
- [**Deployment**](#Deployment)
  - [Running Code Locally](#Running-Code-Locally)
- [**Credits**](#Credits)
  - [Content](#Content)
    
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

Claims corner is a proof of concept for a claims portal to be utilised by an insurance broker connecting, the idea this will connect their client drectly to the broker, makign the reporting of claims faster and easier than just using emails. 

The benefit for the broker it give the broker a uniique selling point; the broker is more integrated with the client's infostructure, making it more difficult for them to move to another broker.

## UX

### User Stories

User stories fall into two categories. 

Client Facing 
- Client specific log on.
- Ability to report motor claims. 
- able to update details of the claim when they become available
- able to contact the broker directly if they're ubalb to log on
- able to contact the broker directly to talk about a specific claim.

Broker facing. 
- A broker specific specific login. 
- the broker needs to able to see all client's claims. 
- Able to operate a diary system.
- Able to contact the client specifically about a specific claim.


### Research

Having worked in the jandling of claim the in the insurance industry for 20 years, I've foound the claims function on every computer system I've used, simply isn't up the to the task of handling claims quicly, the adminstration can take more the 25% of you day with having to re-key data and copy and paste data. 

With this I have a wish list of what a claims system should have to enable better handling of claims and removing the need to retype or copy and paste infomation. 

The basis of the webiste is to present a one time only data entry. Once that claim os fully logged the client of claims handler has not to retype into an email again. 


### Styling

The styling is borrowed from the company I currenntly work for, Anthony Jones Insurance Brokers. [Anthony Jones Insurance Brokers ](https://www.anthonyjones.com/make-a-motor-claim/) the main feature being the "Anthony Jones' Blue". I've then tried to keep things as minimal as possible to avoid contrast issue. The color red was then used to style any button button that wasn't used to . 

The font I've used is Lato, if works well when small, making it ideal for use on phones and tablets, it also scales well. 


### Wireframes

![Mobile Home Scree](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/wireframe/MobileWireframe.png)


![Desktop Home Screen ](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/wireframe/DesktopWireframe.png)

## Features

### Existing-Features

- Register Function
- LogOn Function
- Able to Add new claims.
- Able to edit new claim
- Able to delete claims
- Search feature: 
  - able to seatch for claims via their:
    - registration
    - driver's name
    - Third party's registration
- Contact feature: Client is able to contact for assistnace via:
    - whatsapp
    - telephone
    - or via a contact form. 
  

### Features-Left-To-Implement

 - Include a MI facility, give the client a graphical presentation of their claims data.
 - Add financials of claims costs. 
 - specific login for "Admin" "Claims Handler" and "Client" at the moment the client and and broker staff member has full access to the portal.
  

## Technologies-Used

[**Trello**](https://trello.com/)

- Used to time manage the various steps in the project.

[**Balsamiq**](https://balsamiq.com/)

- Balsamiq was used to create wireframes of both the mobile and website before construction began.

[**Gitpod**](https://gitpod.io/)

- I used Gitpod to write my code.

[**Git**](https://git-scm.com/)

- I've used Git version control system to regularly add and commit changes made to project in gitpod thn pushing them to GitHub.

[**Google Fonts**](https://fonts.google.com/)

- I used google fonts to style the text.

[**Materializecss**](https://materializecss.com/)

- I've used materializecss to to assist with my layout. I've then used CSS to style same.

[**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

- HTML is used to create the landing page for my game.

[**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

- The project uses CSS to apply style to my site. The style.css is link to the index.html.

[**JavaScript**](https://www.javascript.com/)

- The main focus of this project. script.js is linked to the index.html file.

[**jQuery**](https://jquery.com)

- I use jQueryt for DOM manipulation in my project.

[**Python3**](https://www.python.org/)
- was used to program the join the frontend to the backend. 

[**Flask**](https://flask.palletsprojects.com/en/2.0.x/)

- was used as the micro framework for python3

[**Werkzeug**](https://www.palletsprojects.com/p/werkzeug/)

- Flask wraps Werkzeug, using it to handle the details of WSGI while providing more structure and patterns for defining powerful applications.

[**Jinja**](https://jinja.palletsprojects.com/en/2.11.x/)

- Jinja2 is a full-featured template engine for Python.

[**Heruko**](https://id.heroku.com/login)

- Heruko was used to host and delpoy the site 

[**MongoDB**](https://www.mongodb.com/)
- MongoDB was used as the backend database

[**Radom Key Generator**](https://randomkeygen.com/)
- Ramdom key was used to generate the necessary key to protect the database. 

## Version Control

[**Git**](https://git-scm.com/)

- Git was used to regularly commit changes made to my project.

[**GitHub**](https://github.com/)

- Is used as my Repository.

## Testing

### Testing-User-Stories

The website has the following features:

- Register Function
![register test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/RegisterTest.jpg)
- LogOn Function
![Logon test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/LogonTest.jpg)
- Able to Add new claims.
![New Claim test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/newCLaimTest.jpg)

- Able to edit claims and Delete
![Edit and Delete Claims](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/claimEditDeleteclaim.jpg)

- Search feature: 
  - able to seatch for claims via their:
    - registration
    - driver's name
    - Third party's registration
![Search ](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/searchTest.jpg)

- Contact feature: Client is able to contact for assistnace via:
    - whatsapp
    - telephone
    - or via a contact form. 

![Contact](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/contactTest.jpg)

### Responsive-Testing

The wibesite was set up as a mbile first website, the materialize classes are excelement at re-scalling withouth the need to and array of @media queries. 

#### Web Browser and Device Testing

![Web Browser and DEvices Testing](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/devices%20and%20webbrowser%20tests.png)


### Additional-Testing

#### Contact Form.

To Test the contact form:

Open the modal and enter the message:
![Message in Modal](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/messageInModal.jpg)

When you press send, the message disappears. 

This message is received by the developer. 
![messager to developer](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/messageReceivedTest.jpg)


This email is sent to the client. 
![Ackknowledgement to client](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/AckEmail.png)

### HTML-And-CSS-Validation

I used the website, https://validator.w3.org/#validate_by_input, to check my html code. There are serverl erros and warning shown but all these relate to the jinja template notation so were ignored. 

![Image of html test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/htmlTest.jpg)

I used the website. https://jigsaw.w3.org/css-validator/, to check the code for my CSS, fortunatley it showed no errors.
![Image of css test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/htmlTest.jpg)

### Python Testing

I used the website PEP8 online (http://pep8online.com/checkresult) to test the python code. 
![Image of Python3 PEP8 Test test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/Python3Test.jpg)


### Interesting-Bugs-Or-Problems



## Deployment

Gitpod was used to devleoped the site, with progress being comitted to git via the terminal.

### Deployment of Page





### Repository Link

To run the game in a live environment [click here](http://claims-corner.herokuapp.com/login)

The link to my repository can be found via this link:
[Link to Repository](https://github.com/whatnote/ClaimsCorner)

### Running-Code-Locally

- Navigate to the GitHub Repository
- Click the Code drop down menu.
- Click the clipboard icon to copy the URL provided
- Open your preferred development editor the open a terminal window in a directory you like.
- Use "git clone" and paste the copied URL after it.
- A clone of the project will be created locally on your machine.

### Content

- A lot of the code for project was lifted from the putting it all together from the [Backend Developenment course from the CODE Institute](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment), 
  Particularly the:

  -  register 
  -  logon 
  -  log off 

  we're lifted directly from the course with just minor amendments to the CSS and html. 

the claims list was mapped accross from the task list. as was the 
- new claim 
- edit and delete feature
- search 

In these particulary cases the code was amended to suite to the requirement of the user stories. 

the email connenction was lifted from the codeinstitute course. 
#### Putting it all toghter - Sending email using emailJS [link to course here](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+IFD101+2017_T3/courseware/03d3f6524ad249d9b33e3336d156dfd0/e4710f80cdf34bffbd607bc102482d5c/)


## Acknowledgements

A special thanks to my Mentor Spencer Barriball for his guidance in the project. I also need to thank my partner Chrissy and my Daughter Abbey-Rae for allowing me a great many hours in front of the computer.

### Disclaimer

This is an education only project.
