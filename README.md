World of Games

project1:

play 2 games-
memory game
guess game

- The score of the games written in Score.txt
- MainScore.py is a flask application that show the score in localhost 8777
- e2e.py is testing the application whether it works or not by reading the score in the localhost.

- The Jenkinsfile build a container that running:
	python 
	MainScore.py
	e2e.py
