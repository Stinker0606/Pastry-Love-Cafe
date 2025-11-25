label baking_minigame_hub:
    scene bg kitchen
    
    if not tutorial_baking_done:
        # --- TUTORIAL "FIRST TIME BAKING" MODUS ---
        jump baking_tutorial_selection
    else:
        # --- NORMALER MODUS ---
        jump baking_recipe_selection

# --- TUTORIAL WAHL ---
label baking_tutorial_selection:
    user "Ich habe das magische Pulver... und genug Zutaten für ein Rezept."
    user "Wen soll ich zuerst zum Leben erwecken?"
    
    menu (show_say=True):
        "{#lavan}Lavan (Schokoladenkuchen)":
            $ first_li_chosen = "Lavan"
            # Bonus-Punkt!
            call _add_affection(LI_LAVAN, 1)
            # Starte Minigame mit Tutorial-Rezept (MIT Pulver)
            call screen baking_minigame_screen("lavan_tutorial")
            
        "{#macoi}Macoi (Matcha-Muffin)":
            $ first_li_chosen = "Macoi"
            call _add_affection(LI_MACOI, 1)
            call screen baking_minigame_screen("macoi_tutorial")
            
        "{#velvette}Velvette (Red Velvet)":
            $ first_li_chosen = "Velvette"
            call _add_affection(LI_VELVETTE, 1)
            call screen baking_minigame_screen("velvette_tutorial")
            
        "{#cino}Cino (Zitronenrolle)":
            $ first_li_chosen = "Cino"
            call _add_affection(LI_CINO, 1)
            call screen baking_minigame_screen("cino_tutorial")

    # Wenn das Minigame erfolgreich war ('_return' kommt vom Screen):
    if _return == "success":
        $ tutorial_baking_done = True
        jump awakening_sequence_start
    else:
        user "Das hat nicht geklappt. Ich muss es nochmal versuchen."
        jump baking_tutorial_selection

# --- NORMALER MODUS (Alltag) ---
label baking_recipe_selection:
    user "Was möchte ich heute backen?"
    
    menu (show_say=True):
        "Backen":
            jump baking_recipe_list
        
        "Hilfe (Erklärung)":
        # Zeigt das Overlay direkt an (simuliert)
            call screen baking_help_overlay_screen()
            jump baking_minigame_hub
             
        "Verlassen":
            jump alltag_hub


label baking_recipe_list:
    menu (show_say=True):
        # Hier sind die NORMALEN Rezepte
        "{#lavan}Schokokuchen":
            call screen baking_minigame_screen("lavan_date")
            jump lavan_event_1
        
        "{#macoi}Matcha-Muffin":
            call screen baking_minigame_screen("macoi_date")
            jump macoi_event_1

        "{#velvette}Red Velvet Cupcake":
            call screen baking_minigame_screen("velvette_date")
            jump velvette_event_1

        "{#cino}Zimtrolle":
            call screen baking_minigame_screen("cino_date")
            jump cino_event_1
        
        "Zurück":
            jump baking_minigame_hub
