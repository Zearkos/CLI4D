This is intended to be a "shortest path" calculator to change the CLI4D module from one mood to another in the game "Uncle Chop's Rocket Shop".  

CLI4D is an AI Ship companion whose mood is determined by 4 different Traits (Joy, Misery, Passion, Doubt) with values of 0 to 5.
Occassionally while in the game, it is necessary to change the AI form one "mood" to another to finish the repair action on the module.  There are a total of 9 possible moods.

Based on the values of the traits, and by applying the flowpath inside the [manual](https://www.unclechops.com/_files/ugd/7849cf_4ed0ad06af324b8b9bb308825a8d23d1.pdf) on pages 55 and 56, a "mood" is determined for CLI4D.  
To change this mood, the player is able to apply "XPs" to the AI, and add to the trait values.
There are a total of 8 possible XPs, with a maximum of 4 that can be ran in one cycle.

Additionally, a state called "emotional shutdown" can occur if the value of any of the 4 traits would go above 5, OR if more than 4 sets of XPs are ran.  An emotional shutdown resets all trait values to 0.
I am intending this mood change to be done WITHOUT forcing an "emotional shutdown" and starting with a fresh slate as much as possible.

This project is planned to occur in 3 phases:
Phase 1: Replicate and proof the logic for calculating CLI4D's mood.

Phase 2: Implementing the XPs that are available to use for mood conditioning.

Phase 3: Implement a pathing solution for the most efficient path from mood A to mood B.  (Possibly BFS?)

More phases to come when I (inevitably) find out this is going to take more work than previously thought.
