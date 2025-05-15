# Logique du code du minijeu dream.

init python:
    class DreamGame:
        def __init__(self):
            self.awake_meter = 0
            self.magic = 0
            self.intelligence = 0
            self.progress = 0

        def reset(self):
            self.awake_meter = 0
            self.progress = 0

        def add_awake(self, base_value):
            reduction = (self.magic*0.3 + self.intelligence+0.2)
            self.awake_meter += max(1, base_value-reduction)
            if self.awake_meter >= 100:
                renpy.jump("dream_end")
                
                  
