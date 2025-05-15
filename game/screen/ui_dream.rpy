# Composantes screen du minijeu DREAMCLIK


screen awake_meter():
    frame:
        align (0.98, 0.5)
        has vbox
        text "Get Up"
        bar value dream_game.awake_meter range 100 xysize (20, 300)

        