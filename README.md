![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Grant,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

use the code 'pip3 freeze requirements.txt'

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

<h1>Portfolio_Project_3 --- Python_Essentials</h1>
<h1>Batlleship Game!</h1>
<p>This project is a battleships game that is run and played within the terminal. The system runs on a mock terminal through <a href="https://www.heroku.com/" target="_blank">Heroku</a>
The aim of the game is to destroy the computers battleships by guessing where on a grid their battleships are and firing upon them before the computer finds and destroys all yours first.</p>

click here to play the game: <a href="-----">Battleship Game</a>
<br><br>

![image](________)

# Contents

* [**Game Rules**](<#Game-rules>)
    * [How to Play](<#How-to-play>)
* [**Features**](<#features>)
    * [Existing Features](<#Existing-Features>)
    * [Future Features](<#Future-features>)
* [**Data Model](<#Data-Model>)
* [**Testing**](<#testing>)
    * [Bugs](<#bugs>)
    * [Solved Bugs](<#solved-bugs>)
    * [Validation Testing](<#validation-testing>)
* [**Technologies Used**](<#technologies-used>)
* [**Deployment**](<#deployment>)
    * [Deployment of the project](<#deployment-of-the-project>)
    * [Cloning of the project](<#cloning-of-the-project>)
* [**Acknowledgements**](<#acknowledgements>)





# Game Rules

## How to Play
The rules to the game are very straight forward and are as follows as breifly explained above. From the outset, in this version of the game the user will be prompted for their name who will take on the computer.

The game will generate a random board with the battleships placed for both the computer and human players.

The player will be able to see their ships marked with a '$' sign on their board whilst the other board will computer's pieces will remain hidden from the human user.

Hit ships will be marked with a 'X' whilse missed targets will show a '0'

The user and the player both take turns to hit one anothers ships by taking guesses to where they are on the board by giving a grid coordanate that fits the board size.

The winner of the game is the player who wins sinks all the opposing players battleships first.

[Back to Top](<#contents>)

# Features
<hr>

## Existing Features
<!-- Look to add more content upon my creation of the game -->
Random Board Generation
<ul>
<li></li>
<li></li>
<li></li>
<br>
<img src="https:...png">
<img src="">
<br>
</ul>

    
[Back to Top](<#contents>)

### Features left to implement

<li>Have ships larger that 1 x 1 appear on the grid</li>
<li>Allow the players to select the size of the board and how many battleships there can be</li>

[Back to Top](<#contents>)

<br>

# Testing

To test my project, I have manually tested the project by doing the following:
<ul>
    <li>
        testing the programs code in <a href="http://pep8online.com/" target="_blank">pep8online</a> and confirmed that there were no errors with the code.
    </li>
    <li>
        Tested the validations to prove the program is working correctly by entering invalid inputs and checking that all error types are accounted for (outside size of board parameters, same input cannot be inputted twice and strings are not excepted)
    </li>
    <li>
        Tested in the local terminal and the Code institute Heroku Terminal
    </li>
</ul>

[Back to Top](<#contents>)

<br>

## Bugs

### Solved Bugs

<ul>
    <li>I created a validation for checking if the guess made ca be found in the guesses but I didnt pass this validation into the code for the computers turn. This showed up that the
    computer was hitting targets it has already shot and missed. resulting in an unbalanced and unfair game experience wereby the user can have a greater chance at winning then the computer</li>
    <li>........</li>
</ul>

[Back to Top](<#contents>)

<br>

### Unsolved Bugs

<p>There are no unfixed bugs found on the project.</p>

<br>

[Back to Top](<#contents>)

## Technologies Used

<li><a href="https://github.com/" target="_blank">GitHub</a> - The site was used to edit and host the website.</li>
<li><a href="https://gitpod.io/projects" target="_blank">GitPod</a> - Used in the deployment and creating the website</li>
<li><a href="" target="_blank">Python</a> - This was used in the production to get the game running in its own window as </li>
<li><a href="" target="_blank">Node.js</a> - This was used in the production to get the game running in its own window as </li>
<li><a href="http://pep8online.com/" target="_blank">pep8online</a> - This site was used to validate the python code to check for any errors within my writing.</li>
<br>

[Back to Top](<#contents>)

<br>

## Deployment

### Deployment of the project

<p> I deployed this page using GitHub pages. To deploy this project i used the following steps in GitHub:</p>
<ol>
    <li>In the GitHub repository, go to the settings tab.</li>
    <li>In the settings navigate, on the left hand drop down menu select the pages tab.</li>
    <li>On the GitHub pages tab, change the source from none to master or main(depending on what the user sees).</li>
    <li>Once selected, press save and then the page will generate a link for your new completed page.</li>
</ol>

![image](https//:.png)

<p>The link to the page can be found here - <a href="https://grantwils23.github.io/Portfolio-Project-2---JavaScript-Essentials/">LINK HERE!!!!</a></p>

<br>

[Back to Top](<#contents>)

<br>

### Cloning of the Project
<hr>
<p>To create a local clone of the project, follow the steps below:</p>
<ol>
    <li>In the GitHub repository, under the repository name there is a code tab., click on the <b>code</b> tab.</li>
    <li>In the clone tab, click the HTTPS tab. Within this section, click on the clipboard icon and copy the URL supplied for the repository.</li>
    <li>Open an IDE of your choosing and run Git Bash.</li>
    <li>Change the current working directory to the location of which you wish to place the cloned repository.</li>
    <li>In the terminal, write <b>Git Clone</b> and then paste in the URL supplied via GitHub from step 2.</li>
    <li>Press enter and your new cloned repository will be created within the desired location.</li>
</ol>

![image]()

<br>

[Back to Top](<#contents>)

<br>

## Acknowledgements

<p>This project is my 3rd Portfolio Project for the Full Stack Software Developer (e-Commerce) Diploma course provided by the <a href="https://codeinstitute.net/" target="_blank">Code Institute</a>. Here I would like to thank...</p>


[Back to Top](<#contents>)