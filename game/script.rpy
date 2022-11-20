# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aether", color = "#d4af37")
define p = Character("Paimon", color = "#d4af37")
define k = Character("Klee", color = "#d4af37")
define z = Character("Zhong Li", color = "#d4af37")
define d = Character("Diluc", color = "#d4af37")

define trash = 0

# GARBAGES -----------------------------------------------------------------
image trashresized1 = im.FactorScale("images/trash.png", 0.3)
screen garbage1:
    imagebutton:
        xalign 0.83 # change this
        yalign 0.80 # change this
        idle "trashresized1"
        hover "trashresized1"
        action [Hide("garbage1"), SetVariable("trash",trash+1)]

image trashresized2 = im.FactorScale("images/trash.png", 0.2)
screen garbage2:
    imagebutton:
        xalign 0.23 # change this
        yalign 0.60 # change this
        idle "trashresized2"
        hover "trashresized2"
        action [Hide("garbage2"), SetVariable("trash",trash+1)]

image trashresized3 = im.FactorScale("images/trash.png", 0.4)
screen garbage3:
    imagebutton:
        xalign 0.13 # change this
        yalign 0.99 # change this
        idle "trashresized3"
        hover "trashresized3"
        action [Hide("garbage3"), SetVariable("trash",trash+1)]

image trashresized4 = im.FactorScale("images/2trash.png", 0.04)
screen garbage4:
    imagebutton:
        xalign 0.23 # change this
        yalign 0.80 # change this
        idle "trashresized4"
        hover "trashresized4"
        action [Hide("garbage4"), SetVariable("trash",trash+1)]

image trashresized5 = im.FactorScale("images/2trash.png", 0.02)
screen garbage5:
    imagebutton:
        xalign 0.63 # change this
        yalign 0.80 # change this
        idle "trashresized5"
        hover "trashresized5"
        action [Hide("garbage5"), SetVariable("trash",trash+1)]

image trashresized6 = im.FactorScale("images/2trash.png", 0.04)
screen garbage6:
    imagebutton:
        xalign 0.63 # change this
        yalign 0.70 # change this
        idle "trashresized6"
        hover "trashresized6"
        action [Hide("garbage6"), SetVariable("trash",trash+1)]

image trashresized7 = im.FactorScale("images/3trash.png", 0.04)
screen garbage7:
    imagebutton:
        xalign 0.53 # change this
        yalign 0.80 # change this
        idle "trashresized7"
        hover "trashresized7"
        action [Hide("garbage7"), SetVariable("trash",trash+1)]

image trashresized8 = im.FactorScale("images/3trash.png", 0.08)
screen garbage8:
    imagebutton:
        xalign 0.93 # change this
        yalign 0.99 # change this
        idle "trashresized8"
        hover "trashresized8"
        action [Hide("garbage8"), SetVariable("trash",trash+1)]

image trashresized9 = im.FactorScale("images/3trash.png", 0.03)
screen garbage9:
    imagebutton:
        xalign 0.23 # change this
        yalign 0.80 # change this
        idle "trashresized9"
        hover "trashresized9"
        action [Hide("garbage9"), SetVariable("trash",trash+1)]







# FOOD SELECTION ------------------------------------------------------------
image food1resized = im.FactorScale("images/food1.png", 0.05)
screen food1:
    imagebutton:
        xalign 0.49
        yalign 0.64
        idle "food1resized"
        hover "food1resized"
        action Hide("food1")

image food2resized = im.FactorScale("images/food2.png", 0.04)
screen food2:
    imagebutton:
        xalign 0.63
        yalign 0.60
        idle "food2resized"
        hover "food2resized"
        action Hide("food2")

image food3resized = im.FactorScale("images/food3.png", 0.04)
screen food3:
    imagebutton:
        xalign 0.60
        yalign 0.62
        idle "food3resized"
        hover "food3resized"
        action Hide("food3")

image food4resized = im.FactorScale("images/food4.png", 0.05)
screen food4:
    imagebutton:
        xalign 0.445
        yalign 0.66
        idle "food4resized"
        hover "food4resized"
        action Hide("food4")

image food5resized = im.FactorScale("images/food2.png", 0.05)
screen food5:
    imagebutton:
        xalign 0.35
        yalign 0.67
        idle "food5resized"
        hover "food5resized"
        action Hide("food5")

image foodcrateresized = im.FactorScale("images/foodcrate.png", 0.9)
screen foodcrate:
    imagebutton:
        xalign 0.7
        yalign 0.55
        idle "foodcrateresized"
        hover "foodcrateresized"
        action [Hide("food1"), Hide("food2"), Hide("food3"), Hide("food4"), Hide("food5"), Hide("foodcrate"), Hide("done"), Jump('greedy')]

