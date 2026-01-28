## --- HAUPT-EINGANG ZUM BAKING MINIGAME---
label baking_minigame_hub:
    scene bg kitchen 
    
    if not tutorial_baking_done:
        jump baking_recipe_selection
    else:
        jump baking_recipe_selection    


## TUTORIAL MODUS (Einheitlich)
label baking_tutorial_selection:
    user "Was backe ich zuerst?"

    $ quick_menu = False

    ## SCHRITT 1: Die Entscheidung (Nur für Story & Punkte)
    menu:
        "Lava Cake":
            $ first_li_chosen = "Lavan"
            call _add_affection(LI_LAVAN, 1)
            
        "Matcha Cookie":
            $ first_li_chosen = "Macoi"
            call _add_affection(LI_MACOI, 1)
            
        "Red Velvet Cupcake":
            $ first_li_chosen = "Velvette"
            call _add_affection(LI_VELVETTE, 1)
            
        "Zimtrolle":
            $ first_li_chosen = "Cino"
            call _add_affection(LI_CINO, 1)

    $ quick_menu = True

    ## Nach der Wahl geht es weiter zum Minigame-Start
    jump run_tutorial_minigame


## SCHRITT 2: Der Tutorial-Loop
label run_tutorial_minigame:

    ## --- MUSIK STARTEN ---
    play music "audio/Baking_Game_Music.mp3" fadein 0.5
    
    $ current_ingredients = [] # Reset des Minigames

    user "Okay, los geht's. Ich muss mich genau an das Rezept halten."

    $ quick_menu = False

    ## Wir rufen das Minigame IMMER mit dem Rezept "Tutorial" auf.
    call screen baking_minigame_screen("Tutorial", helper=None)

    $ quick_menu = True

    ## 1. ERFOLG
    if _return == "success":
        ## Wir springen direkt weiter in der Story.
        $ tutorial_baking_done = True
        jump awakening_shock_scene 
    
    ## 2. ABBRUCH
    elif _return == "cancel":
        user "Oder doch eher was anderes."
        stop music fadeout 0.5
        ## Wir springen zurück zur Auswahl
        jump baking_tutorial_selection 

    ## 3. FAIL
    else:
        stop music fadeout 0.5
        play sound "audio/Lose_Sound.mp3"
        $ quick_menu = False
        call screen fail_screen_anim()
        $ quick_menu = False
        jump run_tutorial_minigame

## NORMALER MODUS (Alltag)
label baking_recipe_selection:
    
    scene bg kitchen 
    user "Okay, was backen wir?"
    
    menu:
        user "Okay Was backen wir?"

        ## --- REZEPT 1: BUTTERPLÄTZCHEN ---
        "Butterplätzchen":
            $ current_recipe_name = "Butterplätzchen"
            jump run_baking_loop

        ## --- REZEPT 2: ERDBEER CREPE ---
        "Erdbeer Crepe":
            $ current_recipe_name = "Erdbeer Crepe"
            jump run_baking_loop
        
        # "Zurück":
        #     jump kitchen_room_interaction

## --- DER UNIVERSELLE BACK-LOOP ---
label run_baking_loop:

    ## --- MUSIK STARTEN ---
    play music "audio/Baking_Game_Music.mp3" fadein 1.5
    
    ## --- 1: AUTOMATISCHER RESET ---
    ## Damit ist die Schüssel immer leer, wenn man neu startet.
    $ current_ingredients = [] 
    
    ## --- 2: QUICK MENU AUSBLENDEN ---
    $ quick_menu = False
    
    ## 1. Wir starten das Schüssel-Minigame
    call screen baking_minigame_screen(current_recipe_name, helper=current_kitchen_helper)
    
    ## --- 2: MENÜ WIEDER ANZEIGEN ---
    $ quick_menu = True
    
    ## Wir speichern das Ergebnis zwischen
    $ minigame_result = _return
    
    ## 2. SPEZIALFALL: CREPE PHASE 2 (Mein neuer Code)
    if minigame_result == "crepe_phase_2":
        
        ## Auch hier kurz Menü ausblenden für Immersion (optional)
        $ quick_menu = False
        call crepe_pan_minigame
        $ quick_menu = True
        
        ## Das Ergebnis überschreiben wir
        $ minigame_result = _return

    ## 3. AUSWERTUNG
    if minigame_result == "success":
        ## --- SUCCESS SCREEN ---

        stop music fadeout 0.5

        play sound "audio/Win_Sound.mp3"

        if current_recipe_name == "Butterplätzchen":
            $ result_img = "images/minigame/result_butterplaetzchen.png"
        elif current_recipe_name == "Erdbeer Crepe":
            $ result_img = "images/minigame/result_crepe.png"
        else:
            $ result_img = None 

        $ quick_menu = False

        call screen success_screen_anim(result_png=result_img)

        call _add_affection(current_kitchen_helper, 2)

        $ quick_menu = True
