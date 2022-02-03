# rock-paper-scissors-exercise

Welcome to Rock, Paper, Scissors!
This game was developed as part of the OPIM-243 class Intro to Business App Development(Python)
at Georgetown University by Ishaan Shah (MSB'23)


## Instructions

### Starting Up

In order to to start up the game, several commands must be entered in either Terminal or GitBash(for Windows users):

After navigating to the rock-paper-scissors-exercise directory, type in the following three lines:

```sh
conda create -n my-game-env python=3.8 # (first time only)
```
```sh
conda activate my-game-env
```
```sh
pip install -r requirements.txt
```


### Playing the game

In order to play the game, simply type the following line:

```sh
python game.py
```

### Custom name

This game also has the feature of custom names. If you would like to be welcomed with a custom name,
start the game with this line in terminal (or GitBash):

```sh
PLAYER_NAME="Jon Doe" python game.py
```

### Checking

In this repository is also the feature of autochecking the program to make sure the game logic is correct throughout.
In order to run this test, enter the following line in terminal (or GitBash):

```sh
pytest
```






