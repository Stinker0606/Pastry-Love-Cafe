label story_intro_04:

    label shopping_mall_scene:

    scene bg mall with fade
    play music "audio/Mall_Ambience.mp3" fadein 0.5

    user "Das Einkaufszentrum war voll, laut und bunt. Genau das Gegenteil von unserem stillen Café heute Morgen."

    user "Ich blieb vor dem großen Brunnen im Eingangsbereich stehen."

    user "\"Okay Leute. Der Plan ist folgender: Ich muss dringend noch Deko für das Café besorgen. Ihr habt Freizeit.\""
    user "\"Wir treffen uns in zwei Stunden wieder hier.\""

    # --- DIE WÜNSCHE ---

    # 1. VELVETTE (Fashion)
    user "Velvette scannte bereits die Schaufenster mit einem Kennerblick."
    show velvette happy at middle_vel
    v "\"Deko... sicher. Aber weißt du, was noch dringender dekoriert werden muss?\""
    user "Sie zeigte mit einem manikürten Finger direkt auf mich."
    v "\"Du. Da hinten ist eine Boutique, die FAST meinen Standards entspricht. Ich brauche jemanden, der mir Sachen hält. Und vielleicht lasse ich dich auch etwas anprobieren.\""
    hide velvette with dissolve

    # 2. MACOI (Game Movie)
    user "Macoi hingegen starrte wie hypnotisiert auf ein riesiges Filmplakat an der Wand."
    user "Seine Augen, sonst immer halb geschlossen, waren weit aufgerissen. Er wirkte... wach. Wirklich wach."
    show macoi happy at middle_m
    m "\"Cyber-Slayer: The Movie...\""
    user "Er flüsterte es fast ehrfürchtig."
    m "\"Die Kritiken sagen, sie haben die Lore ruiniert. Ich muss es sehen. Ich muss mich darüber aufregen. Sofort.\""
    show macoi happy at right_m with move

    # 3. LAVAN (Romance Movie - versteckt)
    show lavan neutral at left
    user "Lavan stand ebenfalls vor den Kinoplakaten, rümpfte aber die Nase über Macois Wahl."
    l "\"Videospiele... Kinderkram. Wenn wir schon ins Kino gehen, dann in etwas mit Substanz.\""
    user "Sein Blick huschte immer wieder zu einem Plakat mit einem sehr kitschigen Sonnenuntergang und einem sich küssenden Paar: 'Liebe im Sturm'."
    user "\"Du willst 'Liebe im Sturm' sehen, Lavan?\""
    show lavan angry at left with dissolve
    l "\"WAS?! Nein! Ich rede von... der... der kinematographischen Ästhetik!\""
    show lavan blush at left with dissolve
    user "Er lief rot an und wedelte wild mit den Händen."
    l "\"Es geht um die Charakterentwicklung! Und die... Lichtverhältnisse! Das verstehst du nicht! Aber jemand muss ja mitkommen, um den Film objektiv zu bewerten!\""
    hide macoi with dissolve
    hide lavan with dissolve


    # 4. CINO (Bummeln)
    user "Cino drehte sich währenddessen im Kreis und staunte über die gläserne Decke."
    show cino happy at middle
    c "\"Wow! So viele Lichter! Und es riecht nach Popcorn und Parfüm gleichzeitig!\""
    c "\"Ich will einfach überall rein! In den Spielzeugladen! In den Kerzenladen! Und da hinten gibt es Eis! [player_name], komm, wir erkunden einfach alles!\""
    hide cino with dissolve

    user "Ich sah in die Runde. Vier erwartungsvolle Gesichter, auch wenn zwei davon so taten, als wäre es ihnen egal."
    user "Ich kann mich nicht zerteilen. Ich muss mich entscheiden."

    $ quick_menu = False

    menu:
        "Mit Velvette in die Boutique gehen":
            $ mall_date_choice = "Velvette"
            call _add_affection(LI_VELVETTE, 1)
            $ cinema_date = "false"
            $ quick_menu = True
            jump mall_date_velvette

        "Mit Lavan in den Liebesfilm gehen":
            $ mall_date_choice = "Lavan"
            call _add_affection(LI_LAVAN, 1)
            $ cinema_date = "true"
            $ quick_menu = True
            jump mall_date_lavan

        "Mit Macoi in den Gaming-Film gehen":
            $ mall_date_choice = "Macoi"            
            call _add_affection(LI_MACOI, 1)
            $ cinema_date = "true"
            $ quick_menu = True
            jump mall_date_macoi

        "Mit Cino bummeln gehen":
            $ mall_date_choice = "Cino"
            call _add_affection(LI_CINO, 1)
            $ cinema_date = "false"
            $ quick_menu = True
            jump mall_date_cino

