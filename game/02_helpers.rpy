## 02_helpers.rpy

# aaa,bbb,ccc und ddd sind PLACEHOLDER

init python:
    # Definiere die "Schlüssel" für deine LIs.
    LI_AAA = "aaa"
    LI_BBB = "bbb"
    LI_CCC = "ccc"
    LI_DDD = "ddd"

# Ein aufrufbares Label zum Punkte-Vergeben
label _add_affection(li_name, amount=1):
    python:
        if li_name == LI_AAA:
            store.aaa_points += amount
        elif li_name == LI_BBB:
            store.bbb_points += amount
        # ... usw.
    return

# Label für die Spielereingabe, falls wir es nutzen wollen.
label get_player_name:
    $ player_name = renpy.input("Wie ist dein Name?", length=20)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Mc"
    $ mc.name = player_name
    return