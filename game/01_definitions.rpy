## 01_definitions.rpy

# (aaa,bbb,ccc und ddd sind PLACEHOLDER)

# -- 1. Charakter-Definitionen --
define mc = Character("[player_name]") 
define a = Character("aaaa", color="#ffb6c1") 
define k = Character("bbbb", color="#a0e9ff")
define m = Character("cccc", color="#d8bfd8")
define r = Character("dddd", color="#90ee90") 

# -- 2. Spiel-Variablen (default = wird bei "Neuem Spiel" zurückgesetzt) --
default main_story_progress = 1 # Zählt, in welchem "Kapitel/Akt" wir sind.

# Affection Points
default aaa_points = 0
default bbb_points = 0
default ccc_points = 0
default ddd_points = 0

# --- EVENT-FLAGGEN ---
# (Diese steuern, was im Hub-Menü sichtbar ist)
default event_aaa_1_done = False
default event_bbb_1_done = False
default event_ccc_1_done = False
default event_ddd_1_done = False
default event_cafe_minigame_1_done = False


# -- 3. Permanente Variablen (persistent = überleben "Neues Spiel") --
# (Für Galerie, Achievements, etc.)
default persistent.unlocked_cg_aaa_1 = False

# -- 4. Bild-Aliase (Shortcuts) --
# (thumb ist für Thumbnails)
image bg cafe = "images/backgrounds/cafe.jpg"
image aaa smile = "images/sprites/aaa/smile.png"
image cg aaa 1 = "images/gallery/cg_aaa_kiss.jpg"
image cg aaa 1 thumb = "images/gallery/thumb_aaa_kiss.jpg" 

# -- 5. Transform-Definitionen (Positionen) --
transform at_left:
    xalign 0.25 yalign 1.0
transform at_right:
    xalign 0.75 yalign 1.0