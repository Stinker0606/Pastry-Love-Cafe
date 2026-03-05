## Custom GUI Variables -- Do Not Change ------------------------- ##

## GUI Variables ------------------------- ##
default extra_menu = "none"

## CG GALLERY CODE ------------------------- ##
## this tells the gallery which CG to show
default cg = "1"

## Extras screens ##################################################################
##
## This is the code for the extras screens (CG Gallery, Achievements, and Endings)
##
##

screen extras():
    tag menu
    style_prefix "extras"

    add "gui/extras_bg.png"

    ## --- UNSICHTBARE CHEAT-BUTTONS ---
    
    ## 1. ALLES FREISCHALTEN (Oben Links in der Ecke)
    button:
        xpos 0 ypos 0
        xsize 100 ysize 100
        action [
            SetField(persistent, "ending_lavan_unlocked", True),
            SetField(persistent, "ending_macoi_unlocked", True),
            SetField(persistent, "ending_velvette_unlocked", True),
            SetField(persistent, "ending_cino_unlocked", True),
            SetField(persistent, "ending_single_unlocked", True),
            SetField(persistent, "ending_harem_unlocked", True),
            SetField(persistent, "cg_lavan_unlocked", True),
            SetField(persistent, "cg_macoi_unlocked", True),
            SetField(persistent, "cg_velvette_unlocked", True),
            SetField(persistent, "cg_cino_unlocked", True),
            SetField(persistent, "cg_single_unlocked", True),
            SetField(persistent, "cg_harem_unlocked", True),
            SetField(persistent, "cg_baking_unlocked", True)
        ]

    ## 2. ALLES SPERREN / VERGESSEN (Oben Rechts in der Ecke)
    button:
        xalign 1.0 ypos 0
        xsize 100 ysize 100
        action [
            SetField(persistent, "ending_lavan_unlocked", False),
            SetField(persistent, "ending_macoi_unlocked", False),
            SetField(persistent, "ending_velvette_unlocked", False),
            SetField(persistent, "ending_cino_unlocked", False),
            SetField(persistent, "ending_single_unlocked", False),
            SetField(persistent, "ending_harem_unlocked", False),
            SetField(persistent, "cg_lavan_unlocked", False),
            SetField(persistent, "cg_macoi_unlocked", False),
            SetField(persistent, "cg_velvette_unlocked", False),
            SetField(persistent, "cg_cino_unlocked", False),
            SetField(persistent, "cg_single_unlocked", False),
            SetField(persistent, "cg_harem_unlocked", False),
            SetField(persistent, "cg_baking_unlocked", False)
        ]
    ## ----------------------------------

    hbox:
        yalign 0.5

        ## extras menu navigation
        vbox:
            #spacing 25
            #xpos 50
            label "Extras"

            imagebutton auto "gui/button/gallery_%s.png" action SetScreenVariable("extra_menu", "gallery") alt "Gallery"
            imagebutton auto "gui/button/endings_%s.png" action SetScreenVariable("extra_menu", "endings") alt "Endings"
            # imagebutton auto "gui/button/ach_%s.png" action SetScreenVariable("extra_menu", "achievements") alt "Achievements"
            imagebutton auto "gui/button/return_%s.png" action Return() alt "Return"



    if extra_menu == "none":
        text ""
    elif extra_menu == "gallery":
        use gallery
    elif extra_menu == "endings":
        use endings
    # elif extra_menu == "achievements":
    #     use achievements
    else:
        text ""


style extras_label is gui_label
style extras_vbox is gui_vbox


style extras_vbox:
    spacing 25
    xpos 50

style extras_label_text:
    size gui.title_text_size
    color "#f5253c" #gui.accent_color
    font "font/OleoScriptSwashCaps-Regular.ttf"
    yoffset -150
    xpos 75

## Endings Screen ##################################################################
##
## This is code for the Ending screen
##
##
screen endings():

    style_prefix "endings"
    vbox:
        ## Sample Ending Code

        if persistent.ending_lavan_unlocked:
            text _("Ending: Lavan - Ein süßes Versprechen") color "#ff3a50"
        else:
            text _("Ending: ????")

        if persistent.ending_macoi_unlocked:
            text _("Ending: Macoi - Entspannte Zweisamkeit") color "#ff3a50"
        else:
            text _("Ending: ????")

        if persistent.ending_velvette_unlocked:
            text _("Ending: Velvette - Glamour & Kaffee") color "#ff3a50"
        else:
            text _("Ending: ????")

        if persistent.ending_cino_unlocked:
            text _("Ending: Cino - Das perfekte Rezept") color "#ff3a50"
        else:
            text _("Ending: ????")

        if persistent.ending_single_unlocked:
            text _("Ending: Single - Forever Alone") color "#ff3a50"
        else:
            text _("Ending: ????")  

        if persistent.ending_harem_unlocked:
            text _("Ending: All together - Together till the end") color "#ff3a50"
        else:
            text _("Ending: ????")        

style endings_vbox is vbox

style endings_vbox:
    xpos 675
    ypos 155
    spacing 25

style endings_text:
    color "#f5253c"
    font "font/OleoScriptSwashCaps-Regular.ttf"
    size 50

## Achievements Screen ##################################################################
##
## This is code for the Achievements screen
##
##

# screen achievements():
#     style_prefix "ach"

#     vbox:
#         if persistent.ach_1_unlocked:
#             text "Achievements One" color "#ff3a50"
#         else:
#             text "Achievement: ????"

