#===========================================#
# Script qui détermine les choix du MC
#===========================================#


# Premier choix du MC.
label first_choice:
    "Que fais-je faire ??"
    menu:        
        "Aller chasser (Tutoriel Chasse)." if menu_tuto_hunt:
            jump start_tuto_hunt
        "Aller au Village.":
            jump GoToVillage_01


