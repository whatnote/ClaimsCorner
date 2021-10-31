![Picture of deployed project ]https://github.com/whatnote/ClaimsCorner/blob/main/writeUpFilePictures/screenMockUp/claimsCorner.png)

# [Claims Corner]https://github.com/whatnote/ClaimsCorner) - Milestone Project Three

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
  - [Media](#Media)
    - [Pictures](#Pictures)
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

The styling borrowed from the company I currenntly work for, Anthony Jones Insurance Brokers. [Anthony Jones Insurance Brokers ](https://www.anthonyjones.com/make-a-motor-claim/) the main feature being the "Anthony Jones' Blue". I've then triued to keep things as minimal as possible to hold 

### Wireframes

![Desktop Home Screen ](https://github.com/whatnote/ms2historybeforeorafter/blob/master/assets/wireframes/Desktop%20Home%20Screen.png)

## Features

### Existing-Features

- Deal button
- Deals 10 cards at random from a deck of 42 cards.
- Each card contains:
  - A name of event
  - A Picture of the event.
  - Year of Event
  - A more info button on each card, provides a short paragraph about the historical event.
  - In addition to the more info card a link to a website describes the event in even more detail.
- A Score bored
- Compare your score against a benchmark of score
- Add card - a separate page that allows users to suggest a new card to be added to teh deck.

### Game-Controls

- home screen - this expains the game and how to play it.
- A Play Button - Stars the game.
- A Before of After button - These are your game controlers, pick the correct asswer and you'll score a point.
- A scoreboard - Points are logged here.
- A more info button - on the reveal card addation infomation is available about the event.
- A link for additional information - If you want to read even more about the subject this will take you to a link.
- A play again button - Take yuou back to the start of the game.

### Features-Left-To-Implement

- I want levels of difficulty.
  - Hard
  - Medium
  - Easy

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

- I want a play button.
  ![Desktop Home Screen ](https://github.com/whatnote/ms2historybeforeorafter/blob/master/assets/wireframes/Desktop%20Home%20Screen.png)

- I want a large deck of cards.

The deck consists of 42 cards, more can be added with the add card page.

- I’d prefer not to have war events.

No War events included.

- I want the draw to be random.

Using the math function the array is shuffled at random at the start of every game.

![JS math](https://github.com/whatnote/ms2historybeforeorafter/blob/master/assets/WriteUpPics/shuffle.png)

- I want short snappy game, no more than 10 cards in normal mode.

Game in completed in 10 moves.

- I want more than just the year of the event, more info and more information.
  ![More Info button](https://github.com/whatnote/ms2historybeforeorafter/blob/master/assets/WriteUpPics/moreInfo.png)

- I want a play again button.

Play again button.

- I want a scoreboard.

Scoreboard at the top of the page shows the current score

- I want to be able to request a new card is added to the deck.

![New Card](https://github.com/whatnote/ms2historybeforeorafter/blob/master/assets/WriteUpPics/addCard.png)

### Responsive-Testing

The wibesite was set up as a mbile first wesite, the game type meant that hte cards only had to be above and below each other to work on mobile.

#### Web Browser and DEvice Testing

![Web Browser and DEvices Testing](https://github.com/whatnote/ms2historybeforeorafter/blob/master/assets/WriteUpPics/devices%20and%20webbrowser%20tests.png)

### Additional-Testing

#### Add Card Form.

To test the add card form I went to the card form and loaded my deatils.

I entered my details pressed send and then checked my email for the message.

![EmailJS Test](https://github.com/whatnote/ms2historybeforeorafter/blob/master/assets/WriteUpPics/emailJStest.png)

### HTML-And-CSS-Validation

I used the website, https://validator.w3.org/#validate_by_input, to check my html code, when testing 4 minor errors were noted. 2 of them were not closed a /div once that was closed 2 errors were resolved. The other two erros were generated by a some id being used twiced, once this was resolved all the errors were gone.

![Image of html test](assets/testing/html-test.jpg)

I used the website. https://jigsaw.w3.org/css-validator/, to check the code for my CSS, fortunatley it showed no errors.
![Image of css test](assets/testing/css-test.jpg)

### Interesting-Bugs-Or-Problems

Not a bug as such, but something that took me far too long to work out! It was getting the card below/right of the question top/left to display as the second card in the array, it was a very easy fix in the end, I should have asked somebody...

Simply all I had to do was change count to count++ and that as that.

## Deployment

Gitpod was used to devleoped the site, with progress being comitted to git via the terminal.

### Deployment of Page

- Log onto GitHub
- Go to the “repositories” section
- Click: ms2historybeforeorafter
- Click on "settings" located in the right handside, sort of in the middle of the screen.
- Click on “Pages” on the left handside menu
- Under “Source”, select “Master” in the first tab
- In the next tab, select “/root” if not already selected by default
- Click “Save” and the url should be displayed above the "source" section
- Now that the link is displayed, the website is deployed and can be accessed in the browser by clicking on the url

### Repository Link

To run the game in a live environment [click here](https://whatnote.github.io/ms2historybeforeorafter/)

The link to my repository can be found via this link:
[Link to Repository](https://github.com/whatnote/ms2historybeforeorafter)

### Running-Code-Locally

- Navigate to the GitHub Repository
- Click the Code drop down menu.
- Click the clipboard icon to copy the URL provided
- Open your preferred development editor the open a terminal window in a directory you like.
- Use "git clone" and paste the copied URL after it.
- A clone of the project will be created locally on your machine.

### Credits

### Content

- Most of the code was written by me, where it's not I've commented the url by the borrowed section of code.

- As mentioned above I did find an Udemy course, that showed you how to make a high lower claim game using JavaScript. I found this invaluable as it showed you how to construct many of the elements needed to make the game.

* In particular:

  - The shuffle
  - Scoring system
  - Number of turns.

  A link to this course can be found [here](https://www.udemy.com/course/javascript-card-game/).

- The game is clearly not an oringal idea but I would like to think my twist on it using historical events is.

### Media

#### Pictures

### Acknowledgements

A special thanks to my Mentor Spencer Barriball for his guidance in the project. I also need to thank my partner Chrissy and my Daughter Abbey-Rae for allowing me a great many hours in front of the computer.

### Disclaimer

This is an education only project.
