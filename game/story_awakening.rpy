## Spezielles einmaliges Ereignis nach dem ersten mal backen.
label awakening_shock_scene:
    scene black
    user "Okay, das erste Rezept ist fertig. Aber ich habe noch Energie..."
    narrator "Du backst den Rest automatisch..."
    jump awakening_sequence_start

label awakening_sequence_start:
    scene bg cafe
    
    ## Alle sind da
    $ is_lavan_awakened = True
    $ is_macoi_awakened = True
    $ is_velvette_awakened = True
    $ is_cino_awakened = True
    
    show lavan smile at pos_1
    show macoi smile at pos_2
    show velvette smile at pos_3
    show cino smile at pos_4

    user "Was ist hier los!"
    
    if first_li_chosen == "Lavan":
        l "Danke fürs Backen."
    elif first_li_chosen == "Macoi":
        m "Interessant."
    
    jump story_intro_02