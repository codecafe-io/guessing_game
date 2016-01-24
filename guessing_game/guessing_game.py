#!/usr/bin/env python
import random

__author__="codecafe-io"

'''
Simple guessing game for trying out 
number of guesses before 
reaching the answer

Python version: 3.4
'''

x = 0; count = 0
# x = int(input("Please enter a number between 1 to 20: "))
val = random.randrange(1,10)

while x != val:
    try:
        x = int(input("Please enter a number between 1 to 10: "))
    except:
        print ("Something went wrong with your input, please try again")
        continue
    if x < val:
        print ("You guessed smaller")
    elif x > val:
        print ("you guessed higher")
    count += 1
    

 
print ("Good Job, you guessed right: ", x, "and you took {0} times to guess it".format(count))
