#==================================================#

# Script qui définit l'utilisation de l'interface #

#==================================================#

image cadre_frame = "gui/RK-FrameGame.png"




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

label test_anim:
    scene black
    show tuto_marker_anim at truecenter
    "Est-ce que l'animation clignote ?"
    return


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
    show screen tuto_mark(pos_y=160)
    no "Pour accéder à l'interface vous devez cliquer sur cet icône."
    
    no "Nous êtes sur le menu principal de l'interface."
    

    scene black with squares
    show screen interface_buttons
    
    no "Ensuite, vous avez l'icône des quêtes."
    show screen tuto_mark(pos_y=260)
    no "Vous accédez ainsi à toutes informations relatives aux quêtes."

    scene black with squares
    show screen interface_buttons

    no "Et enfin l'icône des relations."
    show screen tuto_mark(pos_y=360)
    no "Vous accèderez de manière rapide aux informations relatives aux filels du jeu."
    
    scene black with squares
    show screen interface_buttons

    no "Depuis l'interface du jeu, vous avez..."
    show RK_Gameplay_Interface 
    
    show screen interface_skills
    no "L'accès à vos compétences..."
    no "Aux informations de quêtes et des relations."

    show screen interface_equip
    no "Vous pourrez vous équiper ici."

    show screen interface_inv
    no "Et enfin avoir accès à votre inventaire."

    scene black with vpunch
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


    "Présentation du choix du tutoriel."
    mc_thought "Je vais..."

    # Présentation du choix du tutoriel.
    jump first_choice
    return
    


    