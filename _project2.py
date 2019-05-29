#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time
import sys
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def print_stop(message):
    print(message)
    time.sleep(2)


class Player:
    score = 0
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# This is the random player
class unsystematic(Player):
    score = 0

    def learn(self, my_move, their_move):
        pass

    def move(self):
        return random.choice(moves)


class cycler(Player):
    score = 0

    def learn(self, my_move, their_move):
        pass

    def move(self):
        if self.my_move is None:
            self.my_move = "scissors"
        elif self.my_move == "scissors":
            self.my_move = "paper"
        elif self.my_move == "paper":
            self.my_move = "rock"
        elif self.my_move == "rock":
            self.my_move = "scissors"
        return self.my_move


# This is the Reflect Player
class Immitator(Player):
    score = 0

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(["rock", "paper", "scissors"])
        if self.their_move is not None:
            return self.their_move


class Human(Player):
    score = 0

    def learn(self, my_move, their_move):
        pass

    def move(self):
        while True:
            my_move = input("rock, paper or scissors?").lower()
            ending = "quit"
            if my_move in moves:
                break
            elif my_move == ending.lower():
                sys.exit()
            else:
                continue
        return my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            print("Player 1 won this round.")
            self.p1.score = self.p1.score + 1
            print("Scores:")
            print(f"Player1: {self.p1.score}    Player2: {self.p2.score}")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        elif beats(move2, move1) is True:
            print("Player 2 won this round.")
            self.p2.score = self.p2.score + 1
            print("Scores:")
            print(f"Player1: {self.p1.score}    Player2: {self.p2.score}")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        else:
            print("Its a tie. No one won.")
            print("Scores:")
            print(f"Player1: {self.p1.score}    Player2: {self.p2.score}")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    def determine_rounds(self):
        while 2 == 2:
            try:
                answer = int(input("How many rounds would you like to play?"))
                return answer
            except ValueError:
                print("Ops! thats not an integer.")

    def play_game(self):
        print("<<<Game start!>>>")
        for round in range(self.determine_rounds()):
            print(f"Round {round}:")
            self.play_round()
        print("<<<Game over!>>>")
        if self.p1.score > self.p2.score:
            print("Total scores")
            print(f"Player1: {self.p1.score}   Player2: {self.p2.score}")
            print("Player 1 WON!")
        elif self.p1.score < self.p2.score:
            print("Total scores")
            print(f"Player1: {self.p1.score}   Player2: {self.p2.score}")
            print("Player 2 WON!")
        else:
            print("Final scores")
            print(f"Player1: {self.p1.score}   Player2: {self.p2.score}")
            print("Its a tie. No one won:(")


if __name__ == '__main__':
    print_stop("Hello! You are playing a game of Rock,Paper,Scissors.")
    print_stop("Rock beats scissors. Scissors beat paper. Paper beats rock. ")
    print_stop("You are Player 1.")
    print_stop("You are going to play against a computer,"
               "so you must choose the computer's play method.")
    print_stop("Your choices will be shown below.")
    print_stop("""    1.Repeated method.
    2.Unsystematic method.
    3.Cycler method.
    4.Immitator method.""")
    while True:
        choice = input("Please choose the Computer's Play method"
                       "(repeated,unsystematic,cycler,immitator):").lower()
        if choice == "repeated":
            game = Game(Human(), Player())
            game.play_game()
            break
        elif choice == "unsystematic":
            game = Game(Human(), unsystematic())
            game.play_game()
            break
        elif choice == "cycler":
            game = Game(Human(), cycler())
            game.play_game()
            break
        elif choice == "immitator":
            game = Game(Human(), Immitator())
            game.play_game()
            break
        else:
            continue
