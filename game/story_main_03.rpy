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
        user "Idk ey schreib hier was UWU."

    ## 4. FAZIT
    if day_score < 2:
        user "Ich muss das heute besser machen."
    else:
        user "Hoffentlich läuft es heute genauso gut."

    return # Oder jump next_scene was du machen willst idk halt
