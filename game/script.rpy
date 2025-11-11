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

## Example characters (REPLACE THESE WITH YOUR OWN!)
define narrator = Character(None)  # For narration without a character name
define mc = Character("Protagonist", color="#c8ffc8")  # Main character
define friend = Character("Friend", color="#c8c8ff")
define mysterious = Character("???", color="#ffc8c8")


################################################################################
## STORY START
################################################################################
## This label is called when the game starts.
## Everything below is where your story begins!

label start:

    ## =========================================================================
    ## EXAMPLE SCENE 1: Basic Dialogue
    ## =========================================================================
    ## This is a simple example to show you how dialogue works.
    ## Delete or modify this for your own story!

    ## Show a background image (you'll add your own images later)
    ## scene bg room
    ## For now, we'll use a simple color background
    scene bg black
    with fade

    ## Narrator text (no character name shown)
    "Welcome to your visual novel!"

    "This is a template project to help you get started."

    ## Character dialogue
    mc "Hi! I'm the protagonist. You can change my name and dialogue in script.rpy!"

    friend "And I'm a friend character. We're just examples!"

    mc "You can add your own characters, backgrounds, music, and story here."


    ## =========================================================================
    ## EXAMPLE SCENE 2: Showing Character Sprites
    ## =========================================================================
    ## When you have character sprites, you can show them like this:
    ## show character_name expression at position
    ##
    ## For example:
    ## show mc happy at left
    ## show friend neutral at right
    ##
    ## For now, we'll skip this since you don't have sprites yet.

    narrator "When you add character sprites, you can display them on screen!"

    narrator "Place your character images in: game/images/characters/"

    narrator "And background images in: game/images/backgrounds/"


    ## =========================================================================
    ## EXAMPLE SCENE 3: Choices
    ## =========================================================================
    ## This shows how to create choices that branch the story

    mc "Let me show you how choices work!"

    menu:
        "Which path should we take?"

        "Path A - The mysterious route":
            jump path_a

        "Path B - The friendly route":
            jump path_b


## ==============================================================================
## PATH A
## ==============================================================================
label path_a:

    mysterious "You chose the mysterious path..."

    mysterious "This is where something mysterious would happen in your story!"

    mc "Interesting choice!"

    jump after_choice


## ==============================================================================
## PATH B
## ==============================================================================
label path_b:

    friend "You chose the friendly path!"

    friend "This is where something friendly would happen in your story!"

    mc "That was a nice choice!"

    jump after_choice


## ==============================================================================
## AFTER CHOICE
## ==============================================================================
label after_choice:

    narrator "Both paths lead back here. This is how you can create branching stories!"


    ## =========================================================================
    ## EXAMPLE SCENE 4: Playing Music & Sound
    ## =========================================================================
    ## To play background music:
    ## play music "audio/music/your_song.mp3" fadeout 1.0 fadein 1.0
    ##
    ## To play sound effects:
    ## play sound "audio/sfx/your_sound.ogg"
    ##
    ## To stop music:
    ## stop music fadeout 1.0

    narrator "You can add background music and sound effects too!"

    narrator "Place music files in: game/audio/music/"

    narrator "And sound effects in: game/audio/sfx/"


    ## =========================================================================
    ## EXAMPLE SCENE 5: Variables and Flags
    ## =========================================================================
    ## You can use variables to track player choices and story progress

    ## Define a variable
    $ player_score = 0
    $ player_name = "Hero"

    mc "You can use variables to remember player choices!"

    ## Modify the variable
    $ player_score += 10

    narrator "Your score is now [player_score]!"

    ## Conditional dialogue based on variables
    if player_score >= 10:
        mc "Great job! Your score is high enough!"
    else:
        mc "Keep trying to increase your score."


    ## =========================================================================
    ## END OF EXAMPLE
    ## =========================================================================

    narrator "That's the end of the example!"

    narrator "Now it's your turn to create your own visual novel!"

    narrator "Check the README.md file for instructions on:"
    narrator "- Adding your own backgrounds and character sprites"
    narrator "- Adding music and sound effects"
    narrator "- Writing your own story"
    narrator "- Building the game for distribution"

    mc "Good luck with your visual novel!"

    ## End the game
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