#         if persistent.ach_2_unlocked:
#             text "Achievements Two" color "#ff3a50"
#         else:
#             text "Achievement: ????"

#         if persistent.ach_3_unlocked:
#             text "Achievements Three" color "#ff3a50"
#         else:
#             text "Achievement: ????"

#         if persistent.ach_4_unlocked:
#             text "Achievements Four" color "#ff3a50"
#         else:
#             text "Achievement: ????"


# style ach_vbox is vbox

# style ach_vbox:
#     xpos 675
#     ypos 155
#     spacing 25

# style ach_text:
#     color "#5d8282"
#     font "font/OleoScriptSwashCaps-Regular.ttf"
#     size 50


## Gallery Screen ##################################################################
##
## This is code for the gallery screens
##
##

screen gallery():

    style_prefix "extras"

    grid 3 3:
        spacing 30

        ## 1. BAKING
        if persistent.cg_baking_unlocked:
            imagebutton:
                idle im.Grayscale(im.Scale(cg_file_baking, thumb_x, thumb_y))
                hover im.Scale(cg_file_baking, thumb_x, thumb_y)
                action [ShowTransient('illustration'), SetVariable("cg", "baking")]
                alt "Baking CG"
        else:
            add im.Scale(cg_file_locked, thumb_x, thumb_y)

        ## 2. LAVAN
        if persistent.cg_lavan_unlocked:
            imagebutton:
                idle im.Grayscale(im.Scale(cg_file_lavan, thumb_x, thumb_y))
                hover im.Scale(cg_file_lavan, thumb_x, thumb_y)
                action [ShowTransient('illustration'), SetVariable("cg", "lavan")]
                alt "Lavan CG"
        else:
            add im.Scale(cg_file_locked, thumb_x, thumb_y)

        ## 3. MACOI
        if persistent.cg_macoi_unlocked:
            imagebutton:
                idle im.Grayscale(im.Scale(cg_file_macoi, thumb_x, thumb_y))
                hover im.Scale(cg_file_macoi, thumb_x, thumb_y)
                action [ShowTransient('illustration'), SetVariable("cg", "macoi")]
                alt "Macoi CG"
        else:
            add im.Scale(cg_file_locked, thumb_x, thumb_y)

        ## 4. VELVETTE
        if persistent.cg_velvette_unlocked:
            imagebutton:
                idle im.Grayscale(im.Scale(cg_file_velvette, thumb_x, thumb_y))
                hover im.Scale(cg_file_velvette, thumb_x, thumb_y)
                action [ShowTransient('illustration'), SetVariable("cg", "velvette")]
                alt "Velvette CG"
        else:
            add im.Scale(cg_file_locked, thumb_x, thumb_y)

        ## 5. CINO
        if persistent.cg_cino_unlocked:
            imagebutton:
                idle im.Grayscale(im.Scale(cg_file_cino, thumb_x, thumb_y))
                hover im.Scale(cg_file_cino, thumb_x, thumb_y)
                action [ShowTransient('illustration'), SetVariable("cg", "cino")]
                alt "Cino CG"
        else:
            add im.Scale(cg_file_locked, thumb_x, thumb_y)

        ## 6. SINGLE
        if persistent.cg_single_unlocked:
            imagebutton:
                idle im.Grayscale(im.Scale(cg_file_single, thumb_x, thumb_y))
                hover im.Scale(cg_file_single, thumb_x, thumb_y)
                action [ShowTransient('illustration'), SetVariable("cg", "single")]
                alt "Single CG"
        else:
            add im.Scale(cg_file_locked, thumb_x, thumb_y)

        ## 7. HAREM
        if persistent.cg_harem_unlocked:
            imagebutton:
                idle im.Grayscale(im.Scale(cg_file_harem, thumb_x, thumb_y))
                hover im.Scale(cg_file_harem, thumb_x, thumb_y)
                action [ShowTransient('illustration'), SetVariable("cg", "harem")]
                alt "Harem CG"
        else:
            add im.Scale(cg_file_locked, thumb_x, thumb_y)   

        null   # Füllt Platz 8 auf
        null   # Füllt Platz 9 auf        

style extras_grid is gui_grid

style extras_grid:
    # spacing 25 # Haben wir jetzt direkt im Grid definiert
    xpos 650
    ypos 160


#### CG IMAGES CODE GO HERE (Der Teil bleibt fast gleich, nutzt aber die neuen Variablen)
screen illustration():

    modal True # WICHTIG: Damit man nicht durch das große Bild hindurch klicken kann

    # Ein schwarzer Hintergrund, damit das Menü drunter abgedunkelt wird
    add Solid("#000000c0")

    ## Das große Bild anzeigen
    if cg == "lavan":
        add cg_file_lavan # Nutzt die Variable von oben
    elif cg == "macoi":
        add cg_file_macoi
    elif cg == "velvette":
        add cg_file_velvette
    elif cg == "cino":
        add cg_file_cino
    elif cg == "single":
        add cg_file_single
    elif cg == "harem":
        add cg_file_harem
    elif cg == "baking":
        add cg_file_baking
    else:
        text "Error: No Illustration Found" xalign 0.5 yalign 0.5 color "#fff"

    ## Return Button
    button:
        background None # Macht den Button komplett unsichtbar
        xpos 0
        ypos 0
        xsize 1920
        ysize 1080
        action Hide('illustration')

style illustration_button is button
style illustration_button_text is button_text

style illustration_button:
    xpos 1660
    ypos 960

style illustration_button_text:
    idle_color "#ffffff"
    hover_color "#ff3a50"
    size 75
