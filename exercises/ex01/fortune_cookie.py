"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730154017"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

# Creating variable to hold the result of calling randint (msg chooser)
msg_chooser = randint(1,12)
fortune = ""

if(msg_chooser > 9):
    fortune = "Treat yourself this week!"
elif (msg_chooser > 6):
    fortune = "Good things are coming your way."
elif (msg_chooser > 3):
    fortune = "Perhaps you've been focusing too much on that one thing."
else:
    fortune = "You're going to kill your test this week."
    
print("Your fortune cookie days...")
print(fortune)
print("Now, go spread positive vibes!")