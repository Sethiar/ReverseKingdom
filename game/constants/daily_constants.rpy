
#==================================
# Moments de la journée généraux.
#==================================


# Items principaux des menus journaliers.
label constants_day:
    
    menu:
        "Aller à la chasse.":
            jump GoToHunt

        "Aller au village.":
            jump GoToVillage

        "Augmenter l'intelligence.":
            jump GotoIntelligence

        "Améliorer la magie.":
            jump GotoMana

        "Augmenter la force.":
            jump GotoStrengh

    return

# Items du menu du matin.
label start_day:
    
    # image bg = daily_up.png
    mc "Que fais-je faire ce matin ?"
    
    call constants_day
    
    menu:
        "Ne rien faire.":
            jump GoToLazy


# Items du milieu de journée.
label middle_day:

    call constants_day

    menu:
        "Faire une sieste":
            jump GoToLazy


# Items du soir.
label finish_day:
    
    menu: 
        "Rêver.":
            jump start_dream

        "Sommeil répérateur":
            jump sleep
        