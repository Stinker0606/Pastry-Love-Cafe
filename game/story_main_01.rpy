## -- TEIL 1: INTRO ---
label story_intro:
    scene bg cafe
    user "Ein alter Freund gab mir dieses spezielle Pulver."
    user "Ich sollte es ausprobieren."
    
    jump baking_minigame_hub # Ab ins Tutorial

## --- TEIL 2: ALLTAG START ---
label alltag_start:
    $ day = 1
    jump alltag_hub
    
## --- TEIL 3: ALLTAGS-HUB ---
label alltag_hub:
    ## --- TAGES-PLANUNG: WER IST WO? ---
    python:
        ## Tag 1 = Lavan, Tag 2 = Macoi, Tag 3 = Velvette, Tag 4 = Cino
        if (day % 4) == 1:
            current_kitchen_helper = "Lavan"
        elif (day % 4) == 2:
            current_kitchen_helper = "Macoi"
        elif (day % 4) == 3:
            current_kitchen_helper = "Velvette"
        else:
            current_kitchen_helper = "Cino"

    scene bg cafe
    user "Ich will was backen"

    menu:
        "In die Küche gehen":
            jump kitchen_room_interaction

        "Tag beenden":
            $ day += 1
            jump alltag_hub

## --- KÜCHEN-RAUM ---
label kitchen_room_interaction:
    scene bg kitchen
    
    ## Zeige den Helfer, der Dienst hat
    if current_kitchen_helper == "Lavan":
        show lavan smile
        l "Auch mal da [player_name]."
    elif current_kitchen_helper == "Macoi":
        show macoi smile
        m "Hey."
    elif current_kitchen_helper == "Velvette":
        show velvette smile
        v "Naa"
    elif current_kitchen_helper == "Cino":
        show cino smile
        c "Hallo."

    menu:
        "Backen (Minigame)":
            ## Wir gehen zum Minigame-Hub.
            jump baking_minigame_hub
            
        "Reden":
            if current_kitchen_helper == "Lavan":
                jump lavan_event_1
            elif current_kitchen_helper == "Macoi":
                jump macoi_event_1
            elif current_kitchen_helper == "Velvette":
                jump velvette_event_1
            elif current_kitchen_helper == "Cino":
                jump cino_event_1    
                
        "Zurück ins Café":
            jump alltag_hub