#=================================================================
# Aller au Village
#=================================================================



# Première visite village.

#---------------------------------------------------------------------------------
# Aller au Village pour la première fois va présenter plusieurs possibilités :

# Rencontrer Isis qui permettra de débloquer le talent intelligence.
# Rencontrer l'aubergiste et sa femme Ingrid. Déblocage du travail en tant que serveur (matin ou après_midi).
# Rencontrer Clara.

image village1 = "images/PageTest/5.png"

label GoToVillage_01:
    
    # images x10 montrant le village et bg_village01.png -- village09.png
    mc_thought "Où est ce que je suis tombé... ???"
    mc_thought "Ah, voici l'auberge."
    mc_thought "C'est le mieux pour commencer..."
    mc_thought "Enfin, c'est ce que je dirais si je comprenais leur langue et leurs coutumes."
    mc_thought "... avec tous les monstres qu'il y a..."

    mc_thought "je dois réfléchir à une approche."
    
    $ well_on = True
    
    # images rue indigènes qui marchent. 3x
    mc_thought "C'est très spécial ici."
    # images zooms sur plusieurs visages. 5x
    mc_thought "des Orcs, des Gobelins, des humains, des elfes..."
    # image zoom sur fesses et poitrines. 3x
    mc_thought "et plutôt jolies en plus..." 
    # image elfes masculins qui le surprennent. 2x
    mc_thought "Mais, je vais devoir faire attention, je crois..."
    

    # scene screen puit_01.png with dissolve
    mc_thought "Je vais m'arrêter là un instant."
    mc_thought "Ah, je ne suis pas tout seul"
    
    # Images du puit avec Isis assise à côté. 5x
    mc_thought "Elle est belle, j'aimerais bien aller la voir..."
    mc_thought "Pour lui dire quoi ???"
    mc_thought "Je ne connais pas sa langue."
    # Images de Isis qui voit le mc. 2x
    mc_thought "Merd..."
    # Images de Isis qui approche.x3
    mc_thought "Elle approche..."
    mc_thought "Encore plus belle.."
        
    # image : Isis qui parle x2
    isi "è'éfx -5ç(_-8()= !!!"
    isi "hçsàç(o' ??"
    isi "rtà ç-ç7é =)=4 ??"

    # images du mc qui ne comprend pas grand chose.
    mc_thought "Je vais essayer de lui faire comprendre que je suis sourd et muet."
    mc_thought "Ça peut marcher"

    # images du mc qui s'exécute. 5x.
    isi "é&8è çàé5 !!"

    # Elle mime une bouche et une oreille barées.
    mc_thought "Elle a l'air d'avoir saisi l'idée."
    mc_thought "Elle peut peut-être m'aider."

    # Image de MC qui mime une marche avec Isis.
    mc_thought "Elle pourra me faire visiter et m'avertir de choses qui peuvent arriver."
    # Isis réfléchit longuement.
    # regarde de la tête aux pieds.
    # Hésite.
    # isis tête montrant la rue du village. 
    isi "&àéç_'  ç(_'è! ??"
    isi "ç(_ pà) !"
    mc_thought "Elle sourit elle a l'air d'accord."
    
    # Balade dans le village.
    # scene screen forge_01 with dissolve
    isi "ççè àç çèç_() !!"
    mc_thought "Voici donc la forge."
    # Isis réfléchit en regardant la forge.
    # Isis regarde le mc. Haut en bas.
    # Reagrde la forge et pars dans sa direction.
    isi "'__ )à= !"
    mc_thought "Où va t-elle ?"

    # scene isis et forgeron discussion.
    mc_thought "Elle le connaît."
    mc_thought "Ils me regardent..."
    mc_thought "..."
    mc_thought "Elle revient..."
    mc_thought "Elle a l'air ennuyée.."

    isi "çuà& _-ç_à, &çè'-) àçè  =çà."
    isi "_', à_"
    
    # Isis faisant voir à MC de l'argent, la forge et la bouche pour manger.
    mc_thought "Elle veut m'aider à trouver de l'argent pour manger."
    mc_thought "Comme on dit : \"Apprend lui à pêcher et tu le nourriras pour l'éternité.\""
    
    # Changement de direction.
    # Image Isis conoseille MC sur Orc et gobelins et autres.
    # image d'instant de promenade à deux et en regardant les différents endroits.
    # Parfois elle discute avec un commerçant et reviens ennuyée.

    mc_thought "Quelle marche, j'ai soif et je ne peux même pas lui offrir à boire."
    mc_thought "Elle est pleine d'énerie et de tendresse."
    mc_thought "Et en plus elle est belle."

    # Image Isisbreast.
    mc_thought "Hum ... !!"
    mc_thought "Qu'est-ce que ... !!"

    mc_thought "Je vois son sein."
    mc_thought "Waah .."

    # premier choix corruption du MC
    call menu_intro_isis_01
    
    call pre_corruption
    
label GotoVillage_02:
    # Isis montre sa bouche et l'auberge.
    isi "'_' à&)à =&5è ?!"
    mc_thought "Oh oui, je meurs de soif."

    # Installation à une table à l'auberge.
    isi "é)5éà éà)àé !!"
    vf "àç5é6&5'5 55è5 ??"
    
    # Isis et la serveuse regardent le mc.
    isi "é)&à) =&)à !"
    vf "à&_& 5 47) !!!"
    vf "ç() )àç)  )à."

    # isis regarde le MC. 
    # Le MC montre ses oreilles et sa bouche. Sourd et muet.

    # Image de Ingrid de pitié et d'empathie.
    # Elle parle avec Isis et Isis sourit et saute au coup d'Ingrid.
    # Isis regarde le MC.
    isi "ç_ à&_àè àéèçà. !!"
    mc_thought "Si j'ai bien compris, elle vient de me trouver un trvaail à l'auberge..."
    mc_thought "Super !!"
    mc_thought "Je devrais lui faire comprendre que j'ai saisi pour le traval."
    
    # Ecran qui explqiuent la situation
    
    isi "àçàç _çà_ )àç==."
    # LE MC la prend dans les mains et la remercie. ELle rougit du contact.
    # Situaton un peu génante, mais elle a accepté
    # Affection Isis + 2.

    mc_thought "Je crois que cela s'est bien passé."
    mc_thought "Je vais la remercier."
    # Le MC met la met sur son coeur est baisse la tete devant ISis.
    # Signe d'affection et de respect.
    
    # Isis sourit et dit au revoir à Ingrid.

    # MC reste avec Ingrid.
    # Cuisine de l'auberge, toilettes, écurie, tables...
    # Images de travail et de repas. Seul. Dan sun coin de la cuisine.
    mc_thought "Et ben..."
    mc_thought "Je me demande qui faisait cela avant..."
    mc_thought "Bon donc je peux venir travailler les après midi."
    mc_thought "Très bien. J'ai un repas gratuit et 15 pièces."
    mc_thought "Il est tant de rentrer."

    # InnF sourit et InnH fait la gueule.
    innF "éç_57 çà_ _)à_)àç."
    innM "àç 44à." # (Au moins Grokk, on ne le nourrisait pas..)
    # Fusille so mari des yeux.
    innF "ç àà& & )."
    # Mc Salue.
    mc_thought "Elle est très belle aussi. Et cette paire de fesses..."
    # Mc part, nuit tombe sur le village.
    mc_thought "Bon rentrons."

    # MC s'aperçoit que quelqu'un le suit.
    # il parvient à le semer dans le village.
    # Il rentre à la caverne, il ne ressent plus de suiveurs.
    mc_thought "Quelle journée !!"

    # Image mc devant le feu à la Caverne.
    # Après cette grosse journée. Le MC va se coucher. 
    jump start_tuto_dream

    return
