label test_hub:
    
    user "Was möchtest du testen?"
    
    menu:
        "Lavan: Event 1 (Erste Begegnung)":
            jump lavan_event_1
            
        "Lavan: Event 2 (Tieferes Gespräch)":
            jump lavan_event_2
        
        "Macoi: Event 1 (Kennenlernen)":
            jump macoi_event_1
            
        "Velvette: Event 1 (Test für Velvette, Event 1)":
            jump velvette_event_1
            
        "Cino: Event 4 (Test für Cino, Event 4)":
            # Du kannst zu JEDEM Label springen!
            jump cino_event_4
            
        "Spiel beenden (Test fertig)":
            return # Beendet das Spiel