## -- TEIL 1: INTRO ---
label story_intro_02:
    ## Wir starten in der Küche oder? - Glaub ja
    scene bg Flur with fade

    ## Intro Monolog
    user "Seitdem sind einige Tage vergangen."

    user "Und jeder einzelne davon war laut."

    user "Als ich an diesem Morgen aufwachte, dröhnte es schon durch die Wände."

    #Sie geht ins Badezimmer und trifft Velvette

    user "Ich schleppte mich ins Badezimmer. Dort stand Velvette, vollkommen in ihrem Element."

    user "Sie schminkte sich, als würde sie sich gerade auf eine Laufstegshow vorbereiten, und ignorierte meine Existenz erfolgreich wie eine echte Diva."

    user "Ich schnappte mir meine Zahnbürste und manövrierte mich geschickt um sie herum"

    $ quick_menu = False

    #--------------
    menu:
        "Einfach Leise mein Ding machen":
            # Hier passiert nichts Besonderes.
            user "Ich beschloss, ihre Konzentration nicht zu stören und putzte leise meine Zähne."

        "Ihr ein Kompliment geben":
            call _add_affection(LI_VELVETTE, 1)
            user "\"Du siehst gut aus.\""

            user "Ohne auch nur ihren Blick vom Spiegel zu lösen, antwortete sie trocken."
            v "\"Ich weiß.\""

    $ quick_menu = True

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

    user "Velvette kam die Treppe herunter, stolz wie eine Königin, die gerade frische Luft mit Parfüm verwechselt hatte."

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

    $ quick_menu = False

    #--------------
    menu:
        "Velvette aufmuntern":
            call _add_affection(LI_VELVETTE, 1)
            user "Ich drehte mich zu Velvette, die immer noch kritisch ihren teigfreien Teller anstarrte."
            user "\"Weißt du, Velvette... eigentlich ist es gut, dass du so wählerisch bist.\""

            v "\"Natürlich ist es das. Aber warum sagst du das?\""

            user "\"Weil unsere Kunden genau diese Art von Standard erwarten. Wenn du am Empfang stehst, wissen sie sofort: Hier gibt es nur das Beste.\""
            user "Ich lächelte sie an."
            user "\"Du bist nicht nur Deko, du bist das Aushängeschild. Zeig ihnen, was Klasse bedeutet.\""

            ##Sprite von Velvette happy oder Blushy
            v "\"Hmpf. Endlich jemand, der meine Vision versteht.\""
            user "Sie straffte die Schultern und warf ihr Haar zurück."
            v "\"Gut. Dann werde ich dafür sorgen, dass dieser Laden glänzt. Jemand muss es ja tun.\""

        "Cino aufmuntern":
            call _add_affection(LI_CINO, 1)
            user "\"Cino, schau mich mal kurz an.\""
            user "Er hielt in seiner nervösen Bewegung inne und sah mich mit großen Augen an."
            user "\"Du musst nicht perfekt sein. Und du musst keine Angst haben, etwas falsch zu machen.\""
            user "\"Deine herzliche Art ist genau das, was dieser Laden braucht. Sei einfach du selbst, okay? Das reicht völlig.\""

            c "\"Einfach nur... ich sein?\""

            user "Ein Stein schien ihm vom Herzen zu fallen und er atmete erleichtert aus."

            c "\"Okay. Puh... Danke, [player_name]. Wenn du das sagst, fühle ich mich gleich viel leichter!\""

        "Lavan aufmuntern":
            call _add_affection(LI_LAVAN, 1)
            user "Ich wandte mich an Lavan, der immer noch finster auf die Kaffeemaschine in der Ecke schielte."
            user "\"Lavan, hör auf, die Maschine anzufunkeln. Sie hat schon Angst vor dir.\""

            l "\"Soll sie auch! Sie muss gehorchen!\""

            user "\"Sie wird gehorchen. Weil du der Einzige bist, der gut genug ist, sie zu bändigen.\""
            user "Ich lehnte mich etwas zu ihm."
            user "\"Ganz ehrlich? Keiner hier macht Kaffee mit so viel... Leidenschaft wie du. Wenn du diese Energie in die Tasse kriegst, statt in die Luft, wird der Kaffee legendär.\""

            ##Sprite von Lavan Blushy
            user "Lavan blinzelte überrascht und sah schnell weg, um sein Grinsen und die leichte röte der wangen zu verbergen zu verbergen."
            l "\"Tsk. Natürlich wird er legendär. Was dachtest du denn?\""
            l "\"Aber... gut. Ich werde mich zusammenreißen. Für den Kaffee.\""

        "Macoi aufmuntern":
            call _add_affection(LI_MACOI, 1)
            user "\"Macoi? Ich weiß, es ist früh. Ich weiß, die Welt ist laut.\""
            user "\"Aber wir ziehen das jetzt durch. Seite an Seite. Und wenn die Schicht vorbei ist, sorge ich dafür, dass du deine Ruhe bekommst.\""

            m "\"Ruhe... klingt gut.\""

            user "Er blinzelte langsam, nickte mir aber dann fast dankbar zu."

    $ quick_menu = True

    #Sprung zum cafe

    scene bg cafe with fade

    user "Eine halbe Stunde später standen wir im Café."

    user "Das Schild an der Tür war noch auf 'Geschlossen' gedreht, aber die Luft im Raum war bereits zum Schneiden dick."

    # Nach einander Charaktere zeigen und dann sagen was sie machen

    user "Lavan stand hinter der Theke und starrte die große Espressomaschine an, als würde er sie zu einem Duell herausfordern."

    user "Cino sortierte Servietten. Wieder und wieder. Ich glaube, er sortierte sie nach 'Falt-Ästhetik'."

    user "Macoi lehnte an der Kasse. Oder besser gesagt: Er hing darüber wie ein nasses Handtuch."

    user "Und Velvette? Sie stand mitten im Raum, perfekt ausgeleuchtet vom einzigen Sonnenstrahl, der durch das Fenster fiel, und checkte ihre Fingernägel."

    user "\"Alle auf Position?\""

    l "\"Die Maschine zischt komisch. Ich traue ihr nicht.\""

    m "\"Ich höre Farben.\""

    v "\"Mein Platz ist hier vorne. Das Licht ist hier am vorteilhaftesten für den ersten Eindruck der Kunden.\""

    user "\"Das ist der Eingangsbereich, Velvette. Du stehst im Weg.\""

    v "\"Ich *bin* der Weg.\""

    user "Ich ignorierte das und ging zur Tür."

    user "\"Okay. Tief durchatmen. Ich drehe das Schild um.\""

    user "Ich drehte das Schild auf 'Geöffnet' und schloss die Tür auf."

    user "Schon nach einer halben Stunde, war das Cafe voll"

    user "Ich beobachtete die Vier wie sie mit ihren Stationen zurecht kamen und war bereit zu helfen"

    ## --- Merken, wer schon Hilfe bekommen hat ---
    ## Alles auf False setzen beim Start des Hubs
    $ helped_velvette = False
    $ helped_macoi = False
    $ helped_lavan = False
    $ helped_cino = False

    jump cafe_opening_decision_hub

    ## --- DAS HUB MENÜ ---
label cafe_opening_decision_hub:

    # Wir berechnen kurz den Status
    # 1. Hat man mind. EINER Person geholfen? (eine ODER-Verknüpfung)
    $ any_help_given = helped_velvette or helped_macoi or helped_lavan or helped_cino

    # 2. Hat man ALLEN geholfen? (eine UND-Verknüpfung)
    $ all_help_given = helped_velvette and helped_macoi and helped_lavan and helped_cino

    user "Was soll ich tun?"

    $ quick_menu = False

    menu:
        # OPTION 1: Backen (Immer da)
        "Etwas Backen (Beendet diese Szene!)":
            $ quick_menu = True
            user "Ich muss backen, sonst haben wir gleich nichts mehr zu verkaufen."
            jump opening_baking_selection

        # OPTION 2: Helfen (Nur da, wenn noch NICHT allen geholfen wurde)
        "Jemandem unter die Arme greifen" if not all_help_given:
            $ quick_menu = True
            jump opening_helping_selection

        # OPTION 3: Tag beenden (Nur da, wenn mind. EINER Person geholfen wurde)
        "Tag beenden (Genug geholfen)" if any_help_given:
            $ quick_menu = True
            user "Ich denke, ich habe das Schlimmste verhindert. Der Rest läuft jetzt von alleine."
            jump story_cafe_after_rush



## --- A. HELFEN AUSWAHL ---
label opening_helping_selection:
    user "Wer braucht am dringendsten Hilfe?"

    $ quick_menu = False

    menu:
        # Die Optionen erscheinen nur, wenn man noch NICHT geholfen hat

        "Velvette helfen" if not helped_velvette:
            $ helped_velvette = True
            $ quick_menu = True
            jump opening_help_velvette

        "Macoi helfen" if not helped_macoi:
            $ helped_macoi = True
            $ quick_menu = True
            jump opening_help_macoi

        "Lavan helfen" if not helped_lavan:
            $ helped_lavan = True
            $ quick_menu = True
            jump opening_help_lavan

        "Cino helfen" if not helped_cino:
            $ helped_cino = True
            $ quick_menu = True
            jump opening_help_cino

        # DER ZURÜCK BUTTON
        "Ich entscheide mich um (Zurück)":
            $ quick_menu = True
            jump cafe_opening_decision_hub

## --- B. BACKEN AUSWAHL ---
label opening_baking_selection:
    user "Okay, ab in die Küche. Aber wen nehme ich mit?"

    $ quick_menu = False

    menu:
        "Alleine backen":
            $ current_kitchen_helper = None
            jump start_opening_baking_process

        "Lavan fragen":
            $ current_kitchen_helper = "Lavan"
            jump start_opening_baking_process

        "Macoi fragen":
            $ current_kitchen_helper = "Macoi"
            jump start_opening_baking_process

        "Velvette fragen":
            $ current_kitchen_helper = "Velvette"
            jump start_opening_baking_process

        "Cino fragen":
            $ current_kitchen_helper = "Cino"
            jump start_opening_baking_process

        # DER ZURÜCK BUTTON
        "Ich entscheide mich um (Zurück)":
            jump cafe_opening_decision_hub

label start_opening_baking_process:
    # Kontext setzen für Rückkehr nach Minigame
    $ baking_context = "story_opening"
    $ quick_menu = True
    $ baking_con = "story_act_2"
    user "Alles klar, fangen wir an!"
    jump baking_minigame_hub

## ----------------------------------------------------------------
## --- SZENE: VELVETTE HELFEN ---
## ----------------------------------------------------------------
label opening_help_velvette:
    show velvette neutral at middle_vel

    user "Ein Mann kam gerade herein in das Cafe. Leicht unsicher schaute er sich um."
    user "Velvette trat einen Schritt zur Seite, musterte den Mann von oben bis unten und rümpfte leicht die Nase."
    v "\"Der Hut ist... eine mutige Entscheidung für diese Jahreszeit. Tisch vier. Da sehen Sie am wenigsten störend aus.\""

    $ quick_menu = False

    menu:
        "Die Situation charmant retten":
            # Richtig
            $ task_result_velvette = "success"
            user "Ich trat schnell dazwischen und lächelte den Mann an."
            user "\"Was meine Kollegin sagen wollte: Tisch vier ist unser gemütlichster Platz. Genau richtig für so einen stilvollen Hut.\""
            user "Der Mann entspannte sich. \"Oh, danke!\""
            call _add_affection(LI_VELVETTE, 1)
            v "Sie warf mir einen Blick zu. \"Glück gehabt. Er hat es gekauft.\""

        "Sie zurechtweisen":
            # Falsch
            $ task_result_velvette = "fail"
            user "\"Velvette! Sei nett zu dem Kunden!\""
            v "\"Pff. Ich bin ehrlich, nicht nett.\""

    jump cafe_opening_decision_hub


## ----------------------------------------------------------------
## --- SZENE: MACOI HELFEN ---
## ----------------------------------------------------------------
label opening_help_macoi:
    show macoi tired at middle

    user "Macoi hatte die Bestellung eingegeben, aber dann schien sein System in den Standby-Modus zu gehen."
    user "Er starrte auf den Tresen, während der Kunde erwartungsvoll sein Portemonnaie zückte."
    m "\"......\""
    user "Stille. Macoi blinzelte nicht einmal."

    $ quick_menu = False

    menu:
        "Ihn verbal erinnern ('Macoi, kassieren!')":
            # Falsch
            $ task_result_macoi = "fail"
            $ quick_menu = True
            user "\"Macoi! Du musst noch abkassieren!\""
            m "\"Häh? Was? Ja... natürlich. 3 Euro... bitte. Nicht so schreien...\""

        "Stummes Signal geben (Anstupsen)":
            # Richtig
            $ task_result_macoi = "success"
            $ quick_menu = True
            user "Ich trat leise neben ihn und stieß ihn ganz sanft mit meinem Ellbogen an."
            m "\"Ah. Danke.\""
            user "Er atmete erleichtert aus und kassierte ruhig ab."
            call _add_affection(LI_MACOI, 1)

    jump cafe_opening_decision_hub


## ----------------------------------------------------------------
## --- SZENE: LAVAN HELFEN ---
## ----------------------------------------------------------------
label opening_help_lavan:
    show lavan angry at middle

    user "Lavan hämmerte den Siebträger gegen die Maschine. Seine Hände zitterten vor Wut."
    l "\"Warum passt das nicht?! Das ist Sabotage!\""

    $ quick_menu = False

    menu:
        "Ihn sanft beruhigen ('Ganz ruhig')":
            # Falsch
            $ task_result_lavan = "fail"
            $ quick_menu = True
            user "\"Hey, ganz ruhig. Atme durch.\""
            l "\"Ich bin ruhig! Behandle mich nicht wie ein Kind!\""

        "Ihn herausfordern ('1:0 für die Maschine?')":
            # Richtig
            $ task_result_lavan = "success"
            $ quick_menu = True
            user "\"Wow. 1:0 für die Kaffeemaschine? Lässt du dich echt von etwas besiegen, das keinen Stecker hat?\""
            l "\"Hah?! Niemals! Pass bloß auf!\""
            user "Mit einem Ruck rastete der Siebträger ein. Er grinste triumphierend."
            call _add_affection(LI_LAVAN, 1)

    jump cafe_opening_decision_hub


## ----------------------------------------------------------------
## --- SZENE: CINO HELFEN ---
## ----------------------------------------------------------------
label opening_help_cino:
    show cino sad at middle

    # Platzhalter Text
    user "Cino kämpfte mit den Servietten."

    $ quick_menu = False

    menu:
        "Ihm helfen":
            # Richtig
            $ task_result_cino = "success"
            $ quick_menu = True
            call _add_affection(LI_CINO, 1)
            c "Danke!"

        "Ihn machen lassen":
            # Fail
            $ task_result_cino = "fail"
            $ quick_menu = True
            user "Er schafft das schon."

    jump cafe_opening_decision_hub

label story_cafe_after_rush:
    scene bg cafe with fade
 # HIER RESETTEN WIR DEN KRAM FÜRS BACKEN ZUR SICHERHEIT
    $ baking_context = None


    user "Puh... Der Tag ist vorbei."

    jump story_intro_03
