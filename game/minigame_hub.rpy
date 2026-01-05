## --- HAUPT-EINGANG ZUM BAKING MINIGAME---
label baking_minigame_hub:
    scene bg kitchen 
    
    if not tutorial_baking_done:
        jump baking_tutorial_selection
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
            
        "Matcha Muffin":
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
        ## Wir springen zurück zur Auswahl
        jump baking_tutorial_selection 

    ## 3. FEHLER (Alles andere)
    else:
        user "Mist, das war falsch. Ich muss es nochmal versuchen."
        ## Wir starten NUR das Minigame neu (gleiches Rezept)
        jump run_tutorial_minigame

## NORMALER MODUS (Alltag)
label baking_recipe_selection:
    
    scene bg kitchen
    user "Okay, [current_kitchen_helper] hilft mir heute. Was backen wir?"
    
    menu:
        user "Okay, [current_kitchen_helper] hilft mir heute. Was backen wir?"

        ## --- REZEPT 1: BUTTERPLÄTZCHEN ---
        "Butterplätzchen":
            $ current_recipe_name = "Butterplätzchen"
            jump run_baking_loop

        ## --- REZEPT 2: ERDBEER CREPE ---
        "Erdbeer Crepe":
            $ current_recipe_name = "Erdbeer Crepe"
            jump run_baking_loop
        
        "Zurück":
            jump kitchen_room_interaction

## --- DER UNIVERSELLE BACK-LOOP ---
label run_baking_loop:
    
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
        scene black with dissolve
        
        if current_recipe_name == "Butterplätzchen":
            $ result_img = "images/minigame/result_butterplaetzchen.png"
        elif current_recipe_name == "Erdbeer Crepe":
            $ result_img = "images/minigame/result_crepe.png"
        else:
            $ result_img = None 

        if result_img and renpy.loadable(result_img):
            show expression result_img at truecenter
            with dissolve
        
        centered "{size=40}Lecker!{/size}\n[current_recipe_name] ist fertig!"
        
        if result_img:
            hide expression result_img
        
        call _add_affection(current_kitchen_helper, 2)
        
## FÜR DICH SOFIYA, Char reaktion auf der verschiedenen gerichte. Untendrunter siehtst du ein Beispiel, mach die Kommentierung weg und wo das FETT geschriebene ist ersetzen.

        if current_recipe_name == "Butterplätzchen" and current_kitchen_helper == "Lavan":
            l "Mein Favorit."
        elif current_recipe_name == "Erdbeer Crepe" and current_kitchen_helper == "Cino":
            c "Juhu!"
        #elif current_recipe_name == "NAME DES REZEPTES" and current_kitchen_helper == "CHARAKTER":
        #    KÜRZEL DES CHARS "REAKTION"    

## BIS HIER FÜR DICH 

        # Fall A: Wir kommen aus der Story-Eröffnung (Der Tag geht weiter)
        if store.baking_context == "story_opening":
            # Variable resetten, damit sie später nicht stört
            $ store.baking_context = None 
            # Wir springen WEITER in der Story
            jump story_cafe_after_rush 

        # Fall B: Wir kommen aus dem normalen Alltag (Zurück zur Küche)
        else:
            jump kitchen_room_interaction
            
    elif minigame_result == "cancel":
        ## ABBRUCH
        scene bg kitchen
        user "Vielleicht später."
        
        if store.baking_context == "story_opening":
            $ store.baking_context = None 
            ## Man interpretiert Abbruch als "Doch nicht backen"
            jump cafe_opening_decision_hub 
        else:
            jump kitchen_room_interaction
        
    else:
        ## FAIL
        scene black with vpunch
        centered "{size=40}Verbrannt!{/size}\nDas war wohl nichts."
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