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

    ## Nach der Wahl geht es weiter zum Minigame-Start
    jump run_tutorial_minigame


## SCHRITT 2: Der Tutorial-Loop
label run_tutorial_minigame:
    
    $ current_ingredients = [] # Reset des Minigames

    user "Okay, los geht's. Ich muss mich genau an das Rezept halten."

    ## Wir rufen das Minigame IMMER mit dem Rezept "Tutorial" auf.
    call screen baking_minigame_screen("Tutorial", helper=None)

    if _return == "success":
        ## Wir springen direkt weiter in der Story.
        $ tutorial_baking_done = True
        jump awakening_shock_scene 
    else:
        ## Wenn fehlgeschlagen:
        user "Mist, das war falsch. Ich muss es nochmal versuchen."
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

    $ current_ingredients = [] # Reset des Minigames
    
    call screen baking_minigame_screen(current_recipe_name, helper=current_kitchen_helper)

    if _return == "success":
        ## --- SUCCESS SCREEN ---
        scene black with dissolve
        
        ## Wir definieren das Bild basierend auf dem Rezept
        if current_recipe_name == "Butterplätzchen":
            $ result_img = "images/minigame/result_butterplaetzchen.png"
        elif current_recipe_name == "Erdbeer Crepe":
            $ result_img = "images/minigame/result_crepe.png"
        else:
            ## Wir setzen es auf None, damit nichts angezeigt wird.
            $ result_img = None 

        ## Wir zeigen das Bild NUR, wenn wir eins definiert haben
        if result_img:
            show expression result_img at truecenter
            with dissolve
        
        centered "{size=40}Lecker!{/size}\n[current_recipe_name] ist fertig!"
        
        if result_img:
            hide expression result_img
        
        ## Belohnung & Dialog
        call _add_affection(current_kitchen_helper, 2)
        
        ## Kleiner Dialog je nach Helfer
        if current_recipe_name == "Butterplätzchen" and current_kitchen_helper == "Lavan":
            l "Mein Favorit."
        elif current_recipe_name == "Erdbeer Crepe" and current_kitchen_helper == "Cino":
            c "Juhu!"
            
        jump kitchen_room_interaction
        
    else:
        # --- FAIL SCREEN ---
        scene black with vpunch
        centered "{size=40}Verbrannt!{/size}\nDas war wohl nichts."
        # Neustart des GLEICHEN Rezepts
        jump run_baking_loop