screen done:
    textbutton "Done": # might want to make the Done button less ugly
        action [Hide("food1"), Hide("food2"), Hide("food3"), Hide("food4"), Hide("food5"), Hide("foodcrate"), Hide("done"), Jump('nongreedy')]
        at transform:
            align(0.9, 0.1)
    #imagebutton:
    #    xalign 0.9
    #    yalign 0.1
    #    idle "done_button"
    #    hover "done_button"
    #    action [Hide("food1"), Hide("food2"), Hide("food3"), Hide("food4"), Hide("foodcrate"), Hide("done"), Jump('nongreedy')]
# FOOD ------------------------------------------------------------

# The game starts here.

label start:
    scene beach
    show screen garbage1
    show screen garbage4
    show screen garbage7

    play music "audio/beachost.mp3"

    show aether at left with dissolve

    "{i}Aether wakes up confused near the Liyue beach. Paimon appears from his backpack, all excited.{/i}"

    hide aether
    show paimon at right with dissolve

    voice "audio/yourefinallyawake.mp3"

    p "Aether, you’re finally awake! You’ve been sleeping for over 10 years bruh!"

    hide paimon

    a "{i}(What’s a br... bruh? What did she just say?){/i}"

    voice "audio/nocap.mp3"
    show paimon at right with dissolve

    p "Yeah, {i}no cap{/i}, don’t you remember what happened?"

    hide paimon
    show aether at left with dissolve

    a "What? Whose cap? No, where’s my sister?"

    voice "audio/simp.mp3"
    hide aether
    show paimon at right with dissolve

    p "...10-year coma and this guy is still a massive {i}simp-{/i}{w=3.8}{nw}"

    hide paimon
    show aether at left with dissolve

    a "What? Just shut up and bring me to a restaurant, I’m hungry."

    voice "audio/bussin.mp3"
    hide aether
    show paimon at right with dissolve

    p "Oh {i}bet{/i}, there’s some {i}bussin-{/i}{w=2.3}{nw}"

    hide paimon
    show aether at left
    with dissolve

    a "YOU KNOW, GRILLED PAIMON DOESN’T EVER MAKE ANY SOUND."

    voice "audio/wdym.mp3"

    hide aether
    show paimon at right

    p "What do you mean?"

    hide paimon
    show aether at left

    a "..."

    voice "audio/wdymbythat.mp3"

    hide aether
    show paimon at right

    p "What do you mean by that?"
    hide screen garbage1
    hide screen garbage4
    hide screen garbage7
    jump scene2

