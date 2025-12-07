## LOGIK FÜR DAS BAKING MINIGAME
init python:
    
    ## Positionen der Zutaten
    ingredient_positions = {
        "Mehl": (100, 200),
        "Ei": (250, 200),
        "Zucker": (400, 200),
        "Milch": (500, 150),
        "Butter": (700, 200),
        "Streusel": (850, 200),
        "Whisk": (1000, 200) 
    }

    ## Globale Variable, um zu wissen, ob der Besen gehalten wird
    store.is_whisk_held = False 

    ## --- 1. ZUTATEN LOGIK ---
    def ingredient_dragged(drags, drop):
        ## --- 1. FAIL-SAFE ---
        ## Wenn der Spieler das Item ins Leere zieht (kein valides Drop-Ziel),
        ## wird die Aktion abgebrochen und das Item zurückgesetzt.
        if not drop:
            drag_item = drags[0]
            start_pos = ingredient_positions[drag_item.drag_name]
            drag_item.snap(start_pos[0], start_pos[1], delay=0.1)
            return

        drag_item = drags[0]
        item_name = drag_item.drag_name
        
        ## SPEZIALFALL: MIXEN (Rühr-Mechanik)
        if item_name == "Whisk": 
            start_pos = ingredient_positions["Whisk"]
            drag_item.snap(start_pos[0], start_pos[1], delay=0.1)
            return

        ## NORMALFALL: ZUTATEN
        ## Wir fügen sie einfach hinzu. KEINE PRÜFUNG HIER!
        store.current_ingredients.append(item_name)
        
        ## Feedback
        renpy.notify(f"{item_name} hinzugefügt")
        
        ## Zutat schnappt zurück
        start_pos = ingredient_positions[item_name]
        drag_item.snap(start_pos[0], start_pos[1], delay=0.1)
        return

    ## --- 2. MIXER STATUS FUNKTIONEN ---

    ## Wird aufgerufen, wenn man den Besen ANKLICKT (Aufhebt)
    def whisk_activate(drags):
        store.is_whisk_held = True
        return

    ## Wird aufgerufen, wenn man den Besen LOSLÄSST
    def whisk_drop_action(drags, drop):
        ## Status auf False setzen
        store.is_whisk_held = False
        
        ## Besen zurückschnappen lassen
        whisk = drags[0]
        whisk.snap(1000, 200, delay=0.1)
        return

    ## --- 3. INTELLIGENTE MIXER LOGIK ---
    def check_mixing_progress():
        
        ## WICHTIG: Wir prüfen jetzt unsere eigene Variable
        if not store.is_whisk_held:
            return

        ## Mausposition holen
        mx, my = renpy.get_mouse_pos()
        
        ## Zonen definieren
        zone1 = (900, 500, 1000, 600) 
        zone2 = (1000, 500, 1100, 600)
        zone3 = (1000, 600, 1100, 700) 
        zone4 = (900, 600, 1000, 700) 
        
        current_zone = None
        if zone1[0] < mx < zone1[2] and zone1[1] < my < zone1[3]: current_zone = "Zone1"
        elif zone2[0] < mx < zone2[2] and zone2[1] < my < zone2[3]: current_zone = "Zone2"
        elif zone3[0] < mx < zone3[2] and zone3[1] < my < zone3[3]: current_zone = "Zone3"
        elif zone4[0] < mx < zone4[2] and zone4[1] < my < zone4[3]: current_zone = "Zone4"
            
        if current_zone:
            screen = renpy.get_screen("baking_minigame_screen")
            if screen:
                hits = screen.scope["whisk_zones_hit"]
            
                if current_zone not in hits:
                    hits.append(current_zone)
                    
                    if len(hits) < 4:
                        renpy.notify(f"Rühren: {len(hits)} / 4")
                    
                    ## RUNDE KOMPLETT?
                    if len(hits) >= 4:
                        hits.clear()
                        
                        ## SCHUTZ VOR DOPPELT-MIXEN
                        if len(store.current_ingredients) > 0 and store.current_ingredients[-1] == "Mixen":
                            renpy.notify("Schon gut, ist bereits gemischt!")
                            return 

                        ## Das "Mixen" wird gespeichert!
                        store.current_ingredients.append("Mixen")
                        renpy.notify("Teig gerührt!")

    ## --- 4. DER GROSSE CHECK AM ENDE ---
    ## Diese Funktion wird NUR vom Button "Fertig!" aufgerufen!
    def final_baking_check(target_recipe_name):
        
        target_steps = recipes_data[target_recipe_name]["steps"]
        current_steps = store.current_ingredients
        
        ## Check 1: Länge
        if len(current_steps) != len(target_steps):
            renpy.notify("Die Menge stimmt nicht!")
            renpy.end_interaction("fail")
            return

        ## Check 2: Reihenfolge und Inhalt (inklusive "Mixen")
        for i in range(len(target_steps)):
            if current_steps[i] != target_steps[i]:
                renpy.notify(f"Fehler bei Schritt {i+1}!")
                renpy.end_interaction("fail")
                return

        ## Check 3: Alles richtig!
        if recipes_data[target_recipe_name]["type"] == "crepe":
            renpy.end_interaction("crepe_phase_2")
        else:
            renpy.end_interaction("success")
        return