# -------------------------------------------------------------------------
# velvette date
# -------------------------------------------------------------------------
label mall_date_velvette:
    user "\"Ich komme mit dir, Velvette. Jemand muss ja aufpassen, dass du den Laden nicht kaufst.\""

    show velvette happy at middle_vel

    v "\"Eine weise Entscheidung. Komm, Darling. Wir haben Arbeit vor uns.\""

    scene bg boutique with fade

    user "Eine halbe Stunde später stand ich in einer Umkleidekabine, während Velvette mir Kleidungsstücke hineinreichte."

    show velvette happy at middle_vel

    v "\"Probier das Grüne. Nein, warte. Grün beißt sich mit deiner Aura. Nimm das Blaue.\""

    user "Ich trat heraus. Velvette musterte mich kritisch, legte den Kopf schief und ging langsam um mich herum."
    user "Ich fühlte mich wie ein Gemälde, das begutachtet wird."

    user "\"Und? Urteil?\""

    show velvette blush with dissolve

    v "\"Hmpf.\""
    user "Sie trat näher an mich heran und zupfte den Kragen zurecht. Ihre Berührung war überraschend sanft."

    v "\"Es ist... akzeptabel. Es betont deine Augen.\""
    user "Sie traf meinen Blick im Spiegel und lächelte. Ein echtes, kleines Lächeln, nicht ihr übliches Grinsen."

    v "\"Du siehst gut aus. Fast so gut wie ich. Aber gewöhn dich nicht daran, dass ich dir Komplimente mache.\""

    user "Wir kauften das Teil und Deko für den Laden, die Velvette aussuchte, weil mein Geschmack 'fragwürdig' sei."

    jump mall_reunite

# -------------------------------------------------------------------------
# lavan date
# -------------------------------------------------------------------------
label mall_date_lavan:
    user "\"Okay, Lavan. Lass uns die... 'Lichtverhältnisse' in diesem Film analysieren.\""

    show lavan happy at middle

    l "\"Gute Wahl. Du wirst sehen, man kann viel lernen. Rein akademisch natürlich.\""

    stop music fadeout 2.5

    scene bg cinema with fade

    play music "audio/Romantic_Music.mp3" fadein 0.5 volume 0.75

    user "Wir saßen im dunklen Kinosaal. Der Film war triefend kitschig. Die Heldin rannte im Regen dem Helden hinterher."

    user "Ich schielte zu Lavan rüber. Er starrte gebannt auf die Leinwand. Er hatte vergessen, sein Popcorn zu essen."

    show lavan sad at middle

    l "\"Warum rennt sie nicht schneller? Der Zug fährt gleich ab! Das ist dramaturgisch völlig unlogisch!\" flüsterte er aufgebracht."

    user "\"Lavan... weinst du?\""

    l "\"WAS?! Nein!\""
    user "Er wischte sich hastig über die Augen."
    l "\"Es ist die Klimaanlage! Sie bläst mir direkt ins Auge! Und... und das Licht ist einfach zu grell!\""

    user "Auf der Leinwand küsste sich das Paar endlich. Lavan schniefte leise."

    user "Ich griff in die Popcorn-Tüte, und unsere Hände berührten sich. Lavan zuckte zusammen, zog seine Hand aber nicht weg."

    show lavan blush with dissolve

    l "\"Tsk. Iss ruhig. Ich kann mich bei dem Kitsch eh nicht auf Essen konzentrieren...\""
    user "Er drückte meine Hand ganz kurz, bevor er sie losließ."

    stop music fadeout 1.5

    jump mall_reunite

    # -------------------------------------------------------------------------
    # Macoi Date
    # -------------------------------------------------------------------------
