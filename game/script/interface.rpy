#==================================================#

# Script qui définit l'utilisation de l'interface #

#==================================================#
image bg pagetest_1 = "images/PageTest/1.png"
image bg pagetest_2 = "images/PageTest/2.png"



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
    # image bg = "tuto_interface.png"
    no "Bonjour, je me présente Nosiris"
    # image bg = "no_reverence.png"
    no "Tout d'abord, merci beaucoup de jouer à ce jeu."
    no "J'espère que vous prendrez autant de plaisir à y jouer que j'ai apprécié le développer."

    # image bg = tuto_interface_01
    no "Je me permets d'interrompre le jeu afin de vous expliquer un peu comment fonctionne l'interface."
    # image bg = tuto_interface_02
    no "Pour accéder à l'interface vous devez cliquer sur cet icône."
    
    call interface_menu
            
    call interface_skills
    # image bg = tuto_interface_04
    no "... L'écran des compétences ..."
            
    call interface_quest
    # image bg = tuto_interface_05
    no "... L'écran des quêtes ..."
            
    call interface_equip
    # image bg = tuto_interface_06
    no "... L'écran des équipements ..."
            
    call interface_inv
    # image bg = tuto_interface_07
    no "... L'écran de l'inventaire ..."
            
    call interface_rela
    # image bg = tuto_interface_08
    no "... Et enfin le plus important, l'écran des relations ..."

    # image bg = tuto_interface_09
    no "Le but du jeu est simple."
    no "Vous devez réussir à augmenter la corruption et l'affection pour les filles que vous rencontrez."
    no "Cela vous permettra de mieux les connaître ... et de progresser dans l'histoire."

    # image bg = tuto_interface_10
    no "Pour cela, vous devez augmenter le niveau de vos compétences."

    # image bg = tuto_interface_11
    no "Suivre l'avancement et les informations données concernant les quêtes."

    # image bg = tuto_interface_12
    no "vous pourrez vous équiper d'objets ici."

    # image bg = tuto_interface_13
    no "Vous pourrez stocker toutes sortes de choses dans cet inventaire."

    # image bg = tuto_interface_14
    no "Et vous pourrez suivre chaque évolution avec vos relations à cet endroit."

    # image bg = tuto_interface_15
    no "Je vous souhaite une bonne expérience de jeu et à bientôt sur mon Patreon <$lien_patreon>"

    # image bg = tuto_interface_02
    no "Et une nouvelle fois, merci beaucoup."

    return

    "Présentation du choix du tutoriel."
    mc_thought "Je vais..."

    
    # Présentation du choix du tutoriel.
    jump first_choice

