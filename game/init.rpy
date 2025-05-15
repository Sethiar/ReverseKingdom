#======================================================#
# Fichier d'initialisation du jeu.
#======================================================#

# Définition de la variable nom du joueur.
default player_name = "John-Doe"
define mc = DynamicCharacter("[player_name]", color="#DE7915")
define mc_thought = Character("[player_name]", kind=mc, what_italic=True, what_prefix="(", what_suffix=")")

init -1:


    # Affichage du cadre du jeu si True.
    default frame_ON = False

    # Affichage du choix tuto_chasse dans le menu.
    default menu_tuto_hunt = True 

    # Animation clignotante
    image tuto_marker_anim:
        "gui/interface/Effects/tuto_mark_1.png"
        0.5
        "gui/interface/Effects/tuto_mark_2.png"
        0.5
        repeat

    