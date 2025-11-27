## -- 1. Charakter-Definitionen --
define user = Character("[player_name]") 
define l = Character("Lavan", color="#9a6f34c5") 
define m = Character("Macoi", color="#bef778")
define v = Character("Velvette", color="#ac1c1c")
define c = Character("Cino", color="#f1d576") 

## -- 2. Spiel-Variablen (default = wird bei "Neuem Spiel" zurückgesetzt) --
default player_gender = None
default player_name = ""
default mc_title = None
default mc_pronoun_he_she = None
default mc_pronoun_his_her = None
default mc_pronoun_article = None

## --- LI-Status-Flaggen ---
## Ist ein Check ob der Char schon erstellt wurde oder nicht.
default is_lavan_awakened = False
default is_macoi_awakened = False
default is_velvette_awakened = False
default is_cino_awakened = False

## --- WICHTIGE VARIABLEN ---
default first_li_chosen = None # Wer wurde im Tutorial zuerst gewählt?
default tutorial_baking_done = False # Wurde das Tutorial beendet?
default current_kitchen_helper = None # Wer hilft beim backen?
default day = 1 # Welcher Tag ist heute?
default current_ingredients = [] # Die Liste der Zutaten, die aktuell in der Schüssel liegen.
default current_recipe_name_global = "" # Speichert den Namen des Rezepts, das gerade im Minigame gebacken wird
default is_whisk_held = False # Überprüfung ob der Schneebesen gehalten wird

## --- Affection Points der Chars ---
default lavan_points = 0
default macoi_points = 0
default velvette_points = 0
default cino_points = 0

## --- UI-Status-Variablen ---
## default current_textbox_color = None | AUS, ist damit die box unten sich mit ändert beim hovern

## --- EVENT-FLAGGEN ---
## (Diese steuern, was im Hub-Menü sichtbar ist)
default event_lavan_1_done = False
default event_macoi_1_done = False
default event_velvette_1_done = False
default event_cino_1_done = False
default event_cafe_minigame_1_done = False

## -- 3. Permanente Variablen (persistent = überleben "Neues Spiel") --
## (Für zum Beispiel Galerie)
default persistent.unlocked_cg_1 = False

## -- 4. Bild-Aliase (Shortcuts für Images) --
## (thumb=Thumbnails, cg=Cutscene-Stuff, bg=Background, lavan=Char-Beispiel)

## MC
image mc_neutral = ConditionSwitch(
    "player_gender == 'male'", "images/sprites/mc/male/neutral.png",
    "player_gender == 'female'", "images/sprites/mc/female/neutral.png",
)

## Lavan
image lavan smile = "images/sprites/lavan/smile.png"

## Macoi
image macoi smile = "images/sprites/macoi/smile.png"

## Velvette
image velvette smile = "images/sprites/velvette/smile.png"

## Cino
image cino smile = "images/sprites/cino/smile.png"

## Backgrounds
image bg pink = Solid("#ffb6c1")
image bg cafe = "images/backgrounds/cafe.jpg"
image bg kitchen = "images/backgrounds/kitchen.jpg"

## Gallery Stuff
image cg 1 = "images/gallery/cg_lavan_hug.jpg"
image cg 1 thumb = "images/gallery/thumb_lavan_hug.jpg" 

## Minigame Images

## Other Images
image team_logo = "gui/team_logo.png"

## -- 5. Transform-Definitionen (Position-Definierung) --
transform at_left:
    xalign 0.25 yalign 1.0
transform at_right:
    xalign 0.75 yalign 1.0

# -- Spezielle Positionen für 4 Personen - AWAKENING SCENE
transform pos_1:
    xalign 0.15 yalign 1.0 # Ganz links

transform pos_2:
    xalign 0.38 yalign 1.0 # Links Mitte

transform pos_3:
    xalign 0.62 yalign 1.0 # Rechts Mitte

transform pos_4:
    xalign 0.85 yalign 1.0 # Ganz rechts

## -- 6. MINIGAME Definierungen & Grundlogik --
init python:
    
    recipes_data = {
        
        # --- TUTORIAL REZEPT ---
        "Tutorial": {
            "steps": ["Mehl", "Ei", "Ei", "Ei", "Mixen", "Milch", "Zucker", "Zucker", "Mixen"],
            "type": "bowl" # Normales Schüssel-Rezept
        },

        # --- ALLTAGS-REZEPT 1: BUTTERPLÄTZCHEN ---
        "Butterplätzchen": {
            "steps": ["Mehl", "Ei", "Ei", "Zucker", "Butter", "Streusel", "Mixen"],
            "type": "bowl"
        },

        # --- ALLTAGS-REZEPT 2: ERDBEER CREPE ---
        "Erdbeer Crepe": {
            # Phase 1: Teig mischen
            "steps": ["Mehl", "Milch", "Ei", "Ei", "Zucker", "Mixen"],
            "type": "crepe" # Löst danach das Pfannen-Minigame aus
        }
    }
