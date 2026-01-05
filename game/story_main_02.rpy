## -- TEIL 1: INTRO ---
label story_intro_02:
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
        "Einfach Leise mein Ding machen":
            # Hier passiert nichts Besonderes.
            user "Ich beschloss, ihre Konzentration nicht zu stören und putzte leise meine Zähne."
            
        "Ihr ein Kompliment geben":
            call _add_affection(LI_VELVETTE, 1)
            user "\"Du siehst gut aus.\""

            user "Ohne auch nur ihren Blick vom Spiegel zu lösen, antwortete sie trocken."
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
    menu:
        "Velvette aufmuntern":
            call _add_affection(LI_VELVETTE, 1)
            user "\"BIBABUB\""
            
        "Cino aufmuntern":
            call _add_affection(LI_VELVETTE, 1)
            user "\"LOREM IPSUM\""

        "Lavan aufmuntern":
            call _add_affection(LI_VELVETTE, 1)
            user "\"TRILALO\""

        "Macoi aufmuntern":
            call _add_affection(LI_VELVETTE, 1)
            user "\"HELP ME\""

    #Sprung zum cafe

    # Sprung zum Café / Hintergrundbild Café Interior

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

    ## --- DAS HUB MENÜ --- VIEL PLACEHOLDER TEXT
label cafe_opening_decision_hub:
    
    # Wir berechnen kurz den Status
    # 1. Hat man mind. EINER Person geholfen? (ODER-Verknüpfung)
    $ any_help_given = helped_velvette or helped_macoi or helped_lavan or helped_cino
    
    # 2. Hat man ALLEN geholfen? (UND-Verknüpfung)
    $ all_help_given = helped_velvette and helped_macoi and helped_lavan and helped_cino

    user "Was soll ich tun?"

    menu:
        # OPTION 1: Backen (Immer da)
        "Etwas Backen (Beendet diese Szene!)":
            user "Ich muss backen, sonst haben wir gleich nichts mehr zu verkaufen."
            jump opening_baking_selection

        # OPTION 2: Helfen (Nur da, wenn noch NICHT allen geholfen wurde)
        "Jemandem unter die Arme greifen" if not all_help_given:
            jump opening_helping_selection

        # OPTION 3: Tag beenden (Nur da, wenn mind. EINER Person geholfen wurde)
        "Tag beenden (Genug geholfen)" if any_help_given:
            user "Ich denke, ich habe das Schlimmste verhindert. Der Rest läuft jetzt von alleine."
            jump story_cafe_after_rush


## --- A. HELFEN AUSWAHL ---
label opening_helping_selection:
    user "Wer braucht am dringendsten Hilfe?"

    menu:
        # Die Optionen erscheinen nur, wenn man noch NICHT geholfen hat

        "Velvette helfen" if not helped_velvette:
            $ helped_velvette = True
            jump opening_help_velvette

        "Macoi helfen" if not helped_macoi:
            $ helped_macoi = True
            jump opening_help_macoi

        "Lavan helfen" if not helped_lavan:
            $ helped_lavan = True
            jump opening_help_lavan
        
        "Cino helfen" if not helped_cino:
            $ helped_cino = True
            jump opening_help_cino

        # DER ZURÜCK BUTTON
        "Ich entscheide mich um (Zurück)":
            jump cafe_opening_decision_hub

## --- B. BACKEN AUSWAHL ---
label opening_baking_selection:
    user "Okay, ab in die Küche. Aber wen nehme ich mit?"

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
    
    user "Alles klar, fangen wir an!"
    jump baking_minigame_hub

## ----------------------------------------------------------------
## --- SZENE: VELVETTE HELFEN ---
## ----------------------------------------------------------------
label opening_help_velvette:
    # show velvette neutral at center
    
    user "Ein Mann kam gerade herein in das Cafe. Leicht unsicher schaute er sich um."
    user "Velvette trat einen Schritt zur Seite, musterte den Mann von oben bis unten und rümpfte leicht die Nase."
    v "\"Der Hut ist... eine mutige Entscheidung für diese Jahreszeit. Tisch vier. Da sehen Sie am wenigsten störend aus.\""

    menu:
        "Die Situation charmant retten":
            # Richtig
            user "Ich trat schnell dazwischen und lächelte den Mann an."
            user "\"Was meine Kollegin sagen wollte: Tisch vier ist unser gemütlichster Platz. Genau richtig für so einen stilvollen Hut.\""
            user "Der Mann entspannte sich. \"Oh, danke!\""
            call _add_affection(LI_VELVETTE, 1)
            v "Sie warf mir einen Blick zu. \"Glück gehabt. Er hat es gekauft.\""

        "Sie zurechtweisen":
            # Falsch
            user "\"Velvette! Sei nett zu dem Kunden!\""
            v "\"Pff. Ich bin ehrlich, nicht nett.\""

    jump cafe_opening_decision_hub


