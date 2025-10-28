## 01_definitions.rpy

# -- 1. Charakter-Definitionen --
define user = Character("[player_name]") 
define l = Character("Lavan", color="#9a6f34c5") 
define m = Character("Macoi", color="#bef778")
define v = Character("Velvette", color="#ac1c1c")
define c = Character("Cino", color="#f1d576") 

# -- 2. Spiel-Variablen (default = wird bei "Neuem Spiel" zurückgesetzt) --
default player_gender = None
default player_name = ""
default mc_title = None
default mc_pronoun_he_she = None
default mc_pronoun_his_her = None
default mc_pronoun_article = None

# --- LI-Status-Flaggen ---
# Ist ein Check ob der Char schon erstellt wurde oder nicht.
default is_lavan_awakened = False
default is_macoi_awakened = False
default is_velvette_awakened = False
default is_cino_awakened = False

# Affection Points der Chars
default lavan_points = 0
default macoi_points = 0
default velvette_points = 0
default cino_points = 0

# --- EVENT-FLAGGEN ---
# (Diese steuern, was im Hub-Menü sichtbar ist)
default event_lavan_1_done = False
default event_macoi_1_done = False
default event_velvette_1_done = False
default event_cino_1_done = False
default event_cafe_minigame_1_done = False

# -- 3. Permanente Variablen (persistent = überleben "Neues Spiel") --
# (Für zum Beispiel Galerie)
default persistent.unlocked_cg_lavan_1 = False

# -- 4. Bild-Aliase (Shortcuts für Images) --
# (thumb=Thumbnails, cg=Cutscene-Stuff, bg=Background, lavan=Char-Beispiel)

# MC
image mc_neutral = ConditionSwitch(
    "player_gender == 'male'", "images/sprites/mc/male/neutral.png",
    "player_gender == 'female'", "images/sprites/mc/female/neutral.png",
)

# Lavan
image lavan smile = "images/sprites/lavan/smile.png"

# Macoi
image macoi smile = "images/sprites/macoi/smile.png"

# Velvette
image velvette smile = "images/sprites/velvette/smile.png"

# Cino
image cino smile = "images/sprites/cino/smile.png"

# Backgrounds
image bg cafe = "images/backgrounds/cafe.jpg"

# Gallery Stuff
image cg lavan 1 = "images/gallery/cg_lavan_hug.jpg"
image cg lavan 1 thumb = "images/gallery/thumb_lavan_hug.jpg" 

# -- 5. Transform-Definitionen (Position-Definierung) --
transform at_left:
    xalign 0.25 yalign 1.0
transform at_right:
    xalign 0.75 yalign 1.0