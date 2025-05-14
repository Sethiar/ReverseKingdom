#=================================================================
# Aller au Village
#=================================================================


# Aller au Village pour la première fois va présenter plusieurs possibilités :

# Rencontrer Isis qui permettra de débloquer le talent intelligence.
# Rencontrer l'aubergiste et sa femme Ingrid. Déblocage du travail en tant que serveur (matin ou après_midi).
# Rencontrer Clara.


label GoToVillage_01:
    # images 10 montrant le village et bg_village01.png -- village09.png
    mc_thought "Enfin le village, je vais ..."
    menu:
        "Aller à l'auberge.":
            call inns
        "Aller au puit." if well_on:
            call well
        "Se promener.":
            call walking_village

    label inns:
        # image : inn_01.png
        # image : inn_02.png
        
        mc_thought "Me voici à l'auberge."
        # image
        mc_thought "Je ne sais pas parler leur langue et je ne connais pas leur coutume."
        mc_thought "La seule chose que je peux faire c'est travailler en plonge."
        # image
        mc_thought "Et je vais devoir me faire comprendre..."

        return 

    label walking_village:
        # Apparition du choix du puit maintenant.
        $ well_on = True
        # images rue indigènes qui marchent. 3x
        mc_thought "C'est très spécial ici."
        # images zooms sur plusieurs visages. 5x
        mc_thought "des Orcs, des Gobelins, des humains, des elfes..."
        # image zoom sur fesses et poitrines. 3x
        mc_thought "et plutôt jolies en plus..." 
        # image elfes masculins qui le surprennent. 2x
        mc_thought "Mais, je vais devoir faire attention, je crois..."
        # image des autres rues, le forgeron, 

        return

    label well:
        # Images du puit avec Isis assise à côté. 5x
        mc_thought "Elle est belle, j'aimerais bien aller la voir..."
        mc_thought "Pour lui dire quoi ???"
        mc_thought "Je ne connais pas sa langue."
        # Iimages de Isis qui voit le mc. 2x
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
        
        
        # fin de la marche dans le village
        return