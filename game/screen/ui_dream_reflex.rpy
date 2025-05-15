# Code concernant le gameplay du jeu. DREAMCLIK"
screen reflex_click(callback, fail):
    timer 1.5 action [Function(renpy.call, fail)]
    imagebutton:
    idle "minigames/dream/gui/object/marker_dream.png"
    action [Function(renpy.call, callback)]
    at random_position()

transform random_position():
    xpos renpy.random.randint(100, 1850)
    ypos renpy.random.randint(50, 1000)  

    
      