label scene2:
    scene liyue
    play music "audio/liyue.mp3" fadeout 1.0 fadein 1.0
    show screen garbage2
    show screen garbage5
    
    "{i}Aether walks to Liyue.{/i}"

    show aether at left with dissolve

    a "What’s going on? Why is everyone speaking a foreign dialect around here? What’s this putrid smell?"

    voice "audio/cantsmell.mp3"

    hide aether
    show paimonmask at right with dissolve

    p "{i}(Suddenly with a radioactive mask){/i} Can’t smell anything."

    hide paimonmask
    show aether at left with dissolve

    a "Thank you for your input, Paimon."
    "{i}Aether walks up to an older looking man.{/i}"
    a "Hey there, do you have any idea what’s going on around here?"

    voice "audio/youngin.mp3"

    hide aether
    show zhongli at right with dissolve

    z "Woah there, a normal young fella’! Oh boy, I’ve been working for so long and alone, I completely lost touch with the youngins of today!"
    
    hide zhongli
    show aether at left with dissolve
    
    a "Would you happen to know where my sister is?"

    hide aether
    show paimonmask at right
    voice "audio/paimonwhat.mp3"

    p "What"
    
    hide paimonmask
    show zhongli at right
    voice "audio/what.mp3"

    z "What"

    hide zhongli
    show aether at left

    a "What"

    voice "audio/akinator.mp3"

    hide aether
    show zhongli at right with dissolve

    z "Look, I ain’t the Akinator- but I can make something work for you. I have this project I can’t figure out for the heck of me."
    
    hide zhongli
    show aether at left with dissolve
    
    a "Sure, I’ll do anything if that means I can find my sister!"

    hide aether
    show paimonmask at right

    p "..."

    hide paimonmask
    show zhongli at right

    z "..."

    hide zhongli
    show aether at left

    a "What"

    voice "audio/iworkforloadboard123.mp3"

    hide aether
    show zhongli at right with dissolve

    z "Anyway, I work for 123Loadboard, and there’s this trucking path I can’t solve for maximum efficiency-"

    hide zhongli
    show aether at left
    show paimonmask at right

    "{i}Aether looks at Paimon, a bit worried.{/i}"

    hide aether
    hide paimonmask
    show zhongli at right with dissolve
    voice "audio/shipmentdelivered.mp3"

    z "This shipment must be delivered within the next 48 hours to CN’s freights. Please log in to ServiceNow using 1Pass-{nw}"

    menu:
        z "This shipment must be delivered within the next 48 hours to CN’s freights. Please log in to ServiceNow using 1Pass-{fast}"
        
        "WHAT are you on about old man. Let me-":

            hide zhongli
            show aether at left
            with dissolve

            a "WHAT are you on about old man. Let me-"

            hide aether
        
        "So the answer would obviously be...":

            hide zhongli
            show aether at left
            with dissolve

            a "So the answer would obviously be..."

            hide aether
    
    voice "audio/holdonbuddy.mp3"
    
    show zhongli at right
    with dissolve

    z "Hold on buddy, I didn’t even finish my question. You have exactly 3 days to write an algorithm allowing to create a solution to solve a common pain point experienced by carriers or brokers.{w=8.0}{nw}"

    voice sustain

    z "A carrier is a trucker that moves loads of merchandise from point A to point B. A broker posts loads they need delivered on load boards to try to get their loads hauled by a carrier.{w=0.5}{nw}"
    
    voice sustain

    z "A pain point is a common issue or problem faced by carriers and brokers that makes their jobs more difficult. Your solution must solve a valid carrier or broker pain point.{w=0.5}{nw}"
    
    voice sustain
    
    z "If you choose to solve a pain point that is not listed below, you must provide a short description of the pain point that justifies it as valid. There are no constraints for language, environment or database.{w=0.5}{nw}"  
    
    voice sustain
    
    z "You can use the cloud or run your solution directly on any machine you like.{w=0.5}{nw}"
    
    voice sustain
    
    z "Your presentation will include your overall architecture, a description of the code/algorithms, and a demo of your solution. You may use randomly generated data for your demo.{w=0.5}{nw}"
    
    voice sustain
    
    z "The judges will deliberate using the following criteria: Effectiveness of your solution to solve the chosen pain point, Technical difficulty of the solution, And originality and creativity of the solution."

    voice "audio/glossary.mp3"

    z "Would you like me to define each term in the Glossary?"
    
    menu:
        z "{fast}"
        "Nah, I got this.":

            hide zhongli
            show aether at left

            a "Nah, I got this."

            hide aether
            hide screen garbage2
            hide screen garbage5
            jump scene3

        "I was just about to ask that.":

            hide zhongli
            show aether at left

            a "I was just about to ask that."

            hide aether
            hide screen garbage2
            hide screen garbage5
            jump scene2_repeat

        "Please god no just shut up, let me go.":

            hide zhongli
            show aether at left
            
            a "Please god no just shut up, let me go."

            hide aether
            jump scene2_response    

label scene2_repeat:
    show zhongli at right with dissolve
    scene glossaryscene
    show zhongli at right with dissolve
    voice "audio/glossarylong.mp3"

    z "Load/Freight	Goods that are transported from one location to another. Shipper An individual or company that has a load/freight that needs to be shipped. Freight Broker An individual or company that works on behalf of the shipper to transport...{w=8}{nw}"

    scene liyue
    voice "audio/repeat.mp3"
    show zhongli at right with dissolve

    z "Would you like me to repeat?"

    hide zhongli
    show paimon at right

    p "*Snoring*{nw}"

    menu:
        p "*Snoring*{fast}"

        "Sorry, was that English?":
            hide paimon
            show aether at left with dissolve

            a "Sorry, was that English?"

            hide aether

            jump scene2_repeat

        "Easiest project of my life":
            hide paimon
            show aether at left

            a "Easiest project of my life"

            hide aether
            jump scene2_response_2

label scene2_response_2:
    voice "audio/goodluck.mp3"

    show zhongli at right
    with dissolve

    z "Alright, good luck then! I’m not sure if the bar is open, but you can text Diluc on discord on the server if the door’s locked!"
    
    hide zhongli
    show aether at left
    with dissolve

    a "Oh yeah, definitely, for sure! {i}(Diluc? Discord? Server?){/i}"

    hide aether
    hide screen garbage2
    hide screen garbage5
    jump scene3    
     
label scene2_response:
    show aether at left
    with dissolve

    a "{i}(Sadly walking down the street...){/i} Sigh… I can't connect with anyone here, and the only reasonable person was a crazy old man. Is there really no hope?"
    
    hide aether
    voice "audio/paimonthinks.mp3"
    show paimon at right
    with dissolve

    p "Paimon thinks that you should-"

    hide paimon

    "{i}Stomach growls{/i}"

    show paimon at right
    with dissolve
    voice "audio/gogetsomefood.mp3"

    p "...go get some food."

    hide paimon
    hide screen garbage2
    hide screen garbage5
    jump scene3

