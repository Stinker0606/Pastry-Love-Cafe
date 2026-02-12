label story_intro_05:

label act5_daydreaming_and_decision:

    # ---------------------------------------------------------
    # SZENE 1: AM NÄCHSTEN TAG BEI DER ARBEIT (Tagträumerei von Mc über Li)
    # ---------------------------------------------------------
    scene bg_cafe_day with fade

    user "Der nächste Arbeitstag hatte längst begonnen, aber mein Kopf war ganz woanders."

    user "Ich wischte mechanisch über den Tresen, während meine Gedanken immer wieder zum gestrigen Abend im Einkaufszentrum zurückwanderten."

    user "Das Lachen, die Atmosphäre, dieser eine Moment..."

    user "Ich muss wohl ziemlich abwesend ausgesehen haben, denn plötzlich riss mich eine Stimme aus meinen Gedanken."

    # ---------------------------------------------------------
    # LOGIK: wer fragt ob alles ok ist (Höchster Affection-Wert)
    # ---------------------------------------------------------

    # Wir ermitteln, wer den höchsten Wert hat.

    #if Lavan max love
    l "\"Hey! Hallo?! Erde an [player_name]!\""
    user "Ich zuckte zusammen. Lavan stand direkt vor mir, die Arme verschränkt, die Stirn in Falten."
    user "\"Lavan? Was ist los? Brennt was?\""
    l "\"Nein. Aber du starrst seit fünf Minuten die Kaffeemühle an, als würdest du sie hypnotisieren wollen.\""
    user "Er sah zur Seite, seine Stimme wurde etwas leiser, fast nuschelnd."
    l "\"Du... wirkst nicht ganz da. Bist du krank? Oder hast du gestern zu viel Unsinn gegessen?\""
    user "\"Mir geht's gut, Lavan. Ich habe nur nachgedacht.\""
    l "\"Tsk. Dann denk gefälligst an die Arbeit. Ich brauche dich hier fit. Verstanden?\""
    user "Trotz der harschen Worte blieb er noch einen Moment stehen und musterte mich besorgt, bevor er zurück zur Maschine ging."

    #if Velvette max love
    user "Ein Schnippen vor meinen Augen holte mich zurück in die Realität."
    v "\"Darling? Bist du eingefroren? Das steht dir nicht.\""
    user "Velvette lehnte elegant am Tresen und musterte mich mit kritischem, aber aufmerksamem Blick."
    user "\"Oh. Sorry, Velvette. Ich war in Gedanken.\""
    v "\"Offensichtlich. Deine Aura ist völlig zerstreut. Es ist der Ausflug gestern, nicht wahr?\""
    user "Sie lächelte leicht, fast wissend."
    v "\"Hat dich meine Gesellschaft so sehr beeindruckt, dass du jetzt zu keiner kognitiven Leistung mehr fähig bist?\""
    user "\"Vielleicht ein bisschen.\""
    v "\"Verständlich. Ruh dich aus, wenn du musst. Ich kann es nicht gebrauchen, wenn mein Personal Augenringe bekommt.\""

    #if Cino max love
    user "Plötzlich spürte ich eine Hand auf meiner Stirn."
    c "\"Hmm... kein Fieber. Aber du guckst so glasig!\""
    user "Cino stand vor mir, die Augen groß vor Sorge. Er hielt einen halb aufgegessenen Keks in der anderen Hand."
    user "\"Cino? Alles okay?\""
    c "\"Das frage ich dich! Du hast den Kunden gar nicht gehört! Geht es dir gut? Bist du traurig?\""
    user "\"Nein, gar nicht. Ich bin nur etwas... verträumt.\""
    c "\"Oh! Verträumt ist gut! Aber mach mir keine Angst, okay?\""
    user "Er brach ein Stück von seinem Keks ab und hielt es mir hin."
    c "\"Hier. Zucker hilft beim Denken!\""

    #if Macoi max love
    user "Jemand tippte mir leicht gegen den Ellbogen."
    user "Ich drehte mich um. Macoi stand da, leise wie immer."
    m "\"Lag?\""
    user "\"Was?\""
    m "\"Du hast gelaggt. Standbild. Seit zwei Minuten.\""
    user "Er musterte mich aus seinen halb geschlossenen Augen. Er wirkte nicht genervt, eher... beobachtend."
    user "\"Ja... sorry. Mein System muss wohl noch laden.\""
    m "\"Verstehe. Zu viele Hintergrundprozesse vom Wochenende.\""
    user "Er schob mir stillschweigend einen frischen Kaffee über den Tresen, den er eigentlich für sich gemacht hatte."
    m "\"Reboot. Wir brauchen dich.\""


    # ---------------------------------------------------------
    # SZENE 2: ABENDS IM BETT (End Entscheidung mit wem sie enden möchte, wenn sie am meisten mag)
    # ---------------------------------------------------------

    scene bg_bedroom_night with fade
    #brauche am besten Musik hier

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
    # Du bekommst hier eine Entscheidung -> gibt dir Affektion mit deinem lI (mehr als sonst +20 oder so)
    # Und dann je nachdem mit wem du am meisten hast bekommst du ein Epilog mit deinem LI -> das heißt wie die story_main_05 so auch für jeden ein Epilog
    # Am besten nennt man sie Epilog_NamevonLI
    # ---------------------------------------------------------

    return
