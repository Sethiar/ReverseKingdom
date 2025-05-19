
#==========================================================#
#============== Ajout de Nosiris ==========================#
#==========================================================#


screen cadre_frame():
    if frame_ON:

        frame:
            style "frame"
            xfill True
            yfill True

screen arrow_1():
    add "gui/interface/Effects/Arrow_1.png": 
        at move_arrow(180)

screen arrow_2():
    add "gui/interface/Effects/Arrow_1.png": 
        at move_arrow(280)      

screen arrow_3():
    add "gui/interface/Effects/Arrow_1.png": 
        at move_arrow(380)

transform move_arrow(y):
    xpos 270 ypos y
    linear 1.0 xpos 155


# Accès à l'interface.
label interface_menu:
    show screen interface_buttons
    $ renpy.pause(9999, hard=True)

# Activation des boutons du gameplay.
screen interface_buttons():
    # Bouton de l'interface.
    imagebutton auto "gui/interface/Icons/ico_interface_%s.png" action [Hide("interface_buttons"), Show("interface_main")] pos (90 , 180)
    # Accès rapide à l'écran des quêtes.
    imagebutton auto "gui/interface/Icons/ico_quest_%s.png" action [Hide("interface_buttons"), Show("interface_quest")] pos (90 , 280)
    # Accès rapide à l'écran des relations.
    imagebutton auto "gui/interface/Icons/ico_rela_%s.png" action [Hide("interface_buttons"), Show("interface_rela")] pos (90 , 380)

label interface_main:
    scene bg RK_Gameplay_Interface with fade
    no "Voici l'interface, vous pouvez accéder à ..."

screen interface_main():
    tag interface
    add "gui/interface/Screens/RK_Gameplay_Interface.png" at truecenter
    use interface_buttons2
  
# Activation des boutons de l'interface utilisateur.
screen interface_buttons2():
    # Bouton skills avec trois états.
    imagebutton auto "gui/interface/Buttons/btn_skills_%s.png" action Show("interface_skills") pos ( 10, 320)
    # Bouton quêtes avec trois états.
    imagebutton auto "gui/interface/Buttons/btn_quest_%s.png" action Show("interface_quest") pos ( 10, 420)
    # Bouton inventaire avec trois états.
    imagebutton auto "gui/interface/Buttons/btn_inv_%s.png" action Show("interface_inv") pos ( 10, 520)
    # Bouton equipement avec trois états.
    imagebutton auto "gui/interface/Buttons/btn_equip_%s.png" action Show("interface_equip") pos ( 10, 620)
    # Bouton relation avec trois états.
    imagebutton auto "gui/interface/Buttons/btn_rela_%s.png" action Show("interface_rela") pos ( 10, 720)  


label interface_skills:
    show screen interface_skills
    show screen skill_mc
    
    $ renpy.pause(9999, hard=True)

screen interface_skills():
    tag interface
    add "gui/interface/Screens/RK_Gameplay_Interface_skills.png"
    use interface_buttons2


label interface_quest:
    show screen interface_quest
    $ renpy.pause(9999, hard=True)

screen interface_quest():
    tag interface
    add "gui/interface/Screens/RK_Gameplay_Interface_quest.png"
    use interface_buttons2


label interface_equip:
    show screen interface_equip
    $ renpy.pause(9999, hard=True)

screen interface_equip():
    tag interface
    add "gui/interface/Screens/RK_Gameplay_Interface_equip.png"
    use interface_buttons2


label interface_rela:
    show screen interface_rela
    $ renpy.pause(9999, hard=True)

screen interface_rela:
    tag interface
    add "gui/interface/Screens/RK_Gameplay_Interface_rela.png"
    use interface_buttons2


label interface_inv:
    show screen RK_Gameplay_Interface_inv
    $ renpy.pause(9999, hard=True)

screen interface_inv():
    tag interface
    add "gui/interface/Screens/RK_Gameplay_Interface_inv.png"
    use interface_buttons2 


#---------------------------------------------------------------------#
# Screen des tutoriels.
#---------------------------------------------------------------------#

# Screen hunt.
screen hunt_Gameplay():
    add "gui/minigames/hunt/background/bg_huntGameplay.png"

# Curseur souris.


# Animation de la flèche.
screen hunt_arrow_1:
    add "gui/interface/Effects/Arrow_1.png": 
        at move_arrow2

transform move_arrow2:
    xpos 290 ypos 575
    linear 1.0 xpos 185

# Changement du curseur de la souris.
screen set_cursor(name):
    on "show" action SetMouseCursor(name)

# Animation de l'escargot.
screen snail_on:
    add "snail_move_across"

image snail_move_across:
    "snail_move"    
    ypos 650 xpos 1250
    linear 3.0 xpos 1000
    repeat


image snail_move = Animation(
    "gui/minigames/hunt/objects/enemy/snail_sprite/sn_5.png", 0.1,
    "gui/minigames/hunt/objects/enemy/snail_sprite/sn_1.png", 0.1,
    loop=True
    )

# Screen dream.
# Screen intelligence.

#---------------------------------------------------------------------
# Il s'agit des menus du jeu rangés.

# Menus uniques.


# Daily Moments.
# Menu du matin.

# Menu de l'après-midi.

# Menu du soir.

# Cavern.


# Village.

# Menu principal village
label menu_village:
    mc_thought "Où vais-aller ?"
    menu: 
        "Aller à l'auberge": 
            jump inns
        "Aller au puit" if well_on:
            jump well
        "Aller chez le forgeron" if forge_on:
            jump forge
        "Se promener":
            jump walking_village
    return


    # Fin de l'information courruption.
    

# Menu Rêves
# Rêve 1 ------------- Le monde d'avant ----------------


#________________________________________________________________________________________________