label scene3:
    scene bar
    play music "audio/tavern.mp3" fadeout 1.0 fadein 1.0
    show screen garbage3
    show screen garbage8

    "{i}Aether enters the bar, and sees a table full of food.{/i}"

    voice "audio/forfree.mp3"
    show paimon at right
    with dissolve

    p "{i}(to Diluc){/i} The old man says we can have anything we want here for free!"

    hide paimon
    voice "audio/goahead.mp3"
    show dilucbar at right
    with dissolve

    d "Oh Zhongli? Sure, go ahead!"
    
    hide dilucbar

    "{i}Aether salivates{/i}"

    voice "audio/feast.mp3"
    show paimon at right
    with dissolve

    p "Yummm! It's time to feast!"

    hide paimon
    hide screen garbage3
    hide screen garbage8
    # TABLE SELECTION
    scene foodtable
    
    show screen foodcrate
    show screen food1
    show screen food2
    show screen food3
    show screen food4
    show screen food5

    call screen done

    jump scene3
      
label greedy:
    voice "audio/greedybastard.mp3"
    show diluc at right

    d "??? Get out of my bar. Greedy bastard"

    hide diluc
    scene black with dissolve

    "{i}Please be mindful that snacks and drinks are limited. I have received multiple reports that specific individuals attempted to take entire crates of snacks and drinks from the bar, leaving less for the other patrons. Try again?{/i}"

    jump scene3

label nongreedy:
    show klee at right
    with dissolve
    voice "audio/lalala.mp3"

    k "la la, la la laaa~"

    hide klee
    show aether at left
    with dissolve

    "{i}Aether looks around, and notices Klee carelessly throw trash at a garbage bin specifically labelled \"USED MASKS ONLY, DO NOT PUT GARBAGE THANK YOU\"{/i}"
    "{i}Aether notices, and frowns{/i}"

    show screen garbage9

    hide aether
    show klee at right
    with dissolve
    voice "audio/cutie.mp3"

    k "{i}(Seeing him){/i} Hey it’s the traveler! Lumine’s told me lots about you noooo cap! She’s a cutie for real for re-{nw}"

    menu:
        k "{i}(Seeing him){/i} Hey it’s the traveler! Lumine’s told me lots about you noooo cap! She’s a cutie for real for re-{fast}"
        "Interrupt her about littering.":
            show aether at left
            with dissolve

            a "Klee, first of all, please don’t talk like that, it’s not good for your… brain. Second of all, I know you can read. What’s written right here? This is not okay."
            hide aether
            show klee at right
            voice "audio/sorry.mp3"

            k "I’m sorry, I won’t do it again. On g- I promise."

            hide klee
            show aether at left

            a "{i}(Walking outside){/i} Another day, another victory. Wait, what was I doing here again?"

            voice "audio/childinbar.mp3"
            hide aether
            show paimon at right

            p "Wait, and you didn’t address the fact that she was a child in a bar?"

            hide paimon

        "Interrupt her about his sister.":
            show aether at left
            with dissolve

            a "Klee, first of all, please don’t talk like that, it’s not good for your… brain. Second of all, did you just mention Lumine? Where is she, is she okay?"
            
            hide aether
            show klee at right
            voice "audio/sumeru.mp3"

            k "it was a really long time ago though, I think she went up north, all the way to Sumeru. Lucky you! The road-trip is super fun!"
            
            hide klee
            show aether at left

            a "{i}(to Paimon){/i} Paimon, Paimon, how do we get to Sumeru? We need to leave now!"
            
            voice "audio/paimonthinkfastestway.mp3"
            hide aether
            show paimon at right

            p "Paimon thinks the fastest way would be with a CN train planned by 123loadboard-"
            
            hide paimon
            show aether at left
            
            a "Damn it."

            hide aether
            hide screen garbage9

    play music "audio/ending.mp3" fadeout 1.0 fadein 1.0

    if (trash == 0):
        scene trash0
        $ renpy.pause(10.0)
    elif (trash == 1):
        scene trash1
        $ renpy.pause(10.0)
    elif (trash == 2):
        scene trash2
        $ renpy.pause(10.0)
    elif (trash == 3):
        scene trash3
        $ renpy.pause(10.0)
    elif (trash == 4):
        scene trash4
        $ renpy.pause(10.0)
    elif (trash == 5):
        scene trash5
        $ renpy.pause(10.0)
    elif (trash == 6):
        scene trash6
        $ renpy.pause(10.0)
    elif (trash == 7):
        scene trash7
        $ renpy.pause(10.0)
    elif (trash == 8):
        scene trash8
        $ renpy.pause(10.0)
    else:
        scene trash9
        $ renpy.pause(10.0)    

return