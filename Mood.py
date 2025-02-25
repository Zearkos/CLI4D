from utils.xp_modules import bath, food, cat, nature, hangover, rain, death, stress
from utils.class_trait import aibot

#   Prints the mood, might not be needed.
def print_mood(ai):
       print("CLI4D should be " + ai.mood)

#   The part that *Actually* calculates the mood
def mood_calculate(ai):
    if ((ai.net1 == 0) and (ai.net2 == 0)):
        ai.mood = "Bored"
    elif ((ai.net1 + ai.net2) < 2):
        ai.mood = "Neutral"
    elif ((ai.net1 > 1) and (ai.joy_misery == "Joy")): #  Broken into sub-functions otherwise it'd get messy with the if/else statements.
        mood_positive(ai) 
    else:
        mood_negative(ai)

#   Second part of the flowpath, right side.
def mood_positive(ai):
    if ai.net2 == 0:
        ai.mood = "Happy"
    elif (ai.passion_doubt == "Passion") and (ai.net2 > 1):
        ai.mood = "Love"
    elif (ai.passion_doubt == "Doubt") and (ai.net2 > 0):
        ai.mood = "Shy"
    else:
        ai.mood = "Anxious"
#   Second part of the flowpath, left side.
def mood_negative(ai):
    if (ai.joy_misery == "Misery") and (ai.net1 <= 1):
        ai.mood = "Anxious"    
    else:
        if (ai.net2 < 2):
            ai.mood = "Sad"
        elif (ai.passion_doubt == "Passion") and (ai.net2 > 1):
            ai.mood = "Angry"
        elif (ai.passion_doubt == "Doubt") and (ai.net2 > 1):
            ai.mood = "Scared"
        else:
            ai.mood = "Anxious"

    #  Defining Net Trait attributes needed for FlowPath
def net_traits(ai):
    if ai.joy >= ai.misery:
        ai.net1 = ai.joy - ai.misery
        ai.joy_misery = str("Joy")
    else: 
        ai.net1 = ai.misery - ai.joy
        ai.joy_misery = str("Misery")
        
    if ai.passion >= ai.doubt:
        ai.net2 = ai.passion - ai.doubt
        ai.passion_doubt = str("Passion")
    else: 
        ai.net2 = ai.doubt - ai.passion
        ai.passion_doubt = str("Doubt")

    # Pretty prints the net values.        
def traits_print(ai):
    print("Net " + ai.joy_misery +  " is " + str(ai.net1))
    print("Net " + ai.passion_doubt + " is " + str(ai.net2))

    # Setup for CLI4D's initial values
def setup():
    global trait_array, mood_input, aistart
    mood_input = input("What is CLI4D's Current Mood (separated by spaces)? ") #    Receiving inputs from user for CLI4D's mood
    trait_array = mood_input.split()
    aistart = aibot(int(trait_array[0]), int(trait_array[1]), int(trait_array[2]), int(trait_array[3]))
    net_traits(aistart)
    traits_print(aistart)
    mood_calculate(aistart)
    print_mood(aistart)



    ############   THIS IS WHERE THE SCRIPT ACTUALLY STARTS  ###################
setup()

#   First run of XPs
xp_list = [bath, food, cat, nature, hangover, rain, death, stress]
first_order = []
requested = input("What mood do you need? ")


for xp in xp_list:
    ai1 = aibot(int(trait_array[0]), int(trait_array[1]), int(trait_array[2]), int(trait_array[3]), f'{xp.__name__}')
    xp(ai1)
    if ai1.mood != "Shutdown":
        net_traits(ai1)
        mood_calculate(ai1)
    first_order.append(ai1)
    #
for bot in first_order:
    if (bot.mood) == (requested.capitalize()):
        print(f'PASS: Running {bot.name.upper()} will return: {bot.mood}.')
    else:
        # print('No Matches.')
        print(f'Fail: Running {bot.name.upper()} will return: {bot.mood}.')