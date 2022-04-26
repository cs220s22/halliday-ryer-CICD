# halliday-ryer-CICD
## Overview:
This repo contains a simple CICD demonstration.
The general purpose of this project is to square a number typed into the URL upon the 
program's creation with aid of heroku. Through Github actions, any change/pull requestion
can be run through tests using Pylint to make sure that the code to be approved for addition is,
working and will not disrupt the program whilst up. 

## Setup:
The repo is uploaded to Github, but needs to be deployed on Heroku as it is necessary to launch
the app. When deployed through Heroku, Heroku will check to make sure the requirements of the app
are installed. When all tests pass on Heroku's side: https://halliday-ryer-cicd.herokuapp.com/ will
be avaliable for use. The app can be run in the users browswer with the additon of: square/5
Square specifies the following number to be squared, the number 5 can be replaces with any valid integer. 

## Technologies used:
Within Github, Github actions.
The program tests via Pylint.
Heroku is used to deploy the app, for which an auth token is used as well. 

## Background + Links used:  
https://devcenter.heroku.com/articles/getting-started-with-python - Intro to using Heroku with python  
https://pylint.pycqa.org/en/latest/intro.html - Documentation for using Pylint  
https://docs.github.com/en/actions - Documentation for using github actions

