# import utils.calculate as calc
from .class_trait import aibot
import copy

#   Bath:          +2 Joy
def bath(ai):
    ai.joy += 2
    if (ai.joy) or (ai.misery) or (ai.passion) or (ai.doubt) > 5:
        ai.mood = "Emotional Shutdown"
    else:
        calc.mood_calculate(ai)

#   Food:          +2 Joy, +1 Doubt
def food(ai):
    ai.joy += 2
    ai.doubt += 1
    if (ai.joy) or (ai.misery) or (ai.passion) or (ai.doubt) > 5:
        ai.mood = "Emotional Shutdown"
    else:
        calc.mood_calculate(ai)
        
#   Cat:           +1 Joy, +1 Passion  ### CAKE DOESN'T EXIST, IT'S A CAT IN GAME.
def cat(ai):
    ai.joy += 1
    ai.passion += 1
    if (ai.joy) or (ai.misery) or (ai.passion) or (ai.doubt) > 5:
        ai.mood = "Emotional Shutdown"
    else:
        calc.mood_calculate(ai)

#   Nature:        +2 Passion
def nature(ai):
    ai.passion += 2
    if (ai.joy) or (ai.misery) or (ai.passion) or (ai.doubt) > 5:
        ai.mood = "Emotional Shutdown"
    else:
        calc.mood_calculate(ai)

#   Hangover Poo:  +1 Misery, +2 Doubt
def hangover(ai):
    ai.misery += 1
    ai.doubt += 2
    if (ai.joy) or (ai.misery) or (ai.passion) or (ai.doubt) > 5:
        ai.mood = "Emotional Shutdown"
    else:
        calc.mood_calculate(ai)

#   Rain:          +1 Misery 
def rain(ai):
    ai.misery += 1
    if (ai.joy) or (ai.misery) or (ai.passion) or (ai.doubt) > 5:
        ai.mood = "Emotional Shutdown"
    else:
        calc.mood_calculate(ai)

#   Death:         +3 Misery
def death(ai):
    ai.misery += 3
    if (ai.joy) or (ai.misery) or (ai.passion) or (ai.doubt) > 5:
        ai.mood = "Emotional Shutdown"
    else:
        calc.mood_calculate(ai)

#   Stress:        +3 Doubt
def stress(ai):
    ai.doubt += 3
    if (ai.joy) or (ai.misery) or (ai.passion) or (ai.doubt) > 5:
        ai.mood = "Emotional Shutdown"
    else:
        calc.mood_calculate(ai)