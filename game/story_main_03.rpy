label story_intro_03:
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

    user "Während ich mich anzog, gingen mir die Gesichter von gestern durch den Kopf..."

    # --- LAVAN CHECK ---
    if task_result_lavan == "fail":
        user "Lavan war den ganzen Tag wütend, weil ich ihn wie ein Kind behandelt habe."
    elif task_result_lavan == "ignored":
        user "Und die arme Espressomaschine... Lavan hat sie fast verprügelt."
        user "Er war so gestresst, dass der halbe Kaffee daneben ging, aber niemand hatte auch Zeit ihm zu helfen."

    # --- MACOI CHECK ---
    if task_result_macoi == "fail":
        user "Macoi war nach meiner Ansage völlig durch den Wind."
        user "Er hat sich komplett abgekapselt."
    elif task_result_macoi == "ignored":
        user "Bei Macoi hat das System komplett ausgesetzt."
        user "Er hat bestimmt drei Bestellungen falsch aufgenommen, weil er im Halbschlaf war und ich ihn nicht wachgerüttelt habe."

    # --- VELVETTE CHECK ---
    if task_result_velvette == "fail":
        user "Velvette war zickig zu den Kunden, nachdem ich sie vor allen bloßgestellt habe."
    elif task_result_velvette == "ignored":
        user "Es gab Beschwerden über eine 'arrogante Kellnerin'. Ich hätte bei Velvette eingreifen sollen."

    # --- CINO CHECK ---
    if task_result_cino == "fail":
        user "Und überall lagen zerrissene Servietten herum..."
    elif task_result_cino == "ignored":
        user "Er sah so verloren aus, wie ein zurückgelassener Welpe"


    # ---------------------------------------------------------
    # Quasi Reflektion / Fazit
    # ---------------------------------------------------------

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
        user "Mit einem flauen Gefühl im Magen ging ich langsam die Treppe hinunter, als würde ich zum Schafott gehen."

    # ---------------------------------------------------------
    # IN DER KÜCHE (Interaktion)
    # ---------------------------------------------------------

    scene bg_kitchen with dissolve
    user "Als ich die Küche betrat, saßen alle schon am Tisch."

    # --- GUTER TAG ---
    if day_score >= 3:
        user "Die Stimmung war entspannt. Cino summte, Lavan wirkte konzentriert und selbst Velvette nickte mir zu."
        user "\"Morgen, Team!\""
        c "\"Guten Morgen, [player_name]! Wir sind bereit für Runde zwei!\""
        l "\"Pff. Ich bin immer bereit.\""

    # --- OKAY TAG ---
    elif day_score == 2:
        user "Es war still. Man hörte nur das Klappern von Löffeln. Die Anspannung von gestern hing noch leicht in der Luft."
        user "\"Morgen.\""
        m "\"Mhm...\""
        v "\"Ich hoffe, du hast heute einen besseren Plan als gestern.\""
        user "\"Wir kriegen das hin.\""

    # --- SCHLECHTER TAG ---
    else:
        user "Die Luft war zum Schneiden dick. Lavan funkelte mich an, Velvette drehte sich weg."
        user "\"Guten Morgen...\" versuchte ich es vorsichtig."

        v "\"Spar dir das. Mein Kopf tut weh von dem Lärm gestern.\""
        l "\"Wenn das heute wieder so läuft, explodiert hier nicht nur die Kaffeemaschine.\""
        user "Okay... das wird hart."

    # ---------------------------------------------------------
    # DIE ANKÜNDIGUNG (Einkaufszentrum Trip)
    # ---------------------------------------------------------

    user "Ich räusperte mich, um ihre Aufmerksamkeit zu bekommen."
    user "\"Hört zu. Morgen ist Wochenende. Das bedeutet, heute machen wir nur eine kurze Schicht bis 14 Uhr.\""

    if day_score >= 3:
        # BELOHNUNG
        user "\"Und weil ihr gestern so einen tollen Job gemacht habt, habe ich eine Belohnung geplant.\""
        user "\"Wir gehen danach alle zusammen ins Einkaufszentrum. Shoppen, Essen, Spaß haben. Auf meine Kosten.\""
        c "\"Jaaaa! Shoppen!\""
        v "\"Endlich eine vernünftige Entscheidung. Ich brauche dringend neue Ohrringe.\""

    elif day_score == 2:
        # ZWISCHENLÖSUNG
        user "\"Danach gehen wir ins Einkaufszentrum. Wir müssen alle mal rauskommen und den Kopf freikriegen.\""
        user "\"Ich lade euch auf ein Essen ein. Ein bisschen Entspannung tut uns gut. Und vorallem stärkt es unseren team Geist.\""
        m "\"Essen klingt gut...\""
        l "\"Von mir aus. Besser als hier rumzuhocken.\""

    else:
        # TEAMBUILDING (ZWANG)
        user "\"Und da gestern... nun ja... optimierungsbedürftig war, ist das heute Pflichtprogramm.\""
        user "\"Wir gehen ins Einkaufszentrum. Teambuilding. Wir müssen lernen, miteinander klarzukommen, ohne dass der Laden abbrennt.\""
        l "\"Teambuilding? Dein Ernst?\""
        user "\"Ja, mein Ernst. Keine Widerrede. Wir müssen ein Team werden.\""
        user "\"Außerdem müssen wir ein paar Sachen holen UND ihr könnt auch sehen wie andere in eurem Feld sich bei kunden verhalten\""
        user "\"Nemmt es als eine Art Theorie Übung auf.\""

    if task_result_cino == "fail":
        user "leck meine eier"
    elif task_result_cino == "ignored":
        user "deine mutter"
    elif task_result_cino == "success":
        user "uwu"

    if day_score < 2:
        user "Mama"

        c "I know"
    else:
        user "puta madre"

        c "oki doki"

    jump story_intro_04
