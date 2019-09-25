define m = Character("Me", color="#d8274a")
define u = Character("Uncle", color="#2dd728")
define p = Character("Policeman")


label start:

    scene bg main street

    "It is summertime again, vacation time. You go to your uncle's house. He takes you on a tour around the city."
    "There are many old buildings..." 

    scene bg old house

    "but the oldest of all is on Main Street." 
    "The address is 880."

    show uncle

    u "That house is haunted."

    menu:
        "Do you go inside?":
            jump go_inside
        "Do you stay there?":
            jump stay_there

label go_inside:
    m "I will go inside."
    u "I want to watch you."

    scene bg inside old house

    "You start up the stone steps of the old haunted house."
    "You open the door and step inside and suddenly a sharp arrow streaks across in front of you!" 
    "But it misses you"

    menu: 
        "Do you go up the staircase?":
            jump staircase
        "Do you go through the swinging doors?":
            jump swinging_doors

label stay_there:

    "You stay there."

    scene bg main street with fade

    "Then you decide to go home, have an ice cream, and go to bed."

    "THE END"

    return

label staircase:

    "You go up the stairs."

    scene bg black with fade

    "You lean against the railing and it breaks."
    "You fall and that's the end of you."

    "THE END"

    return

label swinging_doors:

    scene bg old room

    "You go through the swinging doors."
    "You walk through the room"

    menu:
        "Do you go into the closet?":
            jump closet

        "Do you go into a passageway under the house?":
            jump passageway

label closet:

    scene bg black with fade

    "You go into the closet."
    "You fall through a trapdoor and break your leg."
    "The walls are too smooth to climb. There is no other way up."

    "THE END"

    return

label passageway:

    "You go into a passageway under the house."
    
    scene bg main street with fade
    "You make your way along and it leads to a trapdoor that takes you back to where you started from."

    show policeman

    "You meet a policeman at the top."

    
    p "You were lucky to get out of there. Don't ever go in there again!"

    hide policeman with fade

    "You go home and have some ice cream."

    "THE END"

    return

