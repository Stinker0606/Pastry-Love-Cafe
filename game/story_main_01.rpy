label test_hub:
    
    
    menu:

        user "Was möchtest du testen?"

        "{#lavan}Lavan: Event 1 (Erste Begegnung)":
            jump lavan_event_1
            
        "{#lavan}Lavan: Event 2 (Tieferes Gespräch)":
            jump lavan_event_2
        
        "{#macoi}Macoi: Event 1 (Kennenlernen)":
            jump macoi_event_1
            
        "{#velvette}Velvette: Event 1 (Test für Velvette, Event 1)":
            jump velvette_event_1
            
        "{#cino}Cino: Event 4 (Test für Cino, Event 4)":
            # Du kannst zu JEDEM Label springen!
            jump cino_event_4
            
        "Spiel beenden (Test fertig)":
            return # Beendet das Spiel