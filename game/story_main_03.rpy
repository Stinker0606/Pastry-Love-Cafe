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
        user "Ich streckte mich. Gestern lief es eigentlich ziemlich gut."
        user "Der Laden lief, die Kunden waren zufrieden."
        
    elif day_score == 2:
        # Score ist 2 -> Naja Tag
        user "Gestern war... okay. Es gab Höhen und Tiefen."
        
    else:
        # Score ist 0 oder 1 -> Schlechter Tag
        user "Ich wollte gar nicht aufstehen. Gestern war eine Katastrophe."
        user "Das absolute Chaos."

    ## 3. DETAILLIERTE ANALYSE (Wer hat Mist gebaut?)
    ## Hier prüfen wir: War es FAIL (Falsch geholfen) oder IGNORED (Nicht geholfen)?

    # --- LAVAN CHECK ---
    if task_result_lavan == "fail":
        user "Lavan war den ganzen Tag wütend, weil ich ihn wie ein Kind behandelt habe."
    elif task_result_lavan == "ignored":
        user "Die Kaffeemaschine hat den ganzen Tag komische Geräusche gemacht, weil niemand Lavan geholfen hat."

    # --- MACOI CHECK ---
    if task_result_macoi == "fail":
        user "Macoi war total durch den Wind, nachdem ich ihn so angebrüllt habe."
    elif task_result_macoi == "ignored":
        user "Macoi hat bestimmt drei Bestellungen falsch aufgenommen, weil er im Halbschlaf war."

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