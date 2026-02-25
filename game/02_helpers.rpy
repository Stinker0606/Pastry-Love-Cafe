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

    scene bg sig with dissolve

    ## Die Namensabfrage
    python:
        renpy.choice_for_skipping() # Verhindert, dass Spieler den Namenseingabe-Screen überspringen können, wenn sie einmal da sind.

        while True:
            ## 1. Zeige das Eingabefeld.
            player_name_input = renpy.input("Unterschrift", length=20)

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

    user "[player_name]"

    user "Ich schaute kurz meinen Namen noch einmal an, bevor ich ihm das Klembrett wiedergab und Ihn böse anschaute."

    return ## Kehrt zurück
