label awakening_sequence_start:
    scene bg kitchen
    
    user "Aber ich habe noch Restwärme..."
    user "Ich backe den Rest schnell hinterher!"
    
    # Hier simulieren wir das "automatische Backen" der anderen
    scene black
    with fade
    user "(Backt weiter oder so...)"
    
    # Wir setzen ALLE auf "erweckt", egal wen man gewählt hat
    $ is_lavan_awakened = True
    $ is_macoi_awakened = True
    $ is_velvette_awakened = True
    $ is_cino_awakened = True
    
    narrator "Einige Zeit später..."
    
    scene bg cafe
    
    # Hier würden erscheinen alle Sprites danach
    show lavan smile
    show macoi smile
    show velvette smile
    show cino smile

    user "Wtf?"
    
    if first_li_chosen == "Lavan":
        l "Thx"
    elif first_li_chosen == "Macoi":
        m "Danke"
    elif first_li_chosen == "Velvette":
        v "dankeee"    
    elif first_li_chosen == "Cino":
        c "Uwu idk"

    jump alltag_start