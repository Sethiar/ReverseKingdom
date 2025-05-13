

#=============================================================
# Fichier des tutoriels du jeu.
#=============================================================


# Tutoriel Rêves.
label start_tuto_dream:

    # image bg = "scene_intro_sleep_1.png" (grotte) -- mc
    # image bg = "scene_intro_sleep_2.png" (grotte) -- mc
    # image bg = "scene_intro_enter_dream.png" (grotte) -- mc
    
    # Le MC est dans son lit et il se réveille dans la chambre de son ancien monde.
    # Il a 15 ans.
    # image bg = "scene_intro_dream_1.png" (bedroom) -- mc
    # image bg = "scene_intro_dream_2.png" (bedroom) -- mc
    mc "Waah !!! Le rêve de dingue..."
    mc "Je suis dans mon monde..."
    mc "Je suis dans ma chambre..."
    
    # image bg = "scene_intro_dream_3.png" (bedroom) -- mc insistance sur la chambre plan large
    mc "Ma Chambre ..???"
    mc "La chambre de mon adolescence..."
    mc "Mais qu'est-ce que je fous là ?"
    
    # On frappe à la porte de la chambre.
    son "Toc toc toc !!!"
    
    # image bg = "scene_intro_dream_4.png" (bedroom) -- porte de la chambre -- vue intérieur
    vf "[player_name] !! [player_name] !!!"
    vf "Dépêche-toi de venir manger, c'est prêt !!"
    
    mc "C'est la voix de Clara..."
    mc "Aaaahhh Clara..."
    
    #----------------
    # Choix du mc
    #----------------
    
    # Scène où on voit la porte des yeux du MC.
    # image bg = "scene_intro_dream_5.png"
    label intro_dream:
        mc "Étant donné que je rêve"
        mc "je peux faire ce que je veux !!!"
        # image bg = "scene_intro_dream_5.png"
        
        menu:
            "Se lever":
                jump scene_get_up
            "L'insulter":
                jump scene_fuck_up
                
    label scene_get_up:
        mc "Je me lève tout de suite, j'arrive !!"
        # image bg = scene_get_up.png
        mc "Je suis pressé de voir Clara, même en rêve."
        jump go_on

    label scene_fuck_up:
        mc "Va te faire foutre, Salope !!"
        # image bg = scene_fuck_up.png
        # La porte s'ouvre violemment.
        # image bg "scene_fuck_up2.png"
        # Clara fulmine en hurlant sur MC.
        cl "[player_name] comment oses-tu ???"
        cl "Quoi !! Comment tu me parles, petit avorton de merde !!"
        # image bg "clara_dream_intro_1.png"

        jump fuck_up 
    
    label go_on:
        # Arrivé à la table du petit-déjeuner, Clara, dos à la scène, au niveau de l'évier.
        # MC s'assoit sur la chaise de droite dos à la fenêtre.
        mc "Bonjour Clara !!"
        mc "Comment vas-tu aujourd'hui ??"

   
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Affichage de la section suivante : ...
    jump start_day
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


label start_tuto_hunt:


    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Affichage de la section suivante : ...
    jump start_day
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


label start_tuto_mana:


    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Affichage de la section suivante : ...
    jump start_day
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


