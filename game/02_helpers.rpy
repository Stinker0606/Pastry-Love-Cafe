## -- Helpers für unser Game --
init python:
    ## Definiere die "Keys" für deine LIs.
    LI_LAVAN = "Lavan"
    LI_MACOI = "Macoi"
    LI_VELVETTE = "Velvette"
    LI_CINO = "Cino"

## Ein aufrufbares Label zum Punkte-Vergeben
label _add_affection(li_name, amount=1):
    python:
        if li_name == LI_LAVAN:
            store.lavan_points += amount
        elif li_name == LI_MACOI:
            store.macoi_points += amount
        elif li_name == LI_VELVETTE:
            store.velvette_points += amount
        elif li_name == LI_CINO:
            store.cino_points += amount    
    return

## -- Charakter-Erstellung --
## Dieses Label wird von 'game_start' aufgerufen
label setup_player_character:

    ## Schritt 1: Geschlecht wählen
    user "Zuerst... wer bin ich?" # (user ist hier noch 'None', also Erzähler)
    menu:
        "Ich bin ein Mann.":
            ## Setzt die globalen Variablen aus 01_definitions
            $ player_gender = "male"
            $ mc_pronoun_he_she = "er"
            $ mc_pronoun_his_her = "sein"
            $ mc_title = "Bäcker"
            $ mc_pronoun_article = "der"

        "Ich bin eine Frau.":
            $ player_gender = "female"
            $ mc_pronoun_he_she = "sie"
            $ mc_pronoun_his_her = "ihr"
            $ mc_title = "Bäckerin"
            $ mc_pronoun_article = "die"

    ## Schritt 2: Name wählen
    user "Und mein Name ist..."

    ## Die Namensabfrage
    python:
        while True:
            ## 1. Zeige das Eingabefeld.
            player_name_input = renpy.input("Wie ist mein Name?", length=20)
            
            ## 2. Entferne Leerzeichen
            player_name_input = player_name_input.strip()
            
            ## 3. Prüfe, ob das Ergebnis LEER ist
            if player_name_input == "":
                ## 4. Wenn ja: Zeige Fehlermeldung, Schleife startet neu
                renpy.say(None, "Ich muss einen Namen eingeben.") # 'None' = Erzähler
            else:
                ## 5. Wenn nicht leer: Speichere den Namen...
                store.player_name = player_name_input
                ## ... und brich die Schleife ab
                break

    ## JETZT weisen wir dem 'mc'-Charakter-Objekt den Namen zu
    $ user.name = player_name
    
    user "Okay, ich bin [player_name], [mc_pronoun_article] [mc_title]."
    
    return ## Kehrt zu 'game_start' zurück
