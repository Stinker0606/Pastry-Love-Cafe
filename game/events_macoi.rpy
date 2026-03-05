label Epilog_Macoi:

    scene bg sofa with fade
    play music "audio/Romantic_Music.mp3" fadein 0.5 volume 0.75

    user "Mein Nacken war steif und meine Augen brannten, als ich immer noch auf den Bildschirm starrte."
    user "Es war ein unfassbar langer und anstrengender Tag gewesen, aber mein Kopf ratterte immer noch auf Hochtouren."
    user "Ich wusste einfach nicht, wie ich abschalten sollte. Da war noch so viel zu tun..."

    # Macoi taucht auf
    show macoi sad at middle_m

    user "Plötzlich spürte ich eine warme Hand, die sich sanft auf meine Schulter legte."

    m "\"Hey... Schluss für heute.\""

    user "\"Nur noch diese eine Sache, Macoi, ich schwöre-\""

    user "Bevor ich den Satz beenden konnte, griff er über mich und klappte kurzerhand meinen Laptop zu."

    m "\"Nichts da. Wir hatten eine Abmachung. Du überarbeitest dich nicht mehr, und ich...\""

    user "\"...und du gehst zu menschlichen Zeiten schlafen.\""

    user "\"Ich seufzte tief, aber ein kleines Lächeln stahl sich auf meine Lippen, als ich zu ihm aufsah und mich im Stuhl zurücklehnte.\""

    show macoi happy with dissolve

    user "Er hatte recht. Macoi hatte sich in den letzten Wochen so sehr gebessert. Sein ungesunder, völlig chaotischer Schlafrhythmus gehörte der Vergangenheit an."
    user "Er sah so viel erholter aus, die dunklen Ringe unter seinen Augen waren fast vollständig verschwunden, und er wirkte viel ausgeglichener."
    user "Wenn er so hart an sich arbeitete, musste ich mich wohl auch an meinen Teil der Abmachung halten."

    m "\"Genau. Also, komm her.\""

    user "Er nahm sanft meine Hände, zog mich von meinem Schreibtischstuhl hoch und führte mich hinüber zum Sofa."

    user "Er drückte mich sanft in die Kissen, holte die flauschigste Decke, die wir besaßen, und wickelte mich darin ein wie einen Burrito."
    user "Dann verschwand er kurz in der Küche und kam mit zwei dampfenden Tassen Tee zurück."

    m "\"Filmabend. Dein Gehirn hat jetzt offiziell Pause.\""

    user "\"Was schauen wir?\""

    m "\"Etwas Dummes, Lustiges, bei dem man absolut nicht nachdenken muss.\""

    # Hier ein Belohnungsbild einfügen!
    scene reward macoi with fade
    $ persistent.ending_macoi_unlocked = True
    $ persistent.cg_macoi_unlocked = True

    window hide
    $ quick_menu = False
    pause
    $ quick_menu = True
    window show

    user "Er stellte die Tassen ab, schaltete den Fernseher ein und ließ sich neben mich auf das Sofa fallen."
    user "Sofort zog er mich an seine Seite, sodass ich mich an ihn kuscheln und meinen Kopf auf seiner Brust ablegen konnte."

    user "Die wohlige Wärme, der Duft des Tees und sein ruhiger, gleichmäßiger Herzschlag taten ihre Wirkung."
    user "Ich spürte, wie die harte Anspannung des Tages langsam von mir abfiel und meine Muskeln weich wurden."

    user "\"Danke, Macoi...\""

    user "Er drückte mir einen sanften Kuss auf den Scheitel und strich beruhigend über meinen Arm."

    m "\"Immer wieder gern. Dafür bin ich da. Jetzt entspann dich, ich pass auf dich auf.\""

    user "Während der Film auf dem Bildschirm flackerte und Macoi leise über einen schlechten Witz lachte, schloss ich für einen Moment die Augen."
    user "Endlich war ich zur Ruhe gekommen. Hier, in seinen Armen, fühlte sich alles einfach genau richtig an."

    stop music fadeout 3.0
    scene black with fade


jump credits
