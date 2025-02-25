from .class_trait import aibot

def shutdown_check(bot):
    traits = [bot.joy, bot.misery, bot.passion, bot.doubt]
    for trait in traits:
        if trait > int(5):
            bot.mood = "Shutdown"
            bot.joy = int(0)
            bot.misery = int(0)
            bot.passion = int(0)
            bot.doubt = int(0)
        # else:
        #     net_traits(bot)
        #     mood_calculate(bot)

#   Bath:          +2 Joy
def bath(ai):
    ai.joy += 2
    shutdown_check(ai)

#   Food:          +2 Joy, +1 Doubt
def food(ai):
    ai.joy += 2
    ai.doubt += 1
    shutdown_check(ai)
        
#   Cat:           +1 Joy, +1 Passion  ### CAKE DOESN'T EXIST, IT'S A CAT IN GAME.
def cat(ai):
    ai.joy += 1
    ai.passion += 1
    shutdown_check(ai)

#   Nature:        +2 Passion
def nature(ai):
    ai.passion += 2
    shutdown_check(ai)

#   Hangover Poo:  +1 Misery, +2 Doubt
def hangover(ai):
    ai.misery += 1
    ai.doubt += 2
    shutdown_check(ai)

#   Rain:          +1 Misery 
def rain(ai):
    ai.misery += 1
    shutdown_check(ai)

#   Death:         +3 Misery
def death(ai):
    ai.misery += 3
    shutdown_check(ai)

#   Stress:        +3 Doubt
def stress(ai):
    ai.doubt += 3
    shutdown_check(ai)

