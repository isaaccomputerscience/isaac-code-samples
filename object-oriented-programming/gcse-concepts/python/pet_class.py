# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_oop_concepts

import random

class Pet:
    """Defines a pet in a children's game"""
    def __init__(self, given_name, given_type, given_colour):
        self.name = given_name
        self.type = given_type
        self.colour = given_colour
        all_moods = ["playful", "hungry", "sleepy"]
        self.mood = random.choice(all_moods)
        self.sleeping = False

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_colour(self):
        return self.colour

    def get_mood(self):
        return self.mood

    def is_sleeping(self):
        return self.sleeping

    def describe(self):
        print(f"I am a {self.mood}, {self.colour} {self.type} called {self.name}")

    def set_name(self, new_name):
        self.name = new_name

    def set_type(self, new_type):
        self.type = new_type

    def set_colour(self, new_colour):
        self.colour = new_colour

    def play(self):
       if self.sleeping == True:
           print("Zzzzzzz. I am sleeping")
       elif self.mood == "hungry":
           print("I am too hungry to play")
       elif self.mood == "tired":
           print("I am too tired to play")
       else:
           print("This is fun, I love playing")
           all_moods = ["playful", "hungry", "sleepy"]
           self.mood = random.choice(all_moods)

    def feed(self):
        if self.sleeping == True:
           print("Zzzzzzz. I am sleeping")
        if self.mood == "tired":
            print("I am too sleepy to eat anything now")
        elif self.mood == "playful":
            print("I am not hungry - I want to play")
        else:
            print("Yum - yum - that tastes great")
            self.mood = "playful"

    def sleep(self):
        if self.mood == "playful":
            print("I am too playful to sleep")
        elif self.mood == "hungry":
            print("I need something to eat before I can go to sleep")
        else:
            print("Zzzzzzzz")
            self.sleeping = True

    def wake(self):
        if self.sleeping == False:
           print("I wasn't even asleep!")
        else:
            print("I am awake and ready to play!")
            self.sleeping = False
            self.mood = "playful"


