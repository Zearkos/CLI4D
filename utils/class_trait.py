#from .calculate import mood_calculate
#  Defining the Mood attributes from CLI4D
class aibot:
    def __init__(self, joy, misery, passion, doubt):
        self.joy = joy
        self.misery = misery
        self.passion = passion
        self.doubt = doubt
        self.joy_misery = ""
        self.passion_doubt = ""
        self.net1 = int(0)
        self.net2 = int(0)
        self.mood = ""

