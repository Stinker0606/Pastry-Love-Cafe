## Spezielles einmaliges Ereignis nach dem ersten mal backen.
label awakening_shock_scene:
    stop music fadeout 2.0

    scene black
    user "Okay, das erste Rezept ist fertig. Aber ich habe noch Energie..."
    jump awakening_sequence_start

label awakening_sequence_start:
    scene bg cafe with fade

    play music "audio/Silly_Music.mp3" fadein 0.5 volume 0.75

    ## Alle sind da
    $ is_lavan_awakened = True
    $ is_macoi_awakened = True
    $ is_velvette_awakened = True
    $ is_cino_awakened = True

    user "Nachdem ich die letzte Zutat hineingegeben hatte, schob ich den Teig in den Ofen, stellte den Timer und klopfte mir die Hände ab."

    user "Während das Gebäck backte, machte ich mich daran, das Café für die Öffnung vorzubereiten."

    user "Stühle richtig stellen, Tische abwischen, Kasse einschalten, Schilder aufstellen…"

    #Effekt von Screenshake?

    play sound "audio/Loud_Soundeffect.mp3" volume 0.2
    show bg cafe with hpunch

    user "Ich war gerade dabei, die Servietten zu sortieren, als ich ein Geräusch hörte." 

    user "Etwas dumpfes."

    user "Oder ein… Summen?"

    user "Oder ein tiefes Brummen?"

    user "Oder eine Mischung aus Ofenexplosion und schlecht gelaunter Hummel?"

    user "Ich blieb stehen."

    user "\"Zu müde. Ich halluziniere. Definitiv.\""

    play sound "audio/Loud_Soundeffect.mp3" volume 0.8
    show bg cafe with hpunch

    user "Doch dann kam das Geräusch wieder. Diesmal lauter."

    user "Ich schluckte, griff mir einen Besen, die einzige „Waffe“, die man einer Bäckerin zutrauen konnte und schlich vorsichtig Richtung Küche."

    scene bg kitchen2

    user "Und dort blieb ich erneut stehen."

    user "Ich blinzelte."

    user "Und dann noch einmal."

    user "\"Ich schlafe nicht..? Halluziniere nicht?\""

    user "\"Dann werde ich verrückt.\""

    user "Vor mir standen vier Leute, sichtlich an das Gebäck erinnert das ich vorher gebackt hatte."

    ## Zeigt die 4 Chars an. Schau wo du das einfügst, die Chars werden dann erst angezeigt wo das kommt.
    show lavan neutral at pos_1
    show cino neutral at pos_2
    show macoi neutral at pos_4
    show velvette neutral at pos_3

    ## wer was sagt wenn man ihn als erstes gebacken hat:

    if first_li_chosen == "Lavan":
        user "Der Erste, der mir ins Auge stach, war ein breitgebauter Mann mit braunem Haar."

        user "Mit in die Hüften gestemmten Armen und einer griesgrämigen Miene musterte er die Umgebung."

        user "Er wirkte weniger schockiert als vielmehr maßlos unzufrieden mit der Gesamtsituation."

        l1 "„Und wo zur Hölle bin ich hier eigentlich?!“"

        user "Seine raue Stimme donnerte durch den Raum und ließ mich unwillkürlich zusammenzucken."

    elif first_li_chosen == "Macoi":
        user "Etwas abseits lehnte ein junger Mann gegen die Wand, der aussah, als würde er im Stehen schlafen."

        user "Seine grünen Haare standen wild in alle Richtungen ab, und er rieb sich mit dem Handrücken langsam über die müden Augen."

        user "Er wirkte weder wütend noch ängstlich, sondern eher so, als wäre seine größte Sorge gerade, wo er das nächste Kissen herbekommt."

        m1 "..."

        user "Total desinteressiert."

    elif first_li_chosen == "Velvette":
        user "Mein Blick fiel auf eine Frau, die so gar nicht in diese seltsame Umgebung passte."

        user "Sie schien makellos, ihre Haltung kerzengerade und sie musterte den Boden mit unverhohlener Abscheu."

        user "Sie wirkte wie ein Model oder eine Puppe, mit porzellan Haut, das sich versehentlich ans falsche Set verirrt hatte und nun den Manager sprechen wollte."

        v1 "Ernsthaft? Das alles hier ist..."

        user "Sie suchte ein Wort für ihr Kommentar."

        v1 "Geschmacklos."

        user "Sie schnippte ein imaginäres Staubkorn von ihrer Schulter und rümpfte pikiert die Nase."

    elif first_li_chosen == "Cino":
        user "Ich schaute mir den eher unscheinbarer Mann, der nervös mit seinen Händen spielte."

        user "Er ließ seinen Blick hektisch von einem zum anderen wandern, wie ein scheues Reh, das blitzschnell eine Fluchtroute berechnet."

        user "Er schien der Einzige zu sein, der weniger verärgert als vielmehr ehrlich besorgt war."

        c1 "Ähm... Entschuldigung? Hallo? Weiß vielleicht jemand, wie wir hierher gekommen sind?"

        user "Seine Stimme zitterte leicht, aber er versuchte tapfer, ein höfliches, wenn auch gequältes Lächeln aufzusetzen."

        user "Als er mich starren sah, zuckte er zusammen. Ich sah wie er Luft holte und sein Mut zusammen nahm."

    c1 "\"Wir sind… wirklich keine Gefahr.\""

    user "\"Ihr seid nackt in meiner Küche!\""

    user "exklamierte ich lauter als erwartet."

    v1 "\"Ähm… können wir vielleicht… Kleidung bekommen?\""

    user "Fragte die rothaarige unschuldig."

    user "Ich rieb mir die Schläfen. Das hier war zu viel. Viel zu viel für meinen mehlarmen Morgen."

    user "Doch dann fiel mein Blick auf das kleine Glas mit dem lila Pulver auf der Arbeitsfläche."

    user "\"Oh-\""

    user "\"Oh!\""

    user "\"Ich habe gebacken mit… äh… etwas, das ich gestern bekommen habe. Und jetzt… seid ihr… da.\""

    user "Versuchte ich drauf klarzukommen."

    user "Die anderen waren schon wieder mit was anderem beschäftigt."

    show velvette happy at pos_3 with dissolve

    user "Die rothaarige Frau war mittlerweile damit beschäftigt sich in der Reflektion anzuschauen."

    user "Der grünhaarige, wahrscheinlich der Matcha, stand zwar aufrecht doch seine Augen waren zu. Er schien im Stehen zu schlafen."

    user "Die anderen zwei, der Blonde und der Braunhaarige schienen gerade in ein anderes 'Gespräch' vertieft zu sein."

    show lavan angry at pos_1 with dissolve

    user "Oder eher gesagt schien der Braunhaarige sich über den anderen aufregen."

    user "\"Okay. Bevor hier jemand Feuer fängt oder eins veranstaltet.\""

    user "\"Wir holen euch Kleidung, setzen uns irgendwo hin, wo ihr NICHT meine Küche kontaminiert und dann versuchen wir herauszufinden, was zum Henker hier passiert ist.\""

    user "Alle nickten und ich führte sie aus der Küche."

    user "Das wird noch ein langer Tag."

    scene black with fade
    stop music fadeout 3.0

    jump story_intro_02 # Ab ins Akt 2