## SCREEN
screen baking_minigame_screen(recipe_name, helper=None):
    modal True
    add Solid("#333") # Platzhalter Hintergrund
    ## add "images/backgrounds/kitchen.jpg"

    $ store.current_recipe_name_global = recipe_name

    ## Variable für die Mixer-Treffer
    default whisk_zones_hit = []
    
    ## --- TIMER FÜR DAS RÜHREN ---
    ## Ruft 20 Mal pro Sekunde die Prüfung auf, wo die Maus ist
    timer 0.05 repeat True action Function(check_mixing_progress)

    ## INFO TEXT (Nur zum Testen, später löschen)
    vbox:
        # Positionen:
        xalign 0.5
        # Text
        text f"Rezept:":
            xalign 0.5
        text f"Soll: {recipes_data[recipe_name]['steps']}" size 25 color "#aaa":
            xalign 0.5
        text f"Drin: {len(current_ingredients)}" size 25 color "#aaa" xalign 0.5    

    ## DRAG GROUP
    draggroup:
        
        ## SCHÜSSEL
        drag:
            drag_name "Bowl"
            child Transform("images/minigames/baking/Bowl_Sprite.png", size=(400, 400))
            # child Composite(
            #     (200, 200),  # Platzhalter
            #     (0, 0), Solid("#4444ff"), # Platzhalter
            #     (0, 0), Text("SCHÜSSEL", size=30, color="#fff", xalign=0.5, yalign=0.5, xysize=(200,200)) # Platzhalter
            # )            # Platzhalter
            draggable False
            droppable True
            xpos 800 ypos 400

        ## --- ZUTATEN ---

        ## MEHL
        drag:
            drag_name "Mehl"
            ## child Transform("images/minigame/item_mehl.png", size=(60, 80))
            child Composite(
                (100, 60), # Platzhalter
                (0, 0), Solid("#ffffff"), # Platzhalter
                (0, 0), Text("Mehl", size=20, color="#000", xalign=0.5, yalign=0.5, xysize=(100,60)) # Platzhalter
            ) # Platzhalter
            droppable False
            dragged ingredient_dragged
            xpos 100 ypos 200 

        ## EI
        drag:
            drag_name "Ei"
            child Transform("images/minigames/baking/Single_Egg_Sprite.png", size=(100, 95))
            # child Composite(
            #     (100, 60),
            #     (0, 0), Solid("#ffff00"),
            #     (0, 0), Text("Ei", size=20, color="#000", xalign=0.5, yalign=0.5, xysize=(100,60))
            # )
            droppable False
            dragged ingredient_dragged
            xpos 250 ypos 200

        ## ZUCKER
        drag:
            drag_name "Zucker"
            ## child Transform("images/minigame/item_zucker.png", size=(60, 80))
            child Composite(
                (100, 60),
                (0, 0), Solid("#eeeeee"),
                (0, 0), Text("Zucker", size=20, color="#000", xalign=0.5, yalign=0.5, xysize=(100,60))
            )
            droppable False
            dragged ingredient_dragged
            xpos 400 ypos 200

        ## MILCH
        drag:
            drag_name "Milch"
            child Transform("images/minigames/baking/Milk_Sprite.png", size=(200, 200))
            # child Composite(
            #     (100, 60),
            #     (0, 0), Solid("#0000ff"),
            #     (0, 0), Text("Milch", size=20, color="#fff", xalign=0.5, yalign=0.5, xysize=(100,60))
            # )
            droppable False
            dragged ingredient_dragged
            xpos 500 ypos 150
            
        ## BUTTER
        drag:
            drag_name "Butter"
            ## child Transform("images/minigame/item_butter.png", size=(60, 80))
            child Composite(
                (100, 60),
                (0, 0), Solid("#ffd700"),
                (0, 0), Text("Butter", size=20, color="#000", xalign=0.5, yalign=0.5, xysize=(100,60))
            )
            droppable False
            dragged ingredient_dragged
            xpos 700 ypos 200
            
        ## STREUSEL
        drag:
            drag_name "Streusel"
            ## child Transform("images/minigame/item_streusel.png", size=(60, 80))
            child Composite(
                (100, 60),
                (0, 0), Solid("#ff00ff"),
                (0, 0), Text("Streusel", size=20, color="#fff", xalign=0.5, yalign=0.5, xysize=(100,60))
            )
            droppable False
            dragged ingredient_dragged
            xpos 850 ypos 200

        ## SCHNEEBESEN
        drag:
            id "whisk_drag"
            drag_name "Whisk"
            ## child Transform("images/minigame/item_whisk.png", size=(60, 80))
            child Composite(
                (80, 50),
                (0, 0), Solid("#cccccc"),
                (0, 0), Text("MIXER", size=15, color="#000", xalign=0.5, yalign=0.5, xysize=(80,50))
            )
            droppable False
            activated whisk_activate
            dragged whisk_drop_action
            xpos 1000 ypos 200

    ## Eier Karton
    add Composite(
            (100, 50),
            (0, 0), Solid("#ffff00"),
            (0, 0), Text("Eier Karton", size=20, color="#000", xalign=0.5, yalign=0.5, xysize=(100,60))
        ) xpos 250 ypos 250

    ## --- BUTTONS ---

    ## RESET
    textbutton "Reset":
        xalign 0.02 yalign 0.98
        action [SetScreenVariable("current_ingredients", []), Function(renpy.restart_interaction)]

    # CHECK BUTTON
    textbutton "Fertig!":
        xalign 0.5 yalign 0.95
        style "choice_button"
        text_size 40
        # Ruft die Prüf-Funktion auf
        action Function(final_baking_check, recipe_name)

    ## CANCEL
    textbutton "Abbrechen":
        xalign 0.02 yalign 0.90
        action Return("cancel")

## --- CREPE PFANNE SCREEN ---
label crepe_pan_minigame:
    call screen crepe_pan_screen()
    if _return == "success":
        return "success"
    else:
        return "fail"

screen crepe_pan_screen():
    modal True
    add "bg kitchen" # Oder Pfannen-Hintergrund
    
    default pan_state = 0 
    
    vbox:
        xalign 0.5 yalign 0.5
        
        if pan_state == 0:
            ## add "images/minigame/crepe_raw.png"
            text "Teig brät... (Warte)" size 50
            timer 3.0 action SetScreenVariable("pan_state", 1)
            
        elif pan_state == 1:
            ## add "images/minigame/crepe_cooked_1.png"
            text "JETZT WENDEN!" color "#f00" size 60
            button:
                text "KLICK MICH" size 50
                action SetScreenVariable("pan_state", 2)
                
        elif pan_state == 2:
            ## add "images/minigame/crepe_raw.png"
            text "Seite 2 brät..." size 50
            timer 3.0 action SetScreenVariable("pan_state", 3)
            
        elif pan_state == 3:
            ## add "images/minigame/crepe_cooked_1.png"
            text "FERTIG! Erdbeeren dazu!" size 50
            button:
                text "Erdbeeren drauf" size 50
                action Return("success")