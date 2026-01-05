## -- TEIL 1: INTRO ---
label story_intro_03:
    ## Wir starten in der Küche oder?
    scene bg Flur with fade

    ## Intro Monolog
    user "Seitdem sind einige Tage vergangen."

    user "Und jeder einzelne davon war laut."

    user "Als ich an diesem Morgen aufwachte, dröhnte es schon durch die Wände."

    #Sie geht ins Badezimmer und trifft Velvette

    user "Ich schleppte mich ins Badezimmer. Dort stand Velvette, vollkommen in ihrem Element."

    user "Sie schminkte sich, als würde sie sich gerade auf eine Laufstegshow vorbereiten, und ignorierte meine Existenz erfolgreich wie eine echte Diva."

    user "Ich schnappte mir meine Zahnbürste und manövrierte mich geschickt um sie herum"

    #--------------
    #Hier choice einfach leise dein Ding machen oder ihr ein Kompliment machen

    user "\"Du siehst gut aus.\""

    user "Ohne auch nur ihren Blick vom Spiegel zu lösen"

    v "\"Ich weiß.\""

    user "Ich seufzte leise, beendete mein Tanz und machte mich auf den Weg Richtung Küche, ihr das Badezimmer vollkommen überlassend."

    # Geht den Flur weiter entlang

    user "Auf dem Weg kam ich an Macois angelehnter Tür vorbei."

    user "Drinnen war es dunkel, nur ein bläuliches Schimmern kroch in den Flur. Ich drückte die Tür ein Stück weiter auf."

    user "Der grünhaarige Mann saß zusammengekrümmt wie eine halbe Garnele vor seinem Monitor."

    user "Das einzige Licht im Raum war vom Bildschirm, der ein Videospiel zeigte."

    user "\"Du bist schon wach?\""

    user "Er drehte sich langsam zu mir, und ich sah die deutlichsten Augenringe meines Lebens"

    m "\"Noch wach\""

    user "murmelte er tonlos und wandte sich wieder dem Bildschirm zu."

    user "\"Wir machen in zwei Stunden auf.\""

    user "Er gab keine Antwort."

    user "Wenn er mich überhaupt gehört hatte, dann hatte er beschlossen, es zu ignorieren. Ich schüttelte nur den Kopf und ging weiter."

    # Geht in die Küche und trifft die restlichen 2 LI

    user "Unten in der Küche waren die letzten beiden schon aktiv."

    user "Cino bereitete strahlend das Frühstück zu, summend wie ein sonniger Morgenmensch."

    user "Daneben stand Lavan"

    user "Er ärgerte sich über die Kaffeemaschine, als sei sie persönlich für all sein Leid verantwortlich."

    user "\"Alles gut?\""

    l "\"Ja! Alles super! ALLES SUPER!\""

    user "schnappte er sofort, eindeutig eine Lüge."

    user "Sein Haar puffte leicht vor Hitze auf, wie bei einem wütenden Wasserkocher."

    user "Cino drehte sich mit einem Lächeln zu mir um"

    c "\"[player_name], Er hat nur versucht, den Kaffee stärker zu machen! Und dann ist sie explodiert! Nur ein bisschen.\""

    l "\"SIE IST NICHT EXPLODIERT!\""

    user "Empörte sich Lavan."

    user "Die Kaffeemaschine tropfte verräterisch im Hintergrund."

    c "\"Ich habe uns Pfannkuchen gemacht! Ich hoffe, sie sind nicht zu fluffig, ich wollte sie besonders fluffig machen, aber dann waren sie… zu fluffig, also-\""

    l "\"CINO, KEINER BRAUCHT EINEN ESSAY ÜBER PANCAKES!!\""

    user "Fauchte Lavan und riss ihm fast den Teller aus der Hand."

    user "Er stellte ihn etwas zu kräftig auf den Tisch, sodass mein Salzstreuer bedrohlich wackelte."

    #--------------
    #Hier eine Choice wenn man unterstützt also welche seite

    user "Velvet kam die Treppe herunter, stolz wie eine Königin, die gerade frische Luft mit Parfüm verwechselt hatte."

    v "\"Mein Frühstück bitte ohne Fett, ohne Zucker und ohne jegliche Form von…\""

    user "Sie sah auf den Pfannkuchen"

    v "\"...Teig.\""

    user "Ich blinzelte."

    user "\"Also… nichts?\""

    v "\"Perfekt.\""

    user "Sie setzte sich hin und sah aus, als würde sie jetzt eine imaginäre Menükarte bewerten."

    user "Macoi schlurfte als Letzter in die Küche, zwar in der Uniform jeddoch schief und zerknittert und er murrte etwas, das sich wie ein „Morgen“ anhörte, oder ein Schmerzenslaut."

    user "Er setzte sich hin, legte den Kopf auf den Tisch und starrte die Pfannkuchen an, als würden sie ihn persönlich beleidigen."

    user "\"Willst du einen?\""

    m "\"Ich will schlafen.\""

    user "\"Das ist kein Frühstück.\""

    m "\"Dann will ich kein Frühstück.\""

    user "Unangenehm schaute ich mich im Zimmer um."

    user "\"Also ich hoffe ihr seid heute bereit und motiviert euren ersten Tag nach dem training anzugehen?\""

    user "Jeder von ihnen hatte ein nicht so glückliches Gesichtsausdruck"

    #--------------
    #Hier eine Wahl einfügen wenn man unterstützt (von allen 4), "So alles wird gut mässig"








## PLS LASSEN WAS HIER DRUNTER IST!!

## Ab ins Alltag Hub
    jump alltag_start

    ## ========================================================================================================================================================================================
    ## -- BAKING HUB TEST --- BITTE DEN CODE HIER DRUNTER LASSEN
    ## ========================================================================================================================================================================================

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
