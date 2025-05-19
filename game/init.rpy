#======================================================#
# Fichier d'initialisation du jeu.
#======================================================#

# Définition de la variable nom du joueur.
define mc = DynamicCharacter("[player_name]", color="#DE7915")
define mc_thought = Character("[player_name]", kind=mc, what_italic=True, what_prefix="(", what_suffix=")")

init -1:
    # Affichage du cadre du jeu si True.
    default frame_ON = False

    # Affichage du choix tuto_chasse dans le menu.
    default menu_tuto_hunt = True 

    # Caractéristiques du personnage MC
    # Skills
    default mc_intelligence = 2
    default mc_strength = 1
    default mc_mana = 3
    default mc_dexterity = 1
    
    # Corruption_system
    default holiness_mc = 0
    default corruption_mc = 0
    

    # Affection corruption personnages.
    # Ingrid
    default corruption_ing = 0
    default affection_ing= 0

    # Isis
    default corruption_isi = 0
    default affection_isi= 0
    
    # Clara
    default corruption_cl = 0
    default affection_cl= 0