# WICHTIG: Hier oben in den Klammern müssen die Variablen stehen!
screen finding_game_screen(bg_image, obj_idle, obj_hover, obj_x, obj_y, obj_scale):
    
    # 1. Der Hintergrund (Dynamisch)
    add bg_image:
        size (1920, 1080)

    # 2. Das gesuchte Objekt
    imagebutton:
        # Wir nutzen die Variablen aus der Klammer oben
        idle Transform(obj_idle, zoom=obj_scale)
        hover Transform(obj_hover, zoom=obj_scale)
        
        focus_mask True
        
        # Dynamische Position
        xpos obj_x
        ypos obj_y
        
        action Return("found")
        