label Epilog_Velvette:


    scene bg gartencafe with fade

    "Die Frühlingssonne fiel warm durch das Blätterdach des Gartencafés und ließ die unzähligen Blumen um uns herum in den buntesten Farben leuchten."
    "Es duftete nach Jasmin, frischem Gebäck und dem teuren Parfüm, das Velvette heute trug."

    show velvette

    "Ihr ging es gut. Besser als gut sogar. Als aufsteigender Stern am Modehimmel war ihr Terminkalender voll, aber heute gehörte sie nur mir."
    "Sie nippte elegant an ihrem Cappuccino, achtete penibel darauf, ihren Lippenstift nicht zu verwischen, und seufzte dann zufrieden."

    v "Weißt du... dieser Ort hat tatsächlich einen gewissen Charme. Das Licht hier ist perfekt für Fotos."

    user "Ich dachte, wir machen heute mal keine Fotos für deine Follower?"

    v "Machen wir auch nicht. Ich genieße nur die Ästhetik, Schätzchen."

    "Sie stellte die Tasse ab und rückte ihre perfekt sitzende Bluse zurecht. Früher wäre sie nervös gewesen, wenn ein Windstoß ihre Frisur durcheinandergebracht hätte."
    "Aber als genau das passierte – eine kleine Brise wehte ihr eine Strähne ins Gesicht – lachte sie nur leise und strich sie entspannt zurück."

    v "Weißt du noch, wie ich früher wegen jedem kleinen Fleck oder jedem schlechten Tag fast durchgedreht bin?"

    user "Oh ja. Du hast das Leben wie einen Laufsteg behandelt, auf dem man nicht stolpern darf."

    show velvette 

    v "Ja. Aber ich habe gelernt... das Leben ist eben keine Modenschau. Manchmal regnet es, manchmal stolpert man."
    v "Wichtig ist nur, wie man danach wieder aufsteht und weitermacht. Und dass man jemanden hat, der einem die Hand reicht."

    "Sie legte ihre manikürte Hand auf meine. Es war eine kleine, aber bedeutungsvolle Geste."

    user "Du hast dich wirklich verändert, Velvette. Ich bin stolz auf dich."

    v "Gewöhn dich nicht zu sehr an die sentimentale Velvette! Ich bin immer noch eine Ikone."

    "Wir lachten beide. Dann ließ sie ihren Blick über das Café schweifen."

    v "Ich muss zugeben, du hast hier etwas Tolles aufgebaut. Es ist... gemütlich."

    user "Willst du mir nicht doch mal hinter der Theke helfen? Wir könnten Hilfe gebrauchen."

    show velvette

    v "Ich? Hinter der Theke? Mit einer... Schürze?"
    v "Oh, Liebling, bitte. Ich sehe mich hier absolut nicht beim Kaffeekochen. Das würde meine Nägel ruinieren."

    "Sie lehnte sich vor und drückte meine Hand etwas fester."

    v "Aber ich werde hier sein. Jeden Tag, wenn ich kann. Ich trinke meinen Kaffee, ich sorge für Glamour und ich erzähle jedem, der wichtig ist, dass das hier der 'Place to be' ist."
    v "Ich bin vielleicht keine Kellnerin, aber ich bin dein größter Fan... und deine beste Werbung."

    # Hier wird ein Belohnungsbild
    scene reward velvette with fade
    $ persistent.ending_velvette_unlocked = True
    $ persistent.cg_velvette_unlocked = True

    window hide
    $ quick_menu = False
    pause
    $ quick_menu = True
    window show

    "In diesem Moment, zwischen den blühenden Blumen und dem Klappern der Tassen, wirkte sie nicht wie der unnahbare Star, den die Welt sah."
    "Sie war einfach Velvette. Und sie war glücklich."

    v "Also... bestell mir noch so ein Törtchen. Wir haben etwas zu feiern."

    user "Was feiern wir?"

    v "Uns. Und den Frühling. Und dass ich heute einfach mal nicht perfekt sein muss, um mich perfekt zu fühlen."

return
