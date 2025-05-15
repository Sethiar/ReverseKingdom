#===========================================
# Script qui détermine les choix du MC
#===========================================


# Premier choix du MC.
label first_choice:
    "Présentation du choix du tutoriel."
    
    menu:        
        "Aller chasser (Tutoriel Chasse)." if menu_tuto_hunt:
            jump start_tuto_hunt 
        #"S'entraîner à la magie (Tutoriel Magie).":
            #jump start_tuto_mana
        "Aller au Village.":
            jump GoToVillage_01