label mall_date_macoi:
    user "\"Macoi, ich will sehen, wie sehr sie die Lore ruiniert haben. Ich komm mit.\""

    show macoi happy at middle_m

    m "\"Ja! Endlich jemand mit Kultur.\""
    user "Er packte mich fast schon am Arm und zog mich Richtung Kasse. So schnell hatte ich ihn noch nie gesehen."

    stop music fadeout 2.5

    scene bg cinema with fade

    play music "audio/Movie_Soundeffect.mp3" fadein 0.5 volume 0.75

    user "Der Film war laut, bunt und voller Explosionen. Für mich war es reines Chaos."
    user "Aber für Macoi war es eine Offenbarung."

    user "Er lehnte sich immer wieder zu mir rüber und flüsterte mir Erklärungen ins Ohr. Sein Gesicht war im Licht der Leinwand hellwach."

    show macoi happy at middle_m

    m "\"Siehst du das Schwert? Im Spiel kriegst du das erst nach 50 Stunden Grind. Hier hat er es in Szene 1. Lächerlich. Aber die Grafik ist geil.\""

    user "Ich hörte ihm lieber zu als dem Film. Seine Begeisterung war ansteckend."

    user "\"Du magst das Spiel wirklich, oder?\""

    m "\"Es ist... meine Welt. Wenn die echte Welt zu laut ist.\""

    show macoi blush with dissolve

    user "Er sah mich an, und für einen Moment vergaß er den Film."

    m "\"Aber es ist cool, dass du mitgekommen bist. Alleine nerden macht nur halb so viel Spaß. Hier, nimm meine Nachos. Die mit dem Käse.\""
    user "Er schob mir die Schale hin. Von Macoi war das der ultimative Liebesbeweis."

    stop music fadeout 1.5

    jump mall_reunite

    # -------------------------------------------------------------------------
    # Cino Date
    # -------------------------------------------------------------------------
label mall_date_cino:
    user "\"Ich glaube, ich brauche etwas Bewegung. Komm Cino, wir ziehen los.\""

    show cino happy at middle

    c "\"Juhu! Abenteuerzeit!\""

    scene bg mall with fade

    user "Es war weniger ein gezieltes Einkaufen und mehr ein Zick-Zack-Lauf durch alle möglichen Läden."
    user "Wir rochen an Duftkerzen, welche Cino zum niesen brachten, probierten lustige Sonnenbrillen auf und standen lange vor einem Tierladen."

    user "Schließlich landeten wir in einem Deko-Laden."

    show cino happy at middle

    c "\"Oh! [player_name], guck mal!\""
    user "Er hielt eine kleine, leuchtende Figur hoch. Es war eine Katze, die eine Kaffeetasse hielt."

    c "\"Die sieht aus wie wir! Also... wie das Café! Können wir die holen? Als Glücksbringer?\""

    user "\"Sie passt eigentlich gar nicht zum Stil...\""

    show cino sad with dissolve

    c "\"Bitteeee! Sie passt zu uns, weil sie fröhlich ist!\""
    user "Er schaute mich mit diesen unwiderstehlichen Hundeaugen an."

    user "\"Na gut. Gekauft.\""

    show cino blush with dissolve

    c "\"Ja!\""
    user "Er umarmte mich stürmisch mitten im Laden."
    c "\"Das wird unser Maskottchen! Danke! Das ist der beste Ausflug aller Zeiten!\""

    jump mall_reunite

    # -------------------------------------------------------------------------
    # Kommen wieder zusammen
    # -------------------------------------------------------------------------