## FÜR DICH SOFIYA, Char reaktion auf der verschiedenen gerichte. Untendrunter siehtst du ein Beispiel, mach die Kommentierung weg und wo das FETT geschriebene ist ersetzen.

        if current_recipe_name == "Butterplätzchen" and current_kitchen_helper == "Lavan":
            l "Mein Favorit."
        elif current_recipe_name == "Erdbeer Crepe" and current_kitchen_helper == "Cino":
            c "Juhu!"
        #elif current_recipe_name == "NAME DES REZEPTES" and current_kitchen_helper == "CHARAKTER":
        #    KÜRZEL DES CHARS "REAKTION"    

## BIS HIER FÜR DICH 

        # Fall A: Wir kommen aus der Story-Eröffnung (Der Tag geht weiter)
        return
            
    elif minigame_result == "cancel":
        ## ABBRUCH
        stop music fadeout 0.5
        scene bg kitchen
        user "Eher doch was anderes..."
        
        jump baking_minigame_hub
        
    else:
        ## FAIL
        stop music fadeout 0.5
        play sound "audio/Lose_Sound.mp3"
        $ quick_menu = False
        call screen fail_screen_anim()
        $ quick_menu = False
        jump run_baking_loop

## --- FINDING MINIGAME HUB ---
## Wir erwarten hier Argumente für die Bilder und Positionen
label run_finding_minigame(bg_img, idle_img, hover_img, x_pos, y_pos, scale):
    
    ## Menü ausblenden
    $ quick_menu = False

    ## START DES SPIELS
    ## Wir rufen den Screen auf und geben die Daten weiter, die wir bekommen haben
    call screen finding_game_screen(bg_img, idle_img, hover_img, x_pos, y_pos, scale)
    
    ## Menü wieder an
    $ quick_menu = True

    ## AUSWERTUNG
    if _return == "found":
        return # Zurück zur Story        

## ---------------------------------------------------------------------
## VIDEO END-SCREENS (SUCCESS & FAIL)
## ---------------------------------------------------------------------

## 1. SUCCESS SCREEN
## Zeigt das Video im Hintergrund und das übergebene Bild in der Mitte.
screen success_screen_anim(result_png=None):
    modal True
    
    ## HINTERGRUND VIDEO (Zwingt es auf Vollbild 1920x1080)
    add Movie(play="gui/minigames/Good_Job.webm", loop=True):
        size (1920, 1080)
    
    # ## DAS GEBACKENE ERGEBNIS
    # if result_png:
    #     add result_png:
    #         align (0.5, 0.5)
    #         zoom 0.6  # Größe anpassen
    #         at result_floating_anim # Die kleine Schwebe-Animation 

    ## TEXT / GLÜCKWUNSCH
    if result_png:
        text "Perfekt!" size 100 align (0.5, 0.5) outlines [(3, "#000", 0, 0)]

    ## BUTTON
    textbutton "Weiter":
        align (0.5, 0.9)
        style "choice_button"
        text_size 40
        padding (50, 10)
        action Return() # Schließt den Screen und macht im Hub weiter

## 2. FAIL SCREEN
## Zeigt das Fail-Video und Text.
screen fail_screen_anim():
    modal True
    
    ## HINTERGRUND VIDEO
    add Movie(play="gui/minigames/Try_Again.webm", loop=True):
        size (1920, 1080)
    
    ## TEXT
    vbox:
        align (0.5, 0.5)
        spacing 20
        
        text "Schade!" size 120 color "#fff" xalign 0.5:
            outlines [(5, "#000", 0, 0)] 
            bold True
            
        text "Versuch es nochmal." size 50 color "#ddd" xalign 0.5:
            outlines [(3, "#000", 0, 0)]

    ## BUTTON
    textbutton "Nochmal versuchen":
        align (0.5, 0.85)
        style "choice_button"
        text_size 40
        padding (50, 10)
        action Return() # Schließt den Screen


## 3. ANIMATION
## Lässt das Ergebnis-Bild leicht auf und ab schweben
transform result_floating_anim:
    yoffset 0
    linear 2.0 yoffset -15 # 2 Sekunden lang 15px hoch
    linear 2.0 yoffset 0   # 2 Sekunden lang wieder runter
    repeat