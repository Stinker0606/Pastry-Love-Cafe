label story_intro_03:
    play audio "audio/Bird_Chirping_Ambience.mp3" fadein 1.0
    # IDK Wo wir starten.
    scene bg Flur with fade
    user "Der Wecker klingelte. Ein neuer Tag."

    ## 1. WIR ZÄHLEN ZUSAMMEN
    ## Wir zählen nur die "success" Momente. Alles andere (fail/ignored) gibt 0 Punkte.
    $ day_score = 0

    if task_result_lavan == "success":
        $ day_score += 1
    if task_result_macoi == "success":
        $ day_score += 1
    if task_result_velvette == "success":
        $ day_score += 1
    if task_result_cino == "success":
        $ day_score += 1

    ## 2. GENERELLE STIMMUNG (Good Day / Bad Day)
    if day_score >= 3:
        # Score ist 3 oder 4 -> Guter Tag
        user "Ich streckte mich ausgiebig. Als ich die Augen öffnete, fühlte sich das Zimmer heller an als sonst."
        user "Gestern lief es eigentlich ziemlich gut. Besser als erwartet."
        user "Auch wenn es kleine Probleme gab, haben wir sie schnell gelöst."
        user "Der Laden lief, die Kasse stimmte und das Wichtigste wir haben uns nicht gegenseitig umgebracht."

    elif day_score == 2:
        # Score ist 2 -> Naja Tag
        user "Mein Wecker riss mich aus einem unruhigen Schlaf. Ich rieb mir die Schläfen."
        user "Gestern war... okay. Es gab Höhen und Tiefen."
        user "Wir haben überlebt, aber 'harmonisch' ist ein Wort, das ich noch nicht benutzen würde."
        user "Wir müssten mehr an unserem Zusammenhalt arbeiten. Vielleicht eine Gruppenübung oder der gleichen"

    else:
        # Score ist 0 oder 1 -> Schlechter Tag
        user "Als der Wecker klingelte konnte ich nur grummeln."
        user "Ich zog die Decke über den Kopf und wollte gar nicht aufstehen."
        user "Gestern war eine absolute Katastrophe."
        user "Das pure Chaos. Wenn ich daran denke, zieht sich mein Magen zusammen."
        user "Ich weiß wirklich nicht wie ich das verbessern sollte."

    ## 3. DETAILLIERTE ANALYSE (Wer hat Mist gebaut?)
    ## Hier prüfen wir: War es FAIL (Falsch geholfen) oder IGNORED (Nicht geholfen)?
    stop audio fadeout 1.0
    user "Während ich mich anzog, gingen mir die Gesichter von gestern durch den Kopf..."
    
    scene bg cafe with fade
    show vignette3 with dissolve
    play music "audio/Silly_Music.mp3" fadein 1.0 volume 0.75

    # --- LAVAN CHECK ---
    if task_result_lavan == "fail":
        show lavan angry at middle
        user "Lavan war den ganzen Tag wütend, weil ich ihn wie ein Kind behandelt habe."
        hide lavan with dissolve
    elif task_result_lavan == "ignored":
        show lavan angry at middle
        user "Und die arme Espressomaschine... Lavan hat sie fast verprügelt."
        user "Er war so gestresst, dass der halbe Kaffee daneben ging, aber niemand hatte auch Zeit ihm zu helfen."
        hide lavan with dissolve
    elif task_result_lavan == "success":
        show lavan happy at middle
        user "Nachdem er seine Wut runtergeschluckt hatte, war er wiklich professionell."
        hide lavan with dissolve

    # --- MACOI CHECK ---
    if task_result_macoi == "fail":
        show macoi angry at middle_m
        user "Macoi war nach meiner Ansage völlig durch den Wind."
        user "Er hat sich komplett abgekapselt."
        hide macoi with dissolve
    elif task_result_macoi == "ignored":
        show macoi neutral at middle_m
        user "Bei Macoi hat das System komplett ausgesetzt."
        user "Er hat bestimmt drei Bestellungen falsch aufgenommen, weil er im Halbschlaf war und ich ihn nicht wachgerüttelt habe."
        hide macoi with dissolve
    elif task_result_macoi == "success":
        show macoi happy at middle_m
        user "Er war überraschend wach und konzentriert. Hat er vielleicht Übung in Cooking Mama?"
        hide macoi with dissolve

    # --- VELVETTE CHECK ---
    if task_result_velvette == "fail":
        show velvette angry at middle_vel
        user "Velvette war zickig zu den Kunden, nachdem ich sie vor allen bloßgestellt habe."
        hide velvette with dissolve
    elif task_result_velvette == "ignored":
        show velvette neutral at middle_vel
        user "Es gab Beschwerden über eine 'arrogante Kellnerin'. Ich hätte bei Velvette eingreifen sollen."
        hide velvette with dissolve
    elif task_result_velvette == "success":
        show velvette happy at middle_vel
        user "Velvette war der Wahnsinn, ich konnte garnicht ahnen das sie so ein Naturtalent ist."
        hide velvette with dissolve

    # --- CINO CHECK ---
    if task_result_cino == "fail":
        show cino sad at middle
        user "Und überall lagen zerrissene Servietten herum..cino."
        hide cino with dissolve
    elif task_result_cino == "ignored":
        show cino sad at middle
        user "Er sah so verloren aus, wie ein zurückgelassener Welpe."
        hide cino with dissolve
    elif task_result_cino == "success":
        show cino happy at middle
        user "Er war wirklich beliebt bei den Kunden, sehr nett, die Leute lieben ihn."
        hide cino with dissolve


    # ---------------------------------------------------------
    # Quasi Reflektion / Fazit
    # ---------------------------------------------------------
    hide lavan
    hide macoi
    hide velvette
    hide cino
    hide vignette3
    scene bg Flur with fade

    if day_score >= 3:
        # FAZIT: GUT
        user "Aber egal. Heute ist ein neuer Tag. Hoffentlich läuft es heute genauso gut."
        user "Ich öffnete die Tür und hüpfte die Treppe fast schon hinunter. Es roch lecker nach Kaffee."

    elif day_score == 2:
        # FAZIT: OKAY
        user "Ich seufzte. Ich muss das heute besser machen. Ein bisschen mehr Struktur würde uns gut tun."
        user "Ich schlurfte die Treppe hinunter. Hoffentlich ist noch Kaffee übrig."

    else:
        # FAZIT: SCHLECHT
        user "Ich muss das heute retten. Dringend."
        user "Mit einem flauen Gefühl im Magen ging ich langsam die Treppe hinunter, als würde ich zum Hinrichtung gehen."

    # ---------------------------------------------------------
    # IN DER KÜCHE (Interaktion)
    # ---------------------------------------------------------

    scene bg kitchen2 with fade

    user "Als ich die Küche betrat, saßen alle schon am Tisch."

    # --- GUTER TAG ---
    if day_score >= 3:
        show cino happy at left
        show lavan happy at right
        user "Die Stimmung war entspannt. Cino summte, Lavan wirkte konzentriert und selbst Velvette nickte mir zu."
        user "\"Morgen, Team!\""
        c "\"Guten Morgen, [player_name]! Wir sind bereit für Runde zwei!\""
        l "\"Pff. Ich bin immer bereit.\""

    # --- OKAY TAG ---
    elif day_score == 2:
        show macoi neutral at left_m
        show velvette angry at right_vel
        user "Es war still. Man hörte nur das Klappern von Löffeln. Die Anspannung von gestern hing noch leicht in der Luft."
        user "\"Morgen.\""
        m "\"Mhm...\""
        v "\"Ich hoffe, du hast heute einen besseren Plan als gestern.\""
        user "\"Wir kriegen das hin.\""
        

    # --- SCHLECHTER TAG ---
    else:
        show lavan angry at left
        show velvette angry at right_vel
        user "Die Luft war zum Schneiden dick. Lavan funkelte mich an, Velvette drehte sich weg."
        user "\"Guten Morgen...\" versuchte ich es vorsichtig."

        v "\"Spar dir das. Mein Kopf tut weh von dem Lärm gestern.\""
        l "\"Wenn das heute wieder so läuft, explodiert hier nicht nur die Kaffeemaschine.\""
        user "Okay... das wird hart."

    # ---------------------------------------------------------
    # DIE ANKÜNDIGUNG (Einkaufszentrum Trip)
    # ---------------------------------------------------------

    hide lavan with dissolve
    hide velvette with dissolve
    hide cino with dissolve
    hide macoi with dissolve

    user "Ich räusperte mich, um ihre Aufmerksamkeit zu bekommen."

    show cino neutral at posi_3
    show macoi neutral at posi_1
    show velvette neutral at posi_2
    show lavan neutral at posi_4

    user "\"Hört zu. Morgen ist Wochenende. Das bedeutet, heute machen wir nur eine kurze Schicht bis 14 Uhr.\""

    if day_score >= 3:
        # BELOHNUNG
        user "\"Und weil ihr gestern so einen tollen Job gemacht habt, habe ich eine Belohnung geplant.\""
        user "\"Wir gehen danach alle zusammen ins Einkaufszentrum. Shoppen, Essen, Spaß haben. Auf meine Kosten.\""
        show cino happy with dissolve
        c "\"Jaaaa! Shoppen!\""
        show velvette happy with dissolve
        v "\"Endlich eine vernünftige Entscheidung. Ich brauche dringend neue Ohrringe.\""

    elif day_score == 2:
        # ZWISCHENLÖSUNG
        user "\"Danach gehen wir ins Einkaufszentrum. Wir müssen alle mal rauskommen und den Kopf freikriegen.\""
        user "\"Ich lade euch auf ein Essen ein. Ein bisschen Entspannung tut uns gut. Und vorallem stärkt es unseren Teamgeist.\""
        show macoi happy with dissolve
        m "\"Essen klingt gut...\""
        l "\"Von mir aus. Besser als hier rumzuhocken.\""

    else:
        # TEAMBUILDING (ZWANG)
        user "\"Und da gestern... nun ja... optimierungsbedürftig war, ist das heute Pflichtprogramm.\""
        user "\"Wir gehen ins Einkaufszentrum. Teambuilding. Wir müssen lernen, miteinander klarzukommen, ohne, dass der Laden abbrennt.\""
        show lavan angry with dissolve 
        l "\"Teambuilding? Dein Ernst?\""
        user "\"Ja, mein Ernst. Keine Widerrede. Wir müssen ein Team werden.\""
        user "\"Außerdem müssen wir ein paar Sachen holen UND ihr könnt auch sehen wie andere in eurem Feld sich bei Kunden verhalten.\""
        user "\"Nimmt es als eine Art Übung auf.\""

    scene black with fade
    stop music fadeout 3.0

    jump story_intro_04
