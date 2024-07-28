import random
import pygame
from pydantic import BaseModel

class Main(BaseModel):

    def __init__(self):
        pass

    # Loading the dictionary to randomly pick the answer
    def load_dict(self, file_name):
        file = open(file_name)
        words = file.readlines()
        file.close()
        return [word[:5].upper() for word in words]
    




obj = Main()

#def check_word(word, guess):
DICT_GUESSES = obj.load_dict("dict_english.txt")
DICT_ANSWERS = obj.load_dict("wordle-answers.txt")
ANSWER = random.choice(DICT_ANSWERS)
print(f'The Answer is {ANSWER}')