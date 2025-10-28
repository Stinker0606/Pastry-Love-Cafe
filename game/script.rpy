label splashscreen:
    scene black
    # (Logo maybe hinzufügen und es definieren in 01_definitions)
    # show logo at truecenter
    with dissolve
    pause 2.0
    return # WICHTIG: 'return' beendet den Splashscreen

# --- SYSTEM-LABELS ---

# --- DER START DES SPIELS ---
# (Im Hauptmenü abrufbar per START)
label start:
    # Stoppt die Hauptmenü-Musik falls eine vorhanden ist.
    stop music fadeout 1.0
    scene black
    
    # --- RESET FÜR NEUES SPIEL ---
    # (Setzt alles zurück damit es ein NEW GAME ist)
    # Beispiel:
    $ lavan_points = 0
    $ is_lavan_awakened = False
    $ macoi_points = 0
    $ is_macoi_awakened = False
    $ velvette_points = 0
    $ is_velvette_awakened = False
    $ cino_points = 0
    $ is_cino_awakened = False
    
    $ event_lavan_1_done = False # (Beispiel für alle Event-Flaggen)
    
    # Ruft das Setup-Label aus 02_helpers.rpy auf
    call setup_player_character
    
    # (sobald es fertig ist passiert hier hin der return)
    
    user "Okay, es ist Zeit oder so. IDK"
    
    # Springt zum nächsten Part
    jump test_hub