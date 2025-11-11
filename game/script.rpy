################################################################################
## CHARACTERS
################################################################################
## This is where you define your characters.
## Replace these examples with your own characters!
##
## To define a character:
## define character_name = Character("Display Name", color="#hexcolor")
##
## Example:
## define protagonist = Character("Alex", color="#c8ffc8")
## define villain = Character("Dr. Evil", color="#ff0000")

## Characters
define narrator = Character(None)
define cyberslime = Character("CyberSlime2077", color="#00ff00")


################################################################################
## STORY START
################################################################################
## This label is called when the game starts.
## Everything below is where your story begins!

label start:

    scene bg black
    with fade

    show cyberslime at center

    cyberslime "test dialouge, test dialouge. lmao do I realy have to say this?"

    return


################################################################################
## ADDITIONAL SCENES
################################################################################
## Add your own scenes below! Create new labels for different parts of your story.
##
## Example structure:
##
## label chapter_1:
##     scene bg bedroom
##     mc "This is chapter 1!"
##     jump chapter_2
##
## label chapter_2:
##     scene bg city
##     mc "This is chapter 2!"
##     return
##

## YOUR STORY STARTS HERE!
## Delete the examples above and write your own visual novel below:
