label Epilog_Lavan:


    scene bg Flur with fade

    user "Lavan hatte mir heute Morgen eine Nachricht geschrieben, dass er eine Überraschung für mich geplant hatte und wir uns im Park treffen sollten."
    user "Mein Herz klopfte vor freudiger Aufregung, als ich mich fertig machte."
    user "Für diesen Tag hatte ich mir etwas ganz Besonderes überlegt. Aus den Tiefen meines Schrankes hatte ich das alte, fließende rosa Kleid meiner Mutter hervorgeholt."

    user "\"Genau das Kleid, von dem ich immer gesagt habe...\""
    user "\"Das trage ich erst, wenn ich ein richtiges, wunderschönes Date habe.\""

    user "Mit dem großen, blumengeschmückten Strohhut fühlte ich mich endlich bereit. Ich trat aus dem Haus und machte mich auf den Weg."

    scene bg fruehlingspark with fade

    user "Der Frühling lag wie ein süßes Versprechen in der Luft, und die warme Sonne begleitete mich auf meinem Spaziergang."
    user "Als ich an unserem Treffpunkt ankam – einer kleinen Lichtung, umgeben von blühenden Bäumen  sah ich ihn schon."

    show lavan happy at middle

    user "Als Lavan mich bemerkte, hellte sich sein Gesicht sofort auf. Ein breites, liebevolles Lächeln breitete sich auf seinen Lippen aus und er kam mir mit schnellen Schritten entgegen."

    # Hier wird Belohnungsbild eingeblendet!
    scene reward lavan with fade
    $ persistent.ending_lavan_unlocked = True
    $ persistent.cg_lavan_unlocked = True

    window hide
    $ quick_menu = False
    pause
    $ quick_menu = True
    window show

    user "Bevor ich auch nur ein Wort sagen konnte, schlang er sanft seine Arme um meine Taille und hob mich mit einer spielerischen Leichtigkeit in die Luft."
    user "Ein fröhliches Lachen entwich mir, und ich legte meine Arme um seinen Nacken."

    l "\"Wow... Du siehst absolut wunderschön aus.\""

    user "Die sanften Frühlingsblüten tanzten im Wind um uns herum, als er mich fest an sich drückte."
    user "Die Zeit schien für einen winzigen Moment stillzustehen, als er mich zärtlich küsste. Es war ein Augenblick vollkommenen Glücks."

    show lavan blush with dissolve

    user "Als er mich schließlich sanft wieder auf den Boden gleiten ließ, fiel mein Blick auf das, was sich hinter ihm befand."
    user "Unter dem Blätterdach der Bäume lag eine gemütliche Picknickdecke, liebevoll hergerichtet mit Körben voller Leckereien, frischem Obst und kühlen Getränken."

    user "\"Lavan... Hast du das alles selbst geplant?\""

    l "\"Ich wollte dich überraschen. Ein echtes Frühlingsdate für uns beide.\""

    user "Wir setzten uns auf die Decke, genossen das fantastische Essen und lachten viel."

    user "Während wir uns unterhielten, beobachtete ich ihn unauffällig."
    user "Seine Gesichtszüge waren weich, sein Blick so warm und ruhig."
    user "Er wirkte so viel friedlicher und gelöster als noch am Anfang unserer Reise. Die innere Unruhe, die ihn einst begleitet hatte, schien wie weggeblasen."

    l "\"Warum siehst du mich so an?\""

    user "\"Ich bin nur... einfach glücklich, dass wir hier sind.\""

    user "Er lächelte, griff nach meiner Hand und verschränkte seine Finger sanft mit meinen."

    l "\"Ich auch. Mehr als je zuvor.\""

    user "Wir saßen einfach glücklich zusammen im warmen Licht der Sonne und genossen unser Date – ein perfektes Happy End, das sich in Wirklichkeit wie ein wunderschöner neuer Anfang anfühlte."

    scene black with fade

jump credits
