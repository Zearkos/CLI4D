#   Shortening the print statement, probably not needed later.
def print_mood():
    print("CLI4D should be " + mood_final)

#  Defining the Mood attributes from CLI4D
class mood:
    def __init__(self, joy, misery, passion, doubt):
        self.joy = joy
        self.misery = misery
        self.passion = passion
        self.doubt = doubt

#  Defining Net Mood attributes for FlowPath
def net_traits(): 
    global joy_misery, passion_doubt, mood_net1, mood_net2
    if mood.joy >= mood.misery:
        mood_net1 = mood.joy - mood.misery
        joy_misery = str("Joy")
    else: 
        mood_net1 = mood.misery - mood.joy
        joy_misery = str("Misery")
    if mood.passion >= mood.doubt:
        mood_net2 = mood.passion - mood.doubt
        passion_doubt = str("Passion")
    else: 
        mood_net2 = mood.doubt - mood.passion
        passion_doubt = str("Doubt")
    print("Net " + joy_misery +  " is " + str(mood_net1))
    print("Net " + passion_doubt + " is " + str(mood_net2))

def mood_calculate():
    global mood_final
    if mood_net1 == mood_net2:
        mood_final = "Bored"
    elif (mood_net1 + mood_net2) < 2:
        mood_final = "Neutral"
    elif (mood_net1 > 1) and joy_misery == "Joy":
        mood_positive()
    else:
        mood_negative()

def mood_positive():
    global mood_final
    if mood_net2 == 0:
        mood_final = "Happy"
    elif (passion_doubt == "Passion") and (mood_net2 > 1):
        mood_final = "Love"
    elif (passion_doubt == "Doubt") and (mood_net2 > 0):
        mood_final = "Shy"
    else:
        mood_final = "Anxious"

def mood_negative():
    global mood_final
    if (joy_misery == "Misery") and (mood_net1 < 1):
        mood_final = "Anxious"
    elif (mood.passion + mood.doubt) < 2:
        mood_final = "Sad"
    elif (passion_doubt == "Passion") and (mood_net2 > 1):
        mood_final = "Angry"
    elif (passion_doubt == "Doubt") and (mood_net2 > 1):
        mood_final = "Scared"
    else:
        mood_final = "Anxious"

#    Receiving inputs from user for CLI4D's mood
mood_input = input("What is CLI4D's Current Mood (separated by spaces)? ")
trait_array = mood_input.split()
mood = mood(int(trait_array[0]), int(trait_array[1]), int(trait_array[2]), int(trait_array[3]))

net_traits()
mood_calculate()
print_mood()