## ----------------------------------------------------------------
## --- SZENE: MACOI HELFEN ---
## ----------------------------------------------------------------
label opening_help_macoi:
    # show macoi tired at center

    user "Macoi hatte die Bestellung eingegeben, aber dann schien sein System in den Standby-Modus zu gehen."
    user "Er starrte auf den Tresen, während der Kunde erwartungsvoll sein Portemonnaie zückte."
    m "\"......\""
    user "Stille. Macoi blinzelte nicht einmal."

    menu:
        "Ihn verbal erinnern ('Macoi, kassieren!')":
            # Falsch
            user "\"Macoi! Du musst noch abkassieren!\""
            m "\"Häh? Was? Ja... natürlich. 3 Euro... bitte. Nicht so schreien...\""

        "Stummes Signal geben (Anstupsen)":
            # Richtig
            user "Ich trat leise neben ihn und stieß ihn ganz sanft mit meinem Ellbogen an."
            m "\"Ah. Danke.\""
            user "Er atmete erleichtert aus und kassierte ruhig ab."
            call _add_affection(LI_MACOI, 1)

    jump cafe_opening_decision_hub


## ----------------------------------------------------------------
## --- SZENE: LAVAN HELFEN ---
## ----------------------------------------------------------------
label opening_help_lavan:
    # show lavan angry at center

    user "Lavan hämmerte den Siebträger gegen die Maschine. Seine Hände zitterten vor Wut."
    l "\"Warum passt das nicht?! Das ist Sabotage!\""

    menu:
        "Ihn sanft beruhigen ('Ganz ruhig')":
            # Falsch
            user "\"Hey, ganz ruhig. Atme durch.\""
            l "\"Ich bin ruhig! Behandle mich nicht wie ein Kind!\""

        "Ihn herausfordern ('1:0 für die Maschine?')":
            # Richtig
            user "\"Wow. 1:0 für die Kaffeemaschine? Lässt du dich echt von etwas besiegen, das keinen Stecker hat?\""
            l "\"Hah?! Niemals! Pass bloß auf!\""
            user "Mit einem Ruck rastete der Siebträger ein. Er grinste triumphierend."
            call _add_affection(LI_LAVAN, 1)

    jump cafe_opening_decision_hub


## ----------------------------------------------------------------
## --- SZENE: CINO HELFEN ---
## ----------------------------------------------------------------
label opening_help_cino:
    # show cino nervous at center
    
    # Platzhalter Text
    user "Cino kämpfte mit den Servietten."
    
    menu:
        "Ihm helfen":
            call _add_affection(LI_CINO, 1)
            c "Danke!"
        
        "Ihn machen lassen":
            user "Er schafft das schon."

    jump cafe_opening_decision_hub

label story_cafe_after_rush:
    scene bg cafe with fade

    # HIER RESETTEN WIR DEN STUFF ZUR SICHERHEIT
    $ baking_context = None

    user "Puh... Der Tag ist vorbei."    



