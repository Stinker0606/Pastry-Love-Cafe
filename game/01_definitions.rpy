## -- 1. Charakter-Definitionen --
define user = Character("[player_name]")
define l = Character("Lavan", color="#9a6f34c5")
define m = Character("Macoi", color="#bef778")
define v = Character("Velvette", color="#ac1c1c")
define c = Character("Cino", color="#f1d576")
define p = Character("Pierre", color="#9b73f8")
define k = Character("STAMMKUNDIN", color="#0f0475")
define fm = Character ("Fremder Mann", color="#0f0475" )

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

## --- TAGES-PERFORMANCE TRACKER ---
## Status kann sein:
## "ignored" = Man hat dem Char gar nicht geholfen (Standardwert, gilt als schlecht)
## "fail"    = Man hat geholfen, aber die falsche Antwort gewählt
## "success" = Man hat geholfen und die richtige Antwort gewählt

default task_result_lavan = "ignored"
default task_result_macoi = "ignored"
default task_result_velvette = "ignored"
default task_result_cino = "ignored"

## --- UI-Status-Variablen ---
# default current_textbox_color = None | AUS, ist damit die box unten sich mit ändert beim hovern

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
image lavan angry = Transform(Movie(play="images/sprites/lavan/Lavan_Angry_slow.webm", loop=True, side_mask=True), zoom=0.45)

image lavan blush = Transform(Movie(play="images/sprites/lavan/Lavan_Blush_slow.webm", loop=True, side_mask=True), zoom=0.45)

image lavan happy = Transform(Movie(play="images/sprites/lavan/Lavan_Happy_slow.webm", loop=True, side_mask=True), zoom=0.45)

image lavan neutral = Transform(Movie(play="images/sprites/lavan/Lavan_Neutral_slow.webm", loop=True, side_mask=True), zoom=0.45)

image lavan sad = Transform(Movie(play="images/sprites/lavan/Lavan_Sad_slow.webm", loop=True, side_mask=True), zoom=0.45)

## Macoi

## Velvette
image velvette angry = Transform(Movie(play="images/sprites/velvette/Velvette_Angry_slow.webm", loop=True, side_mask=True), zoom=0.45)

image velvette blush = Transform(Movie(play="images/sprites/velvette/Velvette_Blush_slow.webm", loop=True, side_mask=True), zoom=0.45)

image velvette happy = Transform(Movie(play="images/sprites/velvette/Velvette_Happy_slow.webm", loop=True, side_mask=True), zoom=0.45)

image velvette neutral = Transform(Movie(play="images/sprites/velvette/Velvette_Neutral_slow.webm", loop=True, side_mask=True), zoom=0.45)

image velvette sad = Transform(Movie(play="images/sprites/velvette/Velvette_Sad_slow.webm", loop=True, side_mask=True), zoom=0.45)

## Cino


## Backgrounds
image bg pink = Solid("#ffb6c1")
image bg white = Solid("#ffffff")
image bg cafe = Transform("images/backgrounds/Counter_Background.png", size=(1920, 1080))
image bg kitchen = Transform("images/backgrounds/Baking_Game_Background.png", size=(1920, 1080))
image bg cinema = Transform("images/backgrounds/Cinema_Background.png", size=(1920, 1080))
image bg boutique = Transform("images/backgrounds/Clothing_Store_Background.png", size=(1920, 1080))
image bg mall = Transform("images/backgrounds/Mall_Inside_Background.png", size=(1920, 1080))

## Gallery Stuff
image cg 1 = Transform("images/gallery/cg_lavan_hug.jpg", size=(1920, 1080))
image cg 1 thumb = Transform("images/gallery/thumb_lavan_hug.jpg", size=(1920, 1080))

## Minigame Images

## Other Images
image team_logo = "gui/team_logo.png"

## -- 5. Transform-Definitionen (Position-Definierung) --

transform left:
    xalign 0.25 yalign 1.0
transform right:
    xalign 0.75 yalign 1.0
transform middle:
    xalign 0.50 yalign 1.0    

## -- Spezielle Positionen für 4 Personen - AWAKENING SCENE
transform pos_1:
    xalign 0.07 yalign 1.0 # Ganz links

transform pos_2:
    xalign 0.36 yalign 1.0 # Links Mitte

transform pos_3:
    xalign 0.64 yalign 1.0 # Rechts Mitte

transform pos_4:
    xalign 0.94 yalign 1.0 # Ganz rechts

## Normale Positionen

transform pos_01:
    xalign 0.07 yalign 0.3 # Ganz links

transform pos_02:
    xalign 0.90 yalign 0.15 # Ganz rechts

## 5.1 -- Animations für Schrift und anderen Stuff --

## Lässt XY leicht auf und ab schweben
transform result_floating_anim:
    yoffset 0
    linear 2.0 yoffset -15 # 2 Sekunden lang 15px hoch
    linear 2.0 yoffset 0   # 2 Sekunden lang wieder runter
    repeat

## Lässt XY an und aus blinken
transform alpha_flash:
    alpha 1.0
    linear 0.5 alpha 0.2
    linear 0.5 alpha 1.0
    repeat

## -- 6. MINIGAME Definierungen & Grundlogik --
init python:

    recipes_data = {

        ## --- TUTORIAL REZEPT ---
        "Tutorial": {
            ## Die Liste 'steps' definiert die ZWINGENDE Reihenfolge.
            ## Nutzung einer Liste (Array) garantiert index-basierten Zugriff.
            "steps": ["Mehl", "Ei", "Ei", "Ei", "Mixen", "Milch", "Zucker", "Zucker", "Mixen"],
            "type": "bowl" # 'type' steuert, welcher Minigame-Screen geladen wird (Factory Pattern)
        },

        ## --- ALLTAGS-REZEPT 1: BUTTERPLÄTZCHEN ---
        "Butterplätzchen": {
            "steps": ["Mehl", "Ei", "Ei", "Zucker", "Butter", "Streusel", "Mixen"],
            "type": "bowl" # Normales Schüssel-Rezept
        },

        ## --- ALLTAGS-REZEPT 2: ERDBEER CREPE --- Komplexes Rezept
        "Erdbeer Crepe": {
            ## Hier sieht man die Skalierbarkeit: Neue Zutaten erfordern keinen Code-Change.
            "steps": ["Mehl", "Milch", "Milch", "Ei", "Ei", "Zucker", "Butter", "Mixen"],
            "type": "crepe" # Trigger für Phasen-Wechsel (Teig -> Pfanne)
        }
    }
    
