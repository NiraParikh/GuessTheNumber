#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 0
win = False

print("Guess a number between 1 & 10: ")
while not win:
    guess = int(input())
    tries = tries + 1
    if guess == number:
        win = True
    elif guess < number:
        print("Guess higher...")
    elif guess > number:
        print("Guess Lower...")
if win:
    print("You got the Number!")
    print("Number of tries: " + str(tries) + " ")


