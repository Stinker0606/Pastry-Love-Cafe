label story_intro_05:

label act5_daydreaming_and_decision:

    # ---------------------------------------------------------
    # SZENE 1: AM NÄCHSTEN TAG BEI DER ARBEIT (Tagträumerei von Mc über Li)
    # ---------------------------------------------------------
    scene bg cafe with fade

    play music "audio/Morning_Cafe_Music.mp3" fadein 0.5 volume 0.75

    user "Der nächste Arbeitstag hatte längst begonnen, aber mein Kopf war ganz woanders."

    user "Ich wischte mechanisch über den Tresen, während meine Gedanken immer wieder zum gestrigen Abend im Einkaufszentrum zurückwanderten."

    user "Das Lachen, die Atmosphäre, dieser eine Moment..."

    user "Ich muss wohl ziemlich abwesend ausgesehen haben, denn plötzlich riss mich eine Stimme aus meinen Gedanken."

    # ---------------------------------------------------------
    # LOGIK: wer fragt ob alles ok ist (Höchster Affection-Wert)
    # ---------------------------------------------------------

    python:
        # Wir erstellen unser Dictionary zum Vergleichen
        points = {
            LI_LAVAN: lavan_points,
            LI_MACOI: macoi_points,
            LI_VELVETTE: velvette_points,
            LI_CINO: cino_points
        }
        
        # 1. Finde heraus, was die allerhöchste Punktzahl überhaupt ist
        max_points = max(points.values())
        
        # 2. Sammle ALLE Jungs in einer Liste, die genau diese Punktzahl haben
        tied_lis = [li for li, pts in points.items() if pts == max_points]
        
        # 3. Wähle zufällig einen aus dieser Gewinner-Liste
        highest_affection_li = renpy.random.choice(tied_lis)

    #if Lavan max love
    if highest_affection_li == LI_LAVAN:
        show lavan neutral at middle
        l "\"Hey! Hallo?! Erde an [player_name]!\""
        user "Ich zuckte zusammen. Lavan stand direkt vor mir, die Arme verschränkt, die Stirn in Falten."
        user "\"Lavan? Was ist los? Brennt was?\""
        l "\"Nein. Aber du starrst seit fünf Minuten die Kaffeemühle an, als würdest du sie hypnotisieren wollen.\""
        user "Er sah zur Seite, seine Stimme wurde etwas leiser, fast nuschelnd."
        show lavan sad with dissolve
        l "\"Du... wirkst nicht ganz da. Bist du krank? Oder hast du gestern zu viel Unsinn gegessen?\""
        user "\"Mir geht's gut, Lavan. Ich habe nur nachgedacht.\""
        show lavan angry with dissolve
        l "\"Tsk. Dann denk gefälligst an die Arbeit. Ich brauche dich hier fit. Verstanden?\""
        user "Trotz der harschen Worte blieb er noch einen Moment stehen und musterte mich besorgt, bevor er zurück zur Maschine ging."
        hide lavan with dissolve

    #if Velvette max love
    elif highest_affection_li == LI_VELVETTE:
        user "Ein Schnippen vor meinen Augen holte mich zurück in die Realität."
        show velvette sad at middle_vel
        v "\"Darling? Bist du eingefroren? Das steht dir nicht.\""
        user "Velvette lehnte elegant am Tresen und musterte mich mit kritischem, aber aufmerksamem Blick."
        user "\"Oh. Sorry, Velvette. Ich war in Gedanken.\""
        show velvette neutral with dissolve
        v "\"Offensichtlich. Deine Aura ist völlig zerstreut. Es ist der Ausflug gestern, nicht wahr?\""
        user "Sie lächelte leicht, fast wissend."
        v "\"Hat dich meine Gesellschaft so sehr beeindruckt, dass du jetzt zu keiner kognitiven Leistung mehr fähig bist?\""
        user "\"Vielleicht ein bisschen.\""
        show velvette happy with dissolve
        v "\"Verständlich. Ruh dich aus, wenn du musst. Ich kann es nicht gebrauchen, wenn mein Personal Augenringe bekommt.\""
        hide velvette with dissolve

    #if Cino max love
    elif highest_affection_li == LI_CINO:
        user "Plötzlich spürte ich eine Hand auf meiner Stirn."
        show cino neutral at middle
        c "\"Hmm... kein Fieber. Aber du guckst so glasig!\""
        user "Cino stand vor mir, die Augen groß vor Sorge. Er hielt einen halb aufgegessenen Keks in der anderen Hand."
        user "\"Cino? Alles okay?\""
        show cino angry with dissolve
        c "\"Das frage ich dich! Du hast den Kunden gar nicht gehört! Geht es dir gut? Bist du traurig?\""
        user "\"Nein, gar nicht. Ich bin nur etwas... verträumt.\""
        c "\"Oh! Verträumt ist gut! Aber mach mir keine Angst, okay?\""
        user "Er brach ein Stück von seinem Keks ab und hielt es mir hin."
        show cino happy with dissolve
        c "\"Hier. Zucker hilft beim Denken!\""
        hide cino with dissolve

    #if Macoi max love
    elif highest_affection_li == LI_MACOI:
        user "Jemand tippte mir leicht gegen den Ellbogen."
        user "Ich drehte mich um. Macoi stand da, leise wie immer."
        show macoi neutral at middle_m
        m "\"Lag?\""
        user "\"Was?\""
        m "\"Du hast gelaggt. Standbild. Seit zwei Minuten.\""
        user "Er musterte mich aus seinen halb geschlossenen Augen. Er wirkte nicht genervt, eher... beobachtend."
        user "\"Ja... sorry. Mein System muss wohl noch laden.\""
        m "\"Verstehe. Zu viele Hintergrundprozesse vom Wochenende.\""
        show macoi happy with dissolve
        user "Er schob mir stillschweigend einen frischen Kaffee über den Tresen, den er eigentlich für sich gemacht hatte."
        m "\"Reboot. Wir brauchen dich.\""
        hide macoi with dissolve


    # ---------------------------------------------------------
    # SZENE 2: ABENDS IM BETT (End Entscheidung mit wem sie enden möchte, wenn sie am meisten mag)
    # ---------------------------------------------------------
    stop music fadeout 2.5

    scene black with fade

    if lavan_points < 2 and macoi_points < 2 and velvette_points < 2 and cino_points < 2:
        play music "audio/Sad_Background_Music.mp3" fadein 0.5 volume 0.75
    else:
        play music "audio/Romantic_Music.mp3" fadein 0.5 volume 0.75

    #brauche am besten Musik hier - Welche?? XD wir haben music. Im /audio ordner.

    user "Der Arbeitstag ging vorbei, aber das Gefühl blieb."

    user "Jetzt lag ich in meinem Bett. Das Zimmer war dunkel, nur der Mond schien durch das Fenster."

    user "Ich starrte an die Decke und ließ den Tag Revue passieren."

    user "Dass die Person heute nach mir gesehen hat... das hat mir mehr bedeutet, als ich zugeben wollte."

    user "Ich drehte mich auf die Seite und schloss die Augen."

    user "Es hat keinen Sinn mehr, es zu leugnen. Ich habe mich in dieses Café verliebt. In das Chaos. In die Arbeit."

    user "Aber vor allem in eine Person."

    user "Mein Herz klopfte schneller, als ich mir endlich eingestand, wer mir wirklich nicht mehr aus dem Kopf geht."

    # ---------------------------------------------------------
    # DAS FINALE MENU der Entscheidung -> gibt mehr Affektion wert und dann je nachdem wer am meisten hat dessen Epilog bekommt man
    # Du bekommst hier eine Entscheidung -> gibt dir Affektion mit deinem lI (mehr als +20 oder so)
    # Und dann je nachdem mit wem du am meisten hast bekommst du ein Epilog mit deinem LI.
    # ---------------------------------------------------------

    ## PLS DIE TEXTE ÄNDERN, die hat mit Code pilot (die code AI gegeben) XD

    $ quick_menu = False

    menu:
        "Es ist Lavan." if lavan_points >= 2:
            $ lavan_points += 10
            $ quick_menu = True
            user "Hinter seiner rauen Schale steckt jemand, der sich kümmert. Ich will diejenige sein, die ihn zum Lächeln bringt."
            jump Epilog_Lavan

        "Es ist Macoi." if macoi_points >= 2:
            $ macoi_points += 10
            $ quick_menu = True
            user "Seine Ruhe ist genau das, was ich brauche. Bei ihm fühlt sich die Welt nicht so laut an."
            jump Epilog_Macoi

        "Es ist Velvette." if velvette_points >= 2:
            $ velvette_points += 10
            $ quick_menu = True
            user "Sie fordert mich heraus, aber sie sieht mich auch. Wirklich mich. Ich will an ihrer Seite glänzen."
            
            jump Epilog_Velvette

        "Es ist Cino." if cino_points >= 2:
            $ cino_points += 10
            $ quick_menu = True
            user "Er ist mein Sonnenschein. Mit ihm wird jeder Tag zu einem Abenteuer. Ich will dieses Lachen nie verlieren."
            jump Epilog_Cino

        ## SICHERHEITS-OPTION (Falls der Spieler bei NIEMANDEM 2 Punkte hat, sonst crasht das Spiel!)
        "Ich brauche noch Zeit für mich." if lavan_points < 2 and macoi_points < 2 and velvette_points < 2 and cino_points < 2:
            $ quick_menu = True
            user "Im Moment möchte ich mich einfach auf das Café konzentrieren..."
            jump Epilog_Single #(falls wir Single-Ending haben wollen, sonst einfach zurück ins Main Menu)
            return        

    return

# ---------------------------------------------------------
# DIE EPILOGE SIND IN DEN JEWEILIGEN CHARAKTER DATEIEN
# ---------------------------------------------------------

