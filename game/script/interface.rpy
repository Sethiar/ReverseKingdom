#==================================================#

# Script qui définit l'utilisation de l'interface #

#==================================================#

image cadre_frame = "gui/RK-FrameGame.png"

# introduction à l'interface utilisateur.
# Script qui permet de tester l'interface.
label interface_test:
    scene black with squares
    show screen cadre_frame with pixellate

    no "OK"
    no "bon maintenant l'interaction. Prenons une image."
    
    # Affichage de l'interface avec des boutons
    call screen interface_buttons

    no "Ensuite, on va créer l'interaction."
    no "et on clic !!"

    return
    
    no "Ah, pas mal "


# Script du tutoriel de l'interface utilisateur.
label tuto_interface:
    scene black with squares
    no "Bonjour, je me présente, je m'appelle Nosiris"
    
    # image bg = "no_reverence.png"
    no "Tout d'abord, merci beaucoup de jouer à ce jeu."
    no "J'espère que vous prendrez autant de plaisir à y jouer que j'ai apprécié le développer."

    # image bg = tuto_interface_01
    no "Je me permets d'interrompre le jeu afin de vous expliquer un peu comment fonctionne l'interface."
    
    # image bg = tuto_interface_02
    no "Déjà, on va commencer par rendre le Gameplay plus agréable..."
    no "... enfin, je l'espère..."
    
    
    $ frame_ON =True
    show screen cadre_frame

    # Affichage des îcones sur l'écran.
    show screen interface_buttons
    # Affichage de la flèche.
    no "Pour accéder à l'interface vous devez cliquer sur cet icône."
    show screen arrow_1
    with dissolve
    pause 1
    hide screen arrow_1
    with dissolve

    scene black with squares
    show screen interface_buttons
    
    no "Ensuite, vous avez l'icône des quêtes."
    
    no "Vous accédez ainsi à toutes informations relatives aux quêtes."
    show screen arrow_2
    with dissolve
    pause 1
    hide screen arrow_2
    with dissolve
    
    scene black with squares
    show screen interface_buttons

    no "Et enfin l'icône des relations."
    
    no "Vous accèderez de manière rapide aux informations relatives aux filels du jeu."
    show screen arrow_3
    with dissolve
    pause 1
    hide screen arrow_3
    with dissolve 

    scene black with squares
    show screen interface_buttons

    no "Depuis l'interface du jeu, vous avez accès à différentes sections utiles."

    show RK_Gameplay_Interface
    with dissolve
    pause 0.5

    show screen interface_skills
    with dissolve
    no "L'accès à vos compétences..."
    pause 0.3

    show screen interface_quest
    with dissolve
    no "Aux informations de quêtes..."
    pause 0.3

    show screen interface_rela
    with dissolve
    no "... et des relations."
    pause 0.3

    show screen interface_equip
    with dissolve
    no "Vous pourrez vous équiper ici."
    pause 0.3

    show screen interface_inv
    with dissolve
    no "Et enfin avoir accès à votre inventaire."
    pause 0.5

    # Fin du tuto : tout disparaît
    hide screen interface_skills
    hide screen interface_quest
    hide screen interface_rela
    hide screen interface_equip
    hide screen interface_inv
    hide RK_Gameplay_Interface
    with fade

    scene black with vpunch
    hide RK_Gameplay_Interface
    with fade
    no "Et ho !! Vous dormez ?! Désolé pour la longue introduction mais c'était nécessaire."

    # image no dit aurevoir x5
    no "Vous voici parez pour commencer l'aventure de Reverse Kingdom."
    
    # image bg = tuto_interface_09
    no "Le but du jeu est simple."
    no "Vous devez réussir à augmenter la corruption et l'affection des filles que vous rencontrez."
    no "Cela vous permettra de mieux les connaître ... et de progresser dans l'histoire."
    no "La corruption a aussi un effet sur le personnage que vous incarnez, vos choix définiront votre conduite dans la suite du jeu."
    
    # Image chaleureuse.
    no "Amusez-vous bien."
    
    # image bg = tuto_interface_15
    no "Je vous souhaite une bonne expérience de jeu et à bientôt sur mon Patreon <$lien_patreon>"

    # image bg = tuto_interface_02
    no "Et une nouvelle fois, merci beaucoup."

    # Suite de l'introduction.
    scene white with dissolve
    pause 1.0
    scene page_test_3 with dissolve
    pause 1.0
    jump first_choice
    return
    


    