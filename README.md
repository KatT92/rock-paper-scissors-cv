# rock-paper-scissors
Rock paper scissors project

```manual_rps.py``` a manual game of rps that takes a user input from the terminal, gets a random choice from the computer and prints an outcome.

```RPS-Template.py``` is a pre-made template that takes the model from ```keras_model.h5``` and ```labels.txt``` and an incming image from the camera, and returns the probability that the image is 'rock', 'paper', 'scissors' or 'nothing'.

```camera_rps.py```
- insert text here


## Teachable-machine
I used https://teachablemachine.withgoogle.com/ to upload images of rocks, paper, scissors and nothing to train the model. The more images that were added, and the more different images, the more accurate the model got.

I downloaded conda as well as opencv-python, tensorflow, and ipykernel using pip and set up a virtual environment. I also downloaded my model ```keras_model.h5``` from teachable-machine as well as the labels from ```labels.txt``` (rock, paper, scissors, nothing) and a pre-made template ```RPS-Template```. The template takes in an image from the camera and returns the probability that the image matches each label.

- Add notes on the model/rps-template here including more detailed explanation of how it works

## Manual RPS game
I created this game using python in VSCode and running it in the terminal.

    - I made functions for the user choice, computer choice, deciding the winner and a function to start the game. the game can be started by typing ```manual_rps.py``` in the terminal.
    - For the user choice, I added an additional while statement to make sure the user input was valid, as this needs to be either 'rock', 'paper' or 'scissors' for the game to work.
    - I decided to use arrays for the user choice and computer choice, and then find the index to cut down on repetition of conditions in the if-else statements. I also added a condition in case something went wrong which has been useful for bug testing.

## camera_rps.py