label mall_reunite:

    if cinema_date == "true":
        play music "audio/Mall_Ambience.mp3" fadein 0.5

    scene bg mall with fade

    user "Zwei Stunden später trafen wir uns alle wieder am Brunnen."

    user "Ich hatte meine Deko-Tüten und vielleicht ein paar Extras in der Hand."

    if cinema_date == "false":
        show macoi angry at left_m
        show lavan sad at right
        user "Lavan und Macoi kamen aus dem Kino. Sie stritten immer noch."
        show lavan angry with dissolve
        l "\"Der Film hatte null emotionale Tiefe!\""
        m "\"Er hatte Laser-Drachen. Dein Argument ist ungültig.\""
        hide macoi with dissolve
        hide lavan with dissolve

    user "\"Alle glücklich? Alle bereit für den Heimweg?\""

    show velvette neutral at middle_vel

    v "\"Meine Füße tun weh. Ich verlange einen sehr bequemen Sitz im Auto.\""
    show velvette neutral at right_vel with move

    show cino sad at left

    c "\"Ich hab Hunger! Können wir die Deko essen? Nein? Okay...\""

    user "Ich lachte. Es fühlte sich gut an."
    user "Vielleicht wird das mit dem Café doch was. Wir sind ein seltsamer Haufen, aber irgendwie... passt es."

    stop music fadeout 2.5

    scene black with fade

    user "Ich ließ mich rücklings auf mein Bett fallen und starrte die Decke an."

    play music "audio/Romantic_Music.mp3" fadein 0.5 volume 0.75

    user "Meine Füße pochten ein wenig von der Lauferei, aber es war ein angenehmer Schmerz."

    user "Das Einkaufszentrum... der Lärm, die vielen Menschen, das Chaos mit den Vieren."

    user "Es war anstrengend. Aber es war auch... schön."

    user "Ich drehte mich auf die Seite und zog die Decke bis zum Kinn."

    user "Vor allem dieser eine Moment ging mir nicht mehr aus dem Kopf."

    # ---------------------------------------------------------
    # REFLEKTION JE NACH DATE-PARTNER
    # ---------------------------------------------------------

    # --- REFLEKTION LAVAN ---
    if mall_date_choice == "Lavan":
        scene bg cinema with fade             # BACKGROUND
        show lavan blush at middle          # Char kannst du wählen wann er gezeigt wird und wie. Im 01_definitions stehen die verschiedenen faces.
        show vignette3 with dissolve
        user "Lavan im Kino..."
        user "Er hat so getan, als würde er den Film hassen. Als wäre es Folter für ihn."
        user "Aber ich habe gesehen, wie er sich die Augen gewischt hat."
        user "Und als sich unsere Hände im Popcorn berührt haben... er hat nicht zurückgezogen."
        user "Er hat sogar kurz zugedrückt."
        user "Vielleicht ist er gar nicht so stachelig, wie er immer tut. Vielleicht braucht er nur jemanden, der sich nicht an seinen Dornen stört."
        user "Ein kleines Lächeln stahl sich auf meine Lippen. Sein Gesicht, als er rot wurde... niedlich."


    # --- REFLEKTION VELVETTE ---
    elif mall_date_choice == "Velvette":
        scene bg boutique with fade
        show velvette blush at middle_vel
        show vignette3 with dissolve
        user "Velvette in der Boutique..."
        user "Ich musste grinsen. Sie hat mich herumkommandiert wie eine Anziehpuppe."
        user "Aber da war dieser eine Moment vor dem Spiegel."
        user "Sie hat mich nicht als Projekt gesehen. Sie hat *mich* angesehen."
        user "Ihr Kompliment war echt. Hinter all dem Glitzer und der Arroganz steckt jemand, der einfach nur Perfektion sucht, auch in Beziehungen."
        user "Und dass sie mich 'akzeptabel' fand... aus ihrem Mund ist das wohl die größte Liebeserklärung."


    # --- REFLEKTION MACOI ---
    elif mall_date_choice == "Macoi":
        scene bg cinema with fade
        show macoi blush at middle_m
        show vignette3 with dissolve
        user "Macoi im Kino..."
        user "Ich habe ihn noch nie so lebendig gesehen. Seine Augen haben geleuchtet."
        user "Normalerweise schläft er im Stehen, aber wenn es um Dinge geht, die er liebt, ist er voll da."
        user "Und er hat seine Nachos mit mir geteilt. Seine heiligen Nachos."
        user "Es hat sich so... natürlich angefühlt. Als würden wir schon immer nebeneinander sitzen."
        user "Er braucht keine großen Worte. Seine Nähe reicht völlig aus."


    # --- REFLEKTION CINO ---
    elif mall_date_choice == "Cino":
        scene bg mall with fade
        show cino blush at middle
        show vignette3 with dissolve
        user "Ich blickte auf den Nachttisch. Da stand sie. Die kleine, kitschige Katzenfigur."
        user "Cino..."
        user "Er ist pures Chaos, aber er ist auch pure Freude."
        user "Wie er durch den Laden gehüpft ist, völlig ohne Scham, einfach nur glücklich, mit mir dort zu sein."
        user "Seine Begeisterung ist ansteckend. Wenn ich bei ihm bin, wird die Welt ein bisschen heller."
        user "Er hat gesagt, das ist unser Maskottchen. 'Unseres'."
        user "Der Gedanke ließ mein Herz schneller schlagen."

    scene black with fade

    stop music fadeout 2.5

    jump story_intro_05
