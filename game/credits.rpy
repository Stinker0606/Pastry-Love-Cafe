label credits:
    ## (Optional: Ein Song)
    # play music "audio/song.mp3" fadein 2.0
    
    ## 2. Ein schöner, ruhiger Hintergrund
    scene bg kitchen2                                            ## <- HINTERGRUND DARF MAN ÄNDERN
    ## Legt den halbtransparenten Schatten sanft darüber
    show dark_overlay
    with Dissolve(2.0)
    $ renpy.pause(1.0, hard=True)

    ## 3. Die Namen einblenden (truecenter setzt es exakt in die Mitte)
    show text "{size=100}{color=#f5253c}Story von{/color}{/size}\n{size=110}{color=#f5253c}Nasjo{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(3.0, hard=True)
    hide text with dissolve

    ## Ein schöner, ruhiger Hintergrund
    scene bg cafe2                                           ## <- HINTERGRUND DARF MAN ÄNDERN
    ## Legt den halbtransparenten Schatten sanft darüber
    show dark_overlay
    with Dissolve(2.0)
    $ renpy.pause(1.0, hard=True)

    show text "{size=100}{color=#f5253c}Programming von{/color}{/size}\n{size=110}{color=#f5253c}Koinzen{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(3.0, hard=True)
    hide text with dissolve

    ## Ein schöner, ruhiger Hintergrund
    scene bg boutique                                           ## <- HINTERGRUND DARF MAN ÄNDERN
    ## Legt den halbtransparenten Schatten sanft darüber
    show dark_overlay
    with Dissolve(2.0)
    $ renpy.pause(1.0, hard=True)

    show text "{size=100}{color=#f5253c}Art von{/color}{/size}\n{size=110}{color=#f5253c}Nasjo & Azal3a3{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(3.0, hard=True)
    hide text with dissolve

    ## Ein schöner, ruhiger Hintergrund
    scene bg Flur                                           ## <- HINTERGRUND DARF MAN ÄNDERN
    ## Legt den halbtransparenten Schatten sanft darüber
    show dark_overlay
    with Dissolve(2.0)
    $ renpy.pause(1.0, hard=True)

    show text "{size=100}{color=#f5253c}Musik & Sound Effekte von{/color}{/size}\n{size=110}{color=#f5253c}Azal3a3{/color}{/size}" at truecenter with dissolve
    $ renpy.pause(3.0, hard=True)
    hide text with dissolve

    ## Ein schöner, ruhiger Hintergrund
    scene bg mall                                           ## <- HINTERGRUND DARF MAN ÄNDERN
    ## Legt den halbtransparenten Schatten sanft darüber
    show dark_overlay
    with Dissolve(2.0)
    $ renpy.pause(1.0, hard=True)

    ## 4. Der emotionale Abschluss
    $ renpy.pause(1.0, hard=True)
    show text "{size=140}{color=#f5253c}Vielen Dank fürs Spielen!{/color}{/size}" at truecenter with Dissolve(2.0)
    $ renpy.pause(4.0, hard=True)
    hide text with Dissolve(2.0)

    ## 5. Das tatsächliche Ende (bringt den Spieler zurück ins Hauptmenü)
    return