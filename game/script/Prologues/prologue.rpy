
#==========================================================
# Prologue de Reverse Kingdom
#==========================================================


#  fichier informations du prologue.

label prologue:
    
    # scène apparaît avec une image de fond floutée et progressivement nette.
    
    # Scène dans espace avec étoiles et galaxies autour déformées par un trou noir.
    # MC sous forme de losange bleuté violeté flottant dans le vide.
    
    # image bg = "blackhole_01.png"
    temp_mc "Où suis-je ? Je ne sens rien."
    temp_mc "Je ne vois rien non plus."
    temp_mc "Je suis dans le noir total."
    
    # Image nette de la scène.
    # image bg = "scene_intro_blackhole_1.png" (blackhole)
    temp_mc "Je ne peux pas bouger."
    temp_mc "Je ne peux pas parler."
    
    # image bg = "scene_intro_blackhole_2.png" (blackhole)
    temp_mc "Je peux seulement penser."
    
    # image bg = "scene_intro_blackhole_3.png" (blackhole)
    temp_mc "Je ne sais pas combien de temps ça fait que je suis ici."
    
    #==================================================================
    # Scène du souvenir
    #==================================================================
    
    
    # Transition vers une scène de lumière.
    temp_mc "Essaie de réfléchir et de te souvenir de ce qui s'est passé avant."
    # image bg = "scene_intro_remember_1.png" (autoroute)
    temp_mc "J'étais en train de rouler sur l'autoroute..."
    # image bg = "scene_intro_remember_2.png" (lumière dans ciel)
    temp_mc "Je me souviens d'avoir vu une lumière au loin..."
    # image bg = "scene_intro_remember_3.png" (accident)
    temp_mc "Je me souviens d'avoir perdu le contrôle de ma voiture..."
    # image bg = "scene_intro_remember_4.png" (accident)
    temp_mc "Je me souviens d'avoir eu un accident..."
    # image bg = "scene_intro_remember_5.png" (accident)
    temp_mc "Je me souviens d'être tombé dans le précipice..."
    # image bg = "scene_intro_remember_6.png" (chute)
    temp_mc "Je me souviens avoir vu la lumière venir à ma rencontre lorsque je tombais..."
    # image bg = "scene_intro_remember_7.png" (chute lumière)
    # Effet de l'image qui s'estompe. Noir
    temp_mc "Et, j'ai perdu connaissance..."
    
    #===================================================================
    # Fin de la scène du souvenir
    #===================================================================
    
    #---------------------------------------------------------------------------------
    
    #==================================================================
    # Scène de la voix
    #==================================================================
    
    # image bg = "scene_intro_blackhole_1.png" (blackhole)
    temp_mc "Et maintenant je suis là, en train de flotter..."
    temp_mc "Je ne sais pas où je suis..."
    
    # image bg = "scene_intro_blackhole_2.png" (blackhole)
    temp_mc "Je ne sais pas ce qui m'est arrivé..."
    temp_mc "Je ne sais pas si je suis mort ou vivant..."
    
    # Vox se fait entendre pour la première fois.
    # image bg = "scene_intro_vox_1.png"
    vo "Ténèbres, peur, angoisse, frustation..."
    
    # Surprise et choc de l'écran.
    temp_mc "!!!!"
    
    # Perspective du temp_mc et appartition d'une lumière au loin.
    # image bg = "scene_intro_vox_2.png" (lumière)
    temp_mc "...Une voix résonne en moi..."
    
    # Au fur et à mesure que la voix parle, le plan se rapproche de la lumière.
    # image bg = "scene_intro_vox_3.png" (lumière)
    temp_mc "Qui êtes-vous ?"
    temp_mc "Que voulez-vous ?"
    
    # image bg = "scene_intro_vox_4.png" (lumière)
    temp_mc "Où suis-je ?"
    temp_mc "Aidez-moi !!!!"
    
    #-------------------------------------------------------------------
    # Zoom vers le temple.
    #-------------------------------------------------------------------
    
    # On commence à distinguer un autel au loin dans la lumière.
    # image bg = "scene_intro_vox_5.png" (lumière)
    vo "Calme-toi..."
    vo "Tu es en sécurité ici..."
    
    # On s'approche d'un autel avec colonnes séparées par des panneaux de lumière.
    
    # image bg = "scene_intro_vox_6.png" (lumière)
    vo "Tu es dans un endroit où le temps n'existe pas..."
    
    # image bg = "scene_intro_vox_7.png" (lumière)
    vo "Tu es dans un endroit où la lumière et l'obscurité se rencontrent..."
    # image bg = "scene_intro_vox_8.png" (lumière)
    vo "Tu es dans un endroit où les âmes se rencontrent..."
    # image bg = "scene_intro_vox_9.png" (lumière)
    vo "Tu es dans un endroit où les souvenirs se mélangent..."
    # image bg = "scene_intro_vox_10.png" (lumière)
    vo "Tu es dans un endroit où les rêves se réalisent..."
    
    # Nous sommes arrivés au centre de l'autel.
    
    #-------------------------------------------------------------------
    # fin du zoom.
    #-------------------------------------------------------------------
    
    # image bg = "scene_intro_vox_11.png" (lumière)
    vo "Tu es dans un endroit où les désirs se réalisent..."
    vo "Mais tu es aussi dans un endroit où les cauchemars se réalisent..."
    
    # image bg = "scene_intro_vox_12.png" (lumière)
    vo "et où les pensées se matérialisent..."
    vo "Si tu ne fais pas attention ton âme va se perdre..."
    vo "et tu ne pourras jamais revenir..."
    
    # Le temp_mc revient dans le champ.
    # image bg = "scene_intro_vox_13.png" (lumière)
    temp_mc "Mais qui êtes-vous ?"
    temp_mc "Que voulez-vous ?"
    
    # Mc regarde les panneaux de lumière.
    # image bg = "scene_intro_vox_14.png" (lumière)
    vo "Je suis une voix..."
    vo "C'est la seule chose que tu dois savoir sur moi..."
    
    # Plan plus large vue au dessus de l'autel
    vo "Je suis ici pour te guider..."
    vo "Mais je ne suis pas responsable du chemin que tu vas prendre..."
    vo "C'est à toi de choisir..."
    
    # Retour au plan du temp_mc.
    # image bg = "scene_intro_vox_15.png" (lumière)
    temp_mc "Hein....!!!!"
    temp_mc "Je comprends rien..."
    # Choc de l'écran.
    temp_mc "Je veux retourner d'où je viens...!!!"
    # Choc de l'écran.
    temp_mc "Je veux rentrer chez moi...!!!"
    # Choc de l'écran.
    temp_mc "Je veux retrouver ma vie...!!!"
    
    # Vue depuis la table de l'autel. Vers le haut des colonnes.
    # image bg = "scene_intro_autel_1.png"
    vo "Tu ne peux pas..."
    vo "Tu es ici pour une raison..."
    vo "Si tu voulais véritablement partir, tu ne serais pas ici en train de flotter..."
    
    # Plan à déterminer.
    # image bg = "scene_intro_autel_2.png"
    vo "Cet endroit réalise tes désirs les plus enfouis..."
    vo "Tu es ici parce que tu as un désir..."
    
    # image bg = "scene_intro_autel_3.png"
    vo "Réfléchis bien..."
    vo "Quel est ton désir ?"
    
    # Retour au plan du temp_mc.
    # image bg = "scene_intro_autel_4.png" 
    temp_mc "Je ne sais pas, je veux juste rentrer chez moi..."
    temp_mc "Je ne veux pas mourir..."
    
    # Image vers le haut des colonnes.
    vo "Tu ne peux pas mourir..."
    
    # Image la table de l'autel
    # image bg = "scene_intro_autel_5.png" la table brille et le corps du temp_mc apparaît ne transparence sur la table.
    vo "Une partie de toi et déjà morte..."
    # image bg = "scene_intro_autel_6.png" (autel)
    vo "Celle qui est morte, c'est ton corps dans ton ancien monde..."
    # image bg = "scene_intro_autel_7.png" (autel)
    
    # image bg = "scene_intro_autel_8.png" (losange commence à briller.)
    vo "Mais ton âme, elle, est toujours vivante..."
    # image bg = "scene_intro_autel_9.png" (losange brille de plus en plus.)
    vo "Et elle est ici, dans cet endroit..."
    vo "Cet endroit est un monde intermédiaire..."
    
    # image bg = "scene_intro_autel_10.png" (losange brille.)
    vo "Un monde entre la vie et la mort..."
    vo "Un monde entre le rêve et la réalité..."
    vo "Un monde entre l'obscurité et la lumière..."
    
    # le losange se transforme en un corps humain.
    # image bg = "scene_intro_autel_11.png" (losange corps humain bleutée.)
    vo "Un monde où tu peux choisir ton nouveau destin..."
    # image bg = "scene_intro_autel_12.png" (losange corps humain bleutée.)
    vo "Un monde où tu peux choisir ta nouvelle vie..."
    # image bg = "scene_intro_autel_13.png" (losange corps humain bleutée.)
    vo "Un monde où tu peux choisir ton nouveau corps..."
    
    # Pose temp_mc regardant ces bras. Couleur de peau bleutée. effet transparence/Fantôme..)
    temp_mc "Un nouveau corps ?"
    temp_mc "Mais qu'est-ce que c'est que cette histoire de merde ?"
    
    # Couleur MC passe à l'orange/rouge.
    # image bg = "scene_intro_autel_14.png" (losange corps humain rouge.)
    temp_mc "Je ne veux pas d'un nouveau corps..."
    temp_mc "Je veux juste rentrer chez moi..."
    
    # image bg = "scene_intro_autel_15.png" (Vers le haut de l'autel.)
    vo "Mais pour cela, tu dois m'offrir quelque chose..."
    vo "Quelque chose de précieux..."
    
    # Se rapproche du MC
    # image bg = "scene_intro_autel_16.png" (vers le bas de l'autel.)
    vo "Quelque chose de cher à ton cœur..."
    
    # image bg = "scene_intro_autel_17.png" losange corps humain jaune.)
    temp_mc "Mais je n'ai rien à t'offrir..."
    temp_mc "...!!!"
    
    # Choc de l'écran
    temp_mc "Tu vas prendre mon âme !!!!!"
    # Choc de l'écran
    temp_mc "C'est ça ?"
    # Choc de l'écran
    temp_mc "Tu veux mon âme ?"
    
    # Temps de pause avec soupirement de la voix.
    
    # Image bg = "scene_intro_autel_18.png" (vers le haut de l'autel.)
    vo " ...\"(soupir)\"..."
    vo "..." 
    # image bg = "scene_intro_autel_19.png" (vers le bas de l'autel.)
    vo "Non, je ne veux pas ton âme..."
    
    # Plan sur le temp_mc. couleur du losange bleutée verte.
    # image bg = "scene_intro_autel_20.png" (vers le bas de l'autel.)
    vo "Je veux juste un peu de ta lumière..."
    vo "...Un peu de ta lumière..."
    vo "...Un peu de ta lumière pour réchauffer mon coeur et mon ennui..."
    
    # Différents plan du temp_mc.
    # image bg = "scene_intro_autel_21.png" (plan du temp_mc.)
    temp_mc "Mais qu'est-ce que tu veux dire par là ?"
    # image bg = "scene_intro_autel_22.png" (plan du temp_mc.)
    temp_mc "Je ne comprends pas..." 
    # image bg = "scene_intro_autel_23.png" (plan du temp_mc.)
    temp_mc "Je ne comprends rien..."
    temp_mc "..."
    temp_mc "Ça va faire mal ?"
    # image bg = "scene_intro_autel_24.png" (plan du temp_mc.)
    temp_mc "Je vais souffrir ?"
    
    # image bg = "scene_intro_autel_25.png" (plan du temp_mc.)
    vo "Ça dépend de toi..."
    
    # Choc de l'écran.
    temp_mc "Hein !!!"
    
    #====================================================================
    # Fin de la scène de la voix.
    #====================================================================
    
    #--------------------------------------------------------------------
    
    #====================================================================
    # Apparition de Vox.
    #====================================================================
    
    # Vox va apparaître sur l'autel. dans une pose de déesse effet transition transparence avec effet de lumière.
    # image bg = "scene_intro_autel_?.png" (plan de l'autel.)
    vo "Es tu prêt à me faire cadeau de ce que tu as de plus précieux ?"
    
    # image bg = "scene_intro_vox_body_1.png" (plan de l'autel.)
    vo "Es-tu prêt à me faire cadeau de ta lumière ?"
    # image bg = "scene_intro_vox_body_2.png" (plan de l'autel.)
    
    # Vox apparaît complètement habillée avec une robe blanche et des cheveux longs et brillants.
    
    # image bg = "scene_intro_vox_body_3.png" (plan de l'autel.)
    
    # Le temp_mc se parle en lui-même.
    temp_mc "Qu'est ce qu'elle est belle..."
    temp_mc "..."
    temp_mc "De toute façon, je n'ai pas le choix..."
    # image bg = "scene_intro_vox_mc_1.png" (plan de l'autel.)
    temp_mc "Je suis coincé ici..."
    temp_mc "Oui, et fais cela vite que l'on en finisse..."
    
    # Plan de Vox.
    # image bg = "scene_intro_vox_body_4.png" (plan de l'autel.)
    vo "Je vais te commencer par te poser quelques questions..."
    
    #---------------------------------------------------------------------
    
    #=====================================================================
    # Choix de l'âge.
    #=====================================================================
    
    # Choix pour mentions légales, si non arrêt du jeu.
    vo "As tu plus de 18 ans,  c'est absolument nécessaire pour continuer l'aventure avec moi ?"
    
    menu:
        "Oui":
            $ age = True
        "Non":
            $ age = False
    if age:
        vo "Bien, tu es majeur..."
    
    else:
        vo "Désolé, tu n'es pas majeur..."
        vo "Tu ne peux pas rester ici..."
        vo "Tu dois partir..."
        vo "Tu dois retourner dans ton ancien monde..."
        vo "Tu dois retourner dans ton ancien corps..."
        vo "Tu vas être tétraplégique toute ta vie, mais au moins tu seras vivant..."
        vo "Adieu..."
        
        temp_mc "Non, non, nooooooooooooooooooooooooooooooooooooooooooooooooooooooooon...!!!" 
        
        $ renpy.quit() # Arrêt complet du jeu.
        
    #======================================================================
    # Fin de la scène du choix de l'âge.
    #======================================================================
    
    #---------------------------------------------------------------------
    
    #=====================================================================
    # Scène du choix du prénom.
    #=====================================================================
    
    # Plan de discussion après validation de l'âge.
    # image bg = "scene_intro_vox_mc_2.png" (plan de l'autel.)
    temp_mc "Je suis majeur..., et... donc... ?"
    
    # image bg = "scene_intro_vox_mc_3.png" (plan de l'autel.)
    vo "Quel est ton prénom ?"
    
    # Saisie du prénom par le joueur.
    $ player_name = renpy.input("Quel est ton prénom ?", length=20)
    $ player_name = player_name.strip()
    if player_name =="":
        $ player_name = "John-Doe"
        
    # image bg = "scene_intro_vox_mc_4.png" (plan de l'autel.)
    vo "Merci, tu t'appelles donc [player_name]."
    
    #======================================================================
    # Fin de la scène du choix du prénom.
    #======================================================================
    
    #---------------------------------------------------------------------
    
    # Visages de plus en plus proches.
    # image bg = "scene_intro_vox_mc_5.png" (plan de l'autel.)
    vo "[player_name], voici ce que je veux que tu me donnes..."
    
    # Plan des mains sur le visage du mc.
    # image bg = "scene_intro_vox_mc_6.png" (plan de l'autel.)
    vo "Je veux ta virginité..."
    
    # Choc de l'écran.
    mc "!!!"
    mc "Hein !! Quoi !!"
    # Choc de l'écran.
    mc "Ma virginité ?"
    mc "..."
    mc "Mais je ne suis plus vierge..."
    
    # Vox rigole et se retourne vers l'autel.
    # image bg = "scene_intro_vox_mc_7.png" (plan de l'autel.)
    vo "Je sais, pour ce qui concerne ton corps..."
    # image bg = "scene_intro_vox_mc_8.png" (vox de dos en face du mc.)
    vo "..."
    # image bg = "scene_intro_vox_mc_9.png" (vox retourne sa tête vers le mc.)
    vo "Mais je veux la virginité de ton âme..."
    
    # image bg = "scene_intro_vox_mc_10.png" (vox émet de la lumière rouge et noire
    mc "Je ne suis plus si sûre de vouloir te donner ma lumière..."
    
    # image bg = "scene_intro_vox_mc_11.png" (vox lévite et aspire quelque chose du corps du mc.)
    vo "Trop tard, le rituel est achevé."
    vo "Maintenant, ta pureté est à moi..."
    
    # MC s'envole et se fait aspirer par la lumière de Vox.
    # image bg = "scene_intro_vox_mc_12.png" (vox et mc lévitent et aspire quelque chose du corps du mc.)
    mc "Noooooooooooooooooooooooooon !!!!!!!!!"
    mc_thought "NON !!! JE NE VEUX PAS !!!!!!!!!!!!"
    
    # image bg = "scene_intro_vox_mc_13.png" (vox en train de voler projette sa têt en arrière en signe de victoire.)
    vo "HA HA HA HA HA HA !!!!!!!!!!!!"
    # image bg = "scene_intro_vox_mc_14.png" (vox en train de voler en regardant le pouvoir venir à elle. Plan à définir)
    vo "Ta pureté est à moi maintenant..."
    # Effet de l'écran qui s'estombe des yeux du mc
    mc_thought "Je ne veux p..."
    
    # --------------------------------------------------------------------
    # Scène de la mort du MC.
    #---------------------------------------------------------------------
    
    # image bg = "scene_intro_vox_mc_15.png" (mc les bras ballants en train de léviter
    #  MC se parle à lui-même.
    mc_thought "Je perds connaissance..."
    mc_thought "C'est donc ainsi que tout se termine..."
    # image bg = "scene_intro_vox_mc_16.png" (mc les bras ballants en train de léviter zoom sur le visage.)
    mc_thought"Voici donc l'instant où je meurs..."
    
    # La scène est vue par les yeux du MC
    
    # image bg = "scene_intro_vox_mc_17.png" (effet de transition pour mc qui perd connaissance.)
    
    # Retour sur vox avec les yeux du MC
    
    # image bg = "scene_intro_vox_mc_18.png" (vox en train de léviter et de sourire.)
    vo "HA HA HA... ..."
    # Choc de l'écran.
    # Zoom sur visage vox surprise.
    # image bg = "scene_intro_vox_mc_19.png" (vox en train de léviter surprise.)
    vo "Mais !!! Qu'est-ce que ... !!!!"
    vo "C'es quoi ça ????"
    
    # image bg = "scene_intro_vox_mc_20.png" (vox en train de léviter et cris et douleurs.)
    vo "Ce n'est pas possible ..."
    
    # image bg = "scene_intro_vox_mc_21.png" (vox en train de léviter et cris et douleurs.)
    vo "Haaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhh !!!!!!!!!!!"
    
    # Transition image s'estompe par les yeux du MC qui se ferment.
    # image bg = "scene_intro_vox_mc_22.png" (image de fin de la scène.)

    #=====================================================================
    #=====================================================================
    # Fin du prologue du jeu
    #=====================================================================
    #=====================================================================
    
    #_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-



    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Affichage de la section suivante : introduction au jeu
    jump start_intro
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    