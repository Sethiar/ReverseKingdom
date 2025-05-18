

#=============================================================
# Fichier des tutoriels du jeu.
#=============================================================
image page_test_1 = "images/PageTest/1.png"
image page_test_2 = "images/PageTest/2.png"
image page_test_3 = "images/PageTest/3.png"


# Tutoriel Rêves.
label start_tuto_dream:

    show page_test_1 with dissolve
    # image bg = "scene_intro_sleep_2.png" (grotte) -- mc_thought
    # image bg = "scene_intro_enter_dream.png" (grotte) -- mc_thought
    
    # Le mc_thought est dans son lit et il se réveille dans la chambre de son ancien monde.
    # Il a 15 ans.
    # image bg = "scene_intro_dream_1.png" (bedroom) -- mc_thought
    # image bg = "scene_intro_dream_2.png" (bedroom) -- mc_thought
    mc_thought "Waah !!! Le rêve de dingue..."
    mc_thought "Je suis dans mon monde..."
    mc_thought "Je suis dans ma chambre..."
    
    # image bg = "scene_intro_dream_3.png" (bedroom) -- mc_thought insistance sur la chambre plan large
    mc_thought "Ma Chambre ..???"
    mc_thought "La chambre de mon adolescence..."
    mc_thought "Mais qu'est-ce que je fous là ?"
    
    # On frappe à la porte de la chambre.
    son "Toc toc toc !!!"
    
    # image bg = "scene_intro_dream_4.png" (bedroom) -- porte de la chambre -- vue intérieur
    vf "[player_name] !! [player_name] !!!"
    vf "Dépêche-toi de venir manger, c'est prêt !!"
    
    mc_thought "C'est la voix de Clara..."
    mc_thought "Aaaahhh Clara..."
    
    #----------------
    # Choix du mc_thought
    #----------------
    
    # Scène où on voit la porte des yeux du mc_thought.
    # image bg = "scene_intro_dream_5.png"
    label intro_dream:
        # Mise à zéro des valeurs du mini-jeu.
        $ dream_game.reset()

        mc_thought "Étant donné que je rêve"
        mc_thought "je peux faire ce que je veux !!!"
        # image bg = "scene_intro_dream_5.png"
        
        menu:
            "Se lever":
                jump scene_get_up
            "L'insulter":
                jump scene_fuck_up
        return        
                
    label scene_get_up:
        mc "Je me lève tout de suite, j'arrive !!"
        # image bg = scene_get_up.png
        mc_thought "Je suis pressé de voir Clara, même en rêve."
        jump go_on
        return

    label scene_fuck_up:
        
        show screen awake_meter
        mc "Va te faire foutre, Salope !!"
        # image bg = scene_fuck_up.png
        # La porte s'ouvre violemment.
        # image bg "scene_fuck_up2.png"
        
        # Clara fulmine en hurlant sur mc_thought.
        cl "[player_name] comment oses-tu ???"
        cl "Quoi !! Comment tu me parles, petit avorton de merde !!"
        
        # image bg "Clara tombe en se prenant les jambres dans le pantalon du MC.
        cl "Ahhhhhh"
        cl "[player_name] !! Attention !!!"
        
        # Mc nu au lit en érection qui essaie de la rattraper.
        mc "Clara !!!"

        # Clara tombe sur le lit sur MC.
        # scene screen positionc_cl_Mc_dream.png
        mc_thought "Oups... J'ai ma bite entre ses seins...!!!" 
        mc_thought "Et assez proche de ses lèvres..."

        mc_thought "Voyons voir jusqu'où je peux contrôler ce rêve sans me réveiller."

        menu:
            "Ne rien faire":
                jump go_on
            "Toucher ses seins.":
                jump dream_tits_1
            "Toucher son cul.":
                jump dream_ass_1
            "Lui approcher doucement la bite des lèvres.":
                jump tuto_dream_2    
            "Lui saisir violemment la tête et lui enfoncer la bite dans la gorge.":
                jump max_corruption

        # Selon la réponse il y aura le mini jeu ici DREAMGAMES
        return

    label go_on:
        # Arrivé à la table du petit-déjeuner, Clara, dos à la scène, au niveau de l'évier.
        # mc s'assoit sur la chaise de droite dos à la fenêtre.
        mc "Bonjour Clara !!"
        mc "Comment vas-tu aujourd'hui ??"
        
        return
    
    label dream_tits_1:
        # image de MC lui ouvrant la robe de chambre
        mc_thought "Si je pouvais lui caresser les seins..."

    label dream_ass_1:
        # scene main MC au fesses sous la robe de chambre.
        mc_thought "Si je pouvais lui prendre la fesse et lui mettre une bonne fessée..."

    label tuto_dream_2:
        # MC s'approche doucement des levres de Clara.
        mc_thought "Voilà, tout doucement, tout doucement..."
        mc_thought "je peux sentir son souffle chaud sur ma bite..."
        mc_thought "On va essayer plus prêt."
        menu:
            "Ne rien faire":
                jump go_on
            "Kiss my dick":
                jump kiss_dick
        return
    # DREAMGAMES

    label kiss_dick:
        # Les lèvres s'approchent du penis.
        mc "Kiss my fucking dick !!!"
        mc "....."
    
    
    
    label max_corruption:
        pass
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Affichage de la section suivante : ...
    jump start_day
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


label start_tuto_hunt:
    # Constante pour affichage du menu.
    $ menu_tuto_hunt = False

    show page_test_2 with dissolve
    pause 1.0
    
    no "Voici \"The Hunters Games\"."
    show page_test_3 with dissolve
    no "Le principe est simple : \"Chasser les Montres\"."
    no "Vous êtes le chasseur, ils sont les proies."
    
    # Ecran du GamePlay.
    show screen hunt_Gameplay
    no "Vous avez un total de 6 flèches."
    show screen Arrow_hunt_1

    
    hide screen hunt_Gameplay
    
    # scene screen cavern_fire
    no "Et voilà pour le tuto chasse."

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Affichage de la section suivante : ...
    jump first_choice
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


label start_tuto_mana:
    show page_test_3 with dissolve
    no "L'entraînement à la magie consiste "

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Affichage de la section suivante : ...
    jump start_day
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


