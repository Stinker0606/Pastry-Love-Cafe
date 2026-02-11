label story_intro_04:

    label shopping_mall_scene:

    scene bg mall with fade
    play music "audio/Mall_Ambience.mp3" fadein 1.5

    user "Das Einkaufszentrum war voll, laut und bunt. Genau das Gegenteil von unserem stillen Café heute Morgen."

    user "Ich blieb vor dem großen Brunnen im Eingangsbereich stehen."

    user "\"Okay Leute. Der Plan ist folgender: Ich muss dringend noch Deko für das Café besorgen. Ihr habt Freizeit.\""
    user "\"Wir treffen uns in zwei Stunden wieder hier.\""

    # --- DIE WÜNSCHE ---

    # 1. VELVETTE (Fashion)
    user "Velvette scannte bereits die Schaufenster mit einem Kennerblick."
    v "\"Deko... sicher. Aber weißt du, was noch dringender dekoriert werden muss?\""
    user "Sie zeigte mit einem manikürten Finger direkt auf mich."
    v "\"Du. Da hinten ist eine Boutique, die *fast* meinen Standards entspricht. Ich brauche jemanden, der mir Sachen hält. Und vielleicht lasse ich dich auch etwas anprobieren.\""

    # 2. MACOI (Game Movie)
    user "Macoi hingegen starrte wie hypnotisiert auf ein riesiges Filmplakat an der Wand."
    user "Seine Augen, sonst immer halb geschlossen, waren weit aufgerissen. Er wirkte... wach. Wirklich wach."
    m "\"Cyber-Slayer: The Movie...\""
    user "Er flüsterte es fast ehrfürchtig."
    m "\"Die Kritiken sagen, sie haben die Lore ruiniert. Ich muss es sehen. Ich muss mich darüber aufregen. Sofort.\""

    # 3. LAVAN (Romance Movie - versteckt)
    user "Lavan stand ebenfalls vor den Kinoplakaten, rümpfte aber die Nase über Macois Wahl."
    l "\"Videospiele... Kinderkram. Wenn wir schon ins Kino gehen, dann in etwas mit Substanz.\""
    user "Sein Blick huschte immer wieder zu einem Plakat mit einem sehr kitschigen Sonnenuntergang und einem sich küssenden Paar: *'Liebe im Sturm'.*"
    user "\"Du willst 'Liebe im Sturm' sehen, Lavan?\""
    l "\"WAS?! Nein! Ich rede von... der... der kinematographischen Ästhetik!\""
    user "Er lief rot an und wedelte wild mit den Händen."
    l "\"Es geht um die Charakterentwicklung! Und die... Lichtverhältnisse! Das verstehst du nicht! Aber jemand muss ja mitkommen, um den Film objektiv zu bewerten!\""

    # 4. CINO (Bummeln)
    user "Cino drehte sich währenddessen im Kreis und staunte über die gläserne Decke."
    c "\"Wow! So viele Lichter! Und es riecht nach Popcorn und Parfüm gleichzeitig!\""
    c "\"Ich will einfach überall rein! In den Spielzeugladen! In den Kerzenladen! Und da hinten gibt es Eis! [player_name], komm, wir erkunden einfach alles!\""

    user "Ich sah in die Runde. Vier erwartungsvolle Gesichter (auch wenn zwei davon so taten, als wäre es ihnen egal)."
    user "Ich kann mich nicht zerteilen. Ich muss mich entscheiden."

    menu:
        "Mit Velvette in die Boutique gehen":
            call _add_affection(LI_VELVETTE, 1)
            $ cinema_date = "false"
            jump mall_date_velvette

        "Mit Lavan in den Liebesfilm gehen":
            call _add_affection(LI_LAVAN, 1)
            $ cinema_date = "true"
            jump mall_date_lavan

        "Mit Macoi in den Gaming-Film gehen":
            call _add_affection(LI_MACOI, 1)
            $ cinema_date = "true"
            jump mall_date_macoi

        "Mit Cino bummeln gehen":
            call _add_affection(LI_CINO, 1)
            $ cinema_date = "false"
            jump mall_date_cino

# -------------------------------------------------------------------------
# velvette date
# -------------------------------------------------------------------------
label mall_date_velvette:
    user "\"Ich komme mit dir, Velvette. Jemand muss ja aufpassen, dass du den Laden nicht kaufst.\""

    v "\"Eine weise Entscheidung. Komm, Darling. Wir haben Arbeit vor uns.\""

    scene bg boutique with fade

    user "Eine halbe Stunde später stand ich in einer Umkleidekabine, während Velvette mir Kleidungsstücke hineinreichte."

    v "\"Probier das Grüne. Nein, warte. Grün beißt sich mit deiner Aura. Nimm das Blaue.\""

    user "Ich trat heraus. Velvette musterte mich kritisch, legte den Kopf schief und ging langsam um mich herum."
    user "Ich fühlte mich wie ein Gemälde, das begutachtet wird."

    user "\"Und? Urteil?\""

    v "\"Hmpf.\""
    user "Sie trat näher an mich heran und zupfte den Kragen zurecht. Ihre Berührung war überraschend sanft."

    v "\"Es ist... akzeptabel. Es betont deine Augen.\""
    user "Sie traf meinen Blick im Spiegel und lächelte. Ein echtes, kleines Lächeln, nicht ihr übliches Grinsen."

    v "\"Du siehst gut aus. Fast so gut wie ich. Aber gewöhn dich nicht daran, dass ich dir Komplimente mache.\""

    user "Wir kauften das Teil (und Deko für den Laden, die Velvette aussuchte, weil mein Geschmack 'fragwürdig' sei)."

    jump mall_reunite

# -------------------------------------------------------------------------
# lavan date
# -------------------------------------------------------------------------
label mall_date_lavan:
    user "\"Okay, Lavan. Lass uns die... 'Lichtverhältnisse' in diesem Film analysieren.\""

    l "\"Gute Wahl. Du wirst sehen, man kann viel lernen. Rein akademisch natürlich.\""

    scene bg cinema with fade

    user "Wir saßen im dunklen Kinosaal. Der Film war triefend kitschig. Die Heldin rannte im Regen dem Helden hinterher."

    user "Ich schielte zu Lavan rüber. Er starrte gebannt auf die Leinwand. Er hatte vergessen, seine Popcorn zu essen."

    l "(flüsternd) \"Warum rennt sie nicht schneller? Der Zug fährt gleich ab! Das ist dramaturgisch völlig unlogisch!\""

    user "\"Lavan... weinst du?\""

    l "\"WAS?! Nein!\""
    user "Er wischte sich hastig über die Augen."
    l "\"Es ist die Klimaanlage! Sie bläst mir direkt ins Auge! Und... und das Licht ist einfach zu grell!\""

    user "Auf der Leinwand küsste sich das Paar endlich. Lavan schniefte leise."

    user "Ich griff in die Popcorn-Tüte, und unsere Hände berührten sich. Lavan zuckte zusammen, zog seine Hand aber nicht weg."

    l "\"Tsk. Iss ruhig. Ich kann mich bei dem Kitsch eh nicht auf Essen konzentrieren...\""
    user "Er drückte meine Hand ganz kurz, bevor er sie losließ."

    jump mall_reunite

# -------------------------------------------------------------------------
# Macoi Date
# -------------------------------------------------------------------------
label mall_date_macoi:
    user "\"Macoi, ich will sehen, wie sehr sie die Lore ruiniert haben. Ich komm mit.\""

    m "\"Ja! Endlich jemand mit Kultur.\""
    user "Er packte mich fast schon am Arm und zog mich Richtung Kasse. So schnell hatte ich ihn noch nie gesehen."

    scene bg cinema with fade

    user "Der Film war laut, bunt und voller Explosionen. Für mich war es reines Chaos."
    user "Aber für Macoi war es eine Offenbarung."

    user "Er lehnte sich immer wieder zu mir rüber und flüsterte mir Erklärungen ins Ohr. Sein Gesicht war im Licht der Leinwand hellwach."

    m "\"Siehst du das Schwert? Im Spiel kriegst du das erst nach 50 Stunden Grind. Hier hat er es in Szene 1. Lächerlich. Aber die Grafik ist geil.\""

    user "Ich hörte ihm lieber zu als dem Film. Seine Begeisterung war ansteckend."

    user "\"Du magst das Spiel wirklich, oder?\""

    m "\"Es ist... meine Welt. Wenn die echte Welt zu laut ist.\""
    user "Er sah mich an, und für einen Moment vergaß er den Film."

    m "\"Aber es ist cool, dass du mitgekommen bist. Alleine nerden macht nur halb so viel Spaß. Hier, nimm meine Nachos. Die mit dem Käse.\""
    user "Er schob mir die Schale hin. Von Macoi war das der ultimative Liebesbeweis."

    jump mall_reunite

# -------------------------------------------------------------------------
# Cino Date
# -------------------------------------------------------------------------
label mall_date_cino:
    user "\"Ich glaube, ich brauche etwas Bewegung. Komm Cino, wir ziehen los.\""

    c "\"Juhu! Abenteuerzeit!\""

    scene bg mall with fade

    user "Es war weniger ein gezieltes Einkaufen und mehr ein Zick-Zack-Lauf durch alle möglichen Läden."
    user "Wir rochen an Duftkerzen (Cino musste niesen), probierten lustige Sonnenbrillen auf und standen lange vor einem Tierladen."

    user "Schließlich landeten wir in einem Deko-Laden."

    c "\"Oh! [player_name], guck mal!\""
    user "Er hielt eine kleine, leuchtende Figur hoch. Es war eine Katze, die eine Kaffeetasse hielt."

    c "\"Die sieht aus wie wir! Also... wie das Café! Können wir die holen? Als Glücksbringer?\""

    user "\"Sie passt eigentlich gar nicht zum Stil...\""

    c "\"Bitteeee! Sie passt zu uns, weil sie fröhlich ist!\""
    user "Er schaute mich mit diesen unwiderstehlichen Hundeaugen an."

    user "\"Na gut. Gekauft.\""

    c "\"Ja!\""
    user "Er umarmte mich stürmisch mitten im Laden."
    c "\"Das wird unser Maskottchen! Danke! Das ist der beste Ausflug aller Zeiten!\""

    jump mall_reunite

# -------------------------------------------------------------------------
# Kommen wieder zusammen
# -------------------------------------------------------------------------
label mall_reunite:

    scene bg mall with fade

    user "Zwei Stunden später trafen wir uns alle wieder am Brunnen."

    user "Ich hatte meine Deko-Tüten (und vielleicht ein paar Extras) in der Hand."

    if cinema_date == "false":
        user "Lavan und Macoi kamen aus dem Kino. Sie stritten immer noch."
        l "\"Der Film hatte null emotionale Tiefe!\""
        m "\"Er hatte Laser-Drachen. Dein Argument ist ungültig.\""

    user "\"Alle glücklich? Alle bereit für den Heimweg?\""

    v "\"Meine Füße tun weh. Ich verlange einen sehr bequemen Sitz im Auto.\""
    c "\"Ich hab Hunger! Können wir die Deko essen? Nein? Okay...\""

    user "Ich lachte. Es fühlte sich gut an."
    user "Vielleicht wird das mit dem Café doch was. Wir sind ein seltsamer Haufen, aber irgendwie... passt es."


    return
