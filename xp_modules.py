from .Mood import trait, mood_calculate

#   Bath:          +2 Joy
def bath():
    global trait
    trait.joy += 2
    if (trait.joy) or (trait.misery) or (trait.passion) or (trait.doubt) > 5:
        mood_final = "Emotional Shutdown"
    else:
        mood_calculate()

#   Food:          +2 Joy, +1 Doubt
def food():
    global trait
    trait.joy += 2
    trait.doubt += 1
    if (trait.joy) or (trait.misery) or (trait.passion) or (trait.doubt) > 5:
        mood_final = "Emotional Shutdown"
    else:
        mood_calculate()
        
#   Cat:           +1 Joy, +1 Passion  ### CAKE DOESN'T EXIST, IT'S A CAT IN GAME.
def cat():
    global trait
    trait.joy += 1
    trait.passion += 1
    if (trait.joy) or (trait.misery) or (trait.passion) or (trait.doubt) > 5:
        mood_final = "Emotional Shutdown"
    else:
        mood_calculate()

#   Nature:        +2 Passion
def nature():
    global trait
    trait.passion += 2
    if (trait.joy) or (trait.misery) or (trait.passion) or (trait.doubt) > 5:
        mood_final = "Emotional Shutdown"
    else:
        mood_calculate()

#   Hangover Poo:  +1 Misery, +2 Doubt
def hangover():
    global trait
    trait.misery += 1
    trait.doubt += 2
    if (trait.joy) or (trait.misery) or (trait.passion) or (trait.doubt) > 5:
        mood_final = "Emotional Shutdown"
    else:
        mood_calculate()

#   Rain:          +1 Misery 
def rain():
    global trait
    trait.misery += 1
    if (trait.joy) or (trait.misery) or (trait.passion) or (trait.doubt) > 5:
        mood_final = "Emotional Shutdown"
    else:
        mood_calculate()

#   Death:         +3 Misery
def death():
    global trait
    trait.misery += 3
    if (trait.joy) or (trait.misery) or (trait.passion) or (trait.doubt) > 5:
        mood_final = "Emotional Shutdown"
    else:
        mood_calculate()

#   Stress:        +3 Doubt
def stress():
    global trait
    trait.doubt += 3
    if (trait.joy) or (trait.misery) or (trait.passion) or (trait.doubt) > 5:
        mood_final = "Emotional Shutdown"
    else:
        mood_calculate()