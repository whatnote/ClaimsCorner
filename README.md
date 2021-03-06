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

### Existing Features

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
  

### Features Left To Implement

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

### Testing User Stories

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


### Additional Testing

#### Contact Form.

To Test the contact form:

Open the modal and enter the message:
![Message in Modal](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/messageInModal.jpg)

When you press send, the message disappears. 

This message is received by the developer. 
![messager to developer](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/messageReceivedTest.jpg)


This email is sent to the client. 
![Ackknowledgement to client](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/AckEmail.png)

### HTML And CSS Validation

I used the website, https://validator.w3.org/#validate_by_input, to check my html code. There are serverl erros and warning shown but all these relate to the jinja template notation so were ignored. 

![Image of html test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/htmlTest.jpg)

I used the website. https://jigsaw.w3.org/css-validator/, to check the code for my CSS, fortunatley it showed no errors.
![Image of css test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/CSSTest.jpg)

### Python Testing

I used the website PEP8 online (http://pep8online.com/checkresult) to test the python code. 
![Image of Python3 PEP8 Test test](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/testing/Python3Test.jpg)



## Deployment

Gitpod was used to devleoped the site, with progress being comitted to git via the terminal.

### Deployment of Page

Deployment the Live Version
1. Goto [github](https://github.com/)
2. look for whatnote's page [whatnote's page](https://github.com/whatnote)
3. click on the repositories [Whatnote's Repo](https://github.com/whatnote/ClaimsCorner)
4. click on Claims Corner
5. click on the link, https://claims-corner.herokuapp.com/ to the rightcentre highlighted with green. 
![Live Deployement Link:](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/Deployment/livedeployment.jpg)


To Run Local
1. Goto [github](https://github.com/)
2. look for whatnote's page [whatnote's page](https://github.com/whatnote)
3. click on the repositories [Whatnote's Repo](https://github.com/whatnote/ClaimsCorner)
4. click on Claims Corner
5. Now click on code
![Live Deployement Link:](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/Deployment/localdeployment.jpg)
6. Then click on the copy icon. 
7. open your favourite IDE, then open the CLI. 
8. Enter the command: git clone https://github.com/whatnote/ClaimsCorner.git
9. pressing enter will create a clone
10. Now jump to your mongoDB account. 
11. create a new cluster and new database name the database "claim_corner"
12. Next create the collections and fill them in like this. 

- claimForm ![claimForm](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/Deployment/claimformdb.jpg)

- liability ![liability](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/Deployment/Liabilitydb.jpg)

- users ![user](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/Deployment/usersdb.png)

13. Now create a env.py file 

enther the following code:

import os

os.environ.setdefault("IP", "value")

os.environ.setdefault("PORT", "value")

os.environ.setdefault("SECRET_KEY", "value")

os.environ.setdefault("MONGO_URI", "value")

os.environ.setdefault("MONGO_DBNAME", "value")


14. the Ip value is 0.0.0.0, the port is 5000, for secret key make up your own password or use radom key gen, noted in the technologies used. The MONGO_URI and MONGO_BDNAME are to be found in you MongoDB account. 

in the csae the mongoDB is called claim_corner



15. create a .gitignore file type, open it and ender the file name env.py

16. you can now run the program the typing python3 app.py in the CLI. 


As this is a python code running in the file you'll need to deploy it via Heroku. 
1. In the CLI create a requirements file : pip freeze --local >requirements 
2. Create a Procfile with the command : echo web: python app.py >Procfile
3. Open an heruko account. 
4. Create a new app 
  - the name needs to bu unique! 
  - choose the location nearestto you, I chose Europe and I'm based in England. 
5. Then click on the delpoy tab.
6. Claim on GitHub
7. Then connect it to your repository. 
8. Goto Setting and click on reveal config Var, 
9. Enter the details

![Config Var](https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/Deployment/config%20var.png)

  - The secret key is the one you picked. 
  - MongoDB URI is found in your MongoDB. 

10. Click on enbale Automatic Deploys and the Deploy Branch buttons; this will take a short while to work through.

11. you can then view the deloyped link.


### Repository Link

To run the game in a live environment [click here](http://claims-corner.herokuapp.com/login)

The link to my repository can be found via this link:
[Link to Repository](https://github.com/whatnote/ClaimsCorner)

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