## ===========================================================================================================================================================================================
## ===========================================================================================================================================================================================
##                                                                  WENN DAS HIER DRUNTER NICHT MEHR BENÖTIGT LÖSCHEN BIS ZUR MARKIERUNG !!! 
## ===========================================================================================================================================================================================
## ===========================================================================================================================================================================================

    #Velvettes Choice

    user "Ein Mann kam gerade herein in das Cafe leicht unsicher schaute er sich um."

    user "Velvette trat einen Schritt zur Seite, musterte den Mann von oben bis unten und rümpfte leicht die Nase."

    v "\"Der Hut ist... eine mutige Entscheidung für diese Jahreszeit. Tisch vier. Da sehen Sie am wenigsten störend aus.\""

    # CHOICE
    # Entscheidung die Situation zu retten oder nicht

    # Macois Choice

    user "Ich schaute mich wieder um und erblickte die nächste Situation"

    user "Macoi hatte die Bestellung eingegeben, aber dann schien sein System in den Standby-Modus zu gehen."
    user "Er starrte auf den Tresen, während der Kunde erwartungsvoll sein Portemonnaie zückte."
    m "\"......\""
    user "Stille. Macoi blinzelte nicht einmal. Er war mental ganz weit weg."

    # CHOICE
    # A: Ihn verbal erinnern ("Macoi, kassieren bitte.")
    # B: Stummes Signal geben (Leichtes Anstupsen / Blickkontakt)

    # --- Falls A (Falsch / Zu laut) ---
    user "\"Macoi! Du musst noch abkassieren!\""
    user "Ich sagte es nicht böse, aber in der Stille wirkte meine Stimme wie ein Donnerschlag."
    user "Macoi zuckte heftig zusammen, als hätte ich ihn geweckt."
    m "\"Häh? Was? Ja... natürlich.\""
    user "Er wirkte kurz desorientiert und genervt von der plötzlichen Störung."
    m "\"3 Euro... bitte. Nicht so schreien...\""


    # --- Falls B (Richtig) ---
    user "Ich trat leise neben ihn und stieß ihn ganz sanft mit meinem Ellbogen an, ohne ein Wort zu sagen."
    user "Ich nickte nur ruhig in Richtung des Kunden."
    user "Macoi verstand das Signal sofort. Kein Lärm, kein Stress. Er atmete erleichtert aus."
    m "\"Ah. Danke.\""
    user "Er wandte sich wieder dem Kunden zu, seine Bewegungen waren flüssig und ruhig."
    m "\"Das macht 3 Euro. Danke für Ihre Geduld.\""
    user "Er warf mir einen kurzen Seitenblick zu, der 'Gute Arbeit' bedeutete."

    # Lavans Choice

    user "Lavan hämmerte den Siebträger gegen die Maschine. Seine Hände zitterten vor Wut (und Nervosität)."

    l "\"Warum passt das nicht?! Das ist Sabotage!\""

    # CHOICE
    # A: Ihn sanft beruhigen ("Ganz ruhig, Lavan. Alles ist gut.")
    # B: Ihn spielerisch herausfordern ("Lässt du dich echt von einer Maschine besiegen?")

    # --- Falls A (Falsch / Zu weich) ---
    user "Ich legte ihm eine Hand auf die Schulter. \"Hey, ganz ruhig. Atme durch. Du machst dir zu viel Stress.\""
    user "Lavan riss sich sofort los, sein Gesicht rot vor Scham und Ärger."
    l "\"Ich bin ruhig! Behandle mich nicht wie ein Kind! Ich brauche kein Mitleid!\""
    user "Er machte den Kaffee fertig, drehte mir aber beleidigt den Rücken zu."


    # --- Falls B (Richtig) ---
    user "Ich grinste ihn schief an. \"Wow. 1:0 für die Kaffeemaschine? Lässt du dich echt von etwas besiegen, das keinen Stecker hat?\""
    user "Lavan schnaubte empört, aber das Zittern hörte auf. Der Kampfgeist war geweckt."
    l "\"Hah?! Niemals! Pass bloß auf!\""
    user "Mit einem Ruck rastete der Siebträger perfekt ein. Er grinste triumphierend zu mir herüber."
    l "\"Siehst du? Ich habe gewonnen.\""

    # Cino Choice

## ===========================================================================================================================================================================================
## ===========================================================================================================================================================================================
###                                                                                            MARKIERUNG
## ===========================================================================================================================================================================================
## ===========================================================================================================================================================================================









## PLS LASSEN WAS HIER DRUNTER IST!!

# ## Ab ins Alltag Hub
#     jump alltag_start

#     ## ========================================================================================================================================================================================
#     ## -- BAKING HUB TEST --- BITTE DEN CODE HIER DRUNTER LASSEN
#     ## ========================================================================================================================================================================================

# ## --- TEIL 2: ALLTAG START ---
# label alltag_start:
#     $ day = 1
#     jump alltag_hub

# ## --- TEIL 3: ALLTAGS-HUB ---
# label alltag_hub:
#     ## --- TAGES-PLANUNG: WER IST WO? ---
#     python:
#         ## Tag 1 = Lavan, Tag 2 = Macoi, Tag 3 = Velvette, Tag 4 = Cino
#         if (day % 4) == 1:
#             current_kitchen_helper = "Lavan"
#         elif (day % 4) == 2:
#             current_kitchen_helper = "Macoi"
#         elif (day % 4) == 3:
#             current_kitchen_helper = "Velvette"
#         else:
#             current_kitchen_helper = "Cino"

#     scene bg cafe
#     user "Ich will was backen"

#     menu:
#         "In die Küche gehen":
#             jump kitchen_room_interaction

#         "Tag beenden":
#             $ day += 1
#             jump alltag_hub

# ## --- KÜCHEN-RAUM ---
# label kitchen_room_interaction:
#     scene bg kitchen

#     ## Zeige den Helfer, der Dienst hat
#     if current_kitchen_helper == "Lavan":
#         show lavan smile
#         l "Auch mal da [player_name]."
#     elif current_kitchen_helper == "Macoi":
#         show macoi smile
#         m "Hey."
#     elif current_kitchen_helper == "Velvette":
#         show velvette smile
#         v "Naa"
#     elif current_kitchen_helper == "Cino":
#         show cino smile
#         c "Hallo."

#     menu:
#         "Backen (Minigame)":
#             ## Wir gehen zum Minigame-Hub.
#             jump baking_minigame_hub

#         "Reden":
#             if current_kitchen_helper == "Lavan":
#                 jump lavan_event_1
#             elif current_kitchen_helper == "Macoi":
#                 jump macoi_event_1
#             elif current_kitchen_helper == "Velvette":
#                 jump velvette_event_1
#             elif current_kitchen_helper == "Cino":
#                 jump cino_event_1
