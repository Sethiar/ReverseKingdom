#======================================================#
# Fichier comprenant les variables sur le temps du jeu.
#======================================================#

# Initialisation des variables de temps.
# Commence la journée à 7H

python early:
    def maj_moment_day():
        global daily_moments
        if 6 <= hour < 12:
            daily_moments = "Matin"
        elif 12 <= hour < 18:
            daily_moments = "Après-midi"
        elif 18 <=  daily_moments < 22:
            daily_moments = "Soirée"
        else:
            daily_moments = "Nuit"     

