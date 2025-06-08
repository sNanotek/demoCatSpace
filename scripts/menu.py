import pygame
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.text import Text
from scripts.animatedbg import AnimatedBg
class Menu(Scene):

    def __init__(self):
        super().__init__()
        self.bg = AnimatedBg("assets\MenuSpace.png", [0,0], [1280,0], [self.all_sprites])
        self.title = Text("fonts\Inter\Inter.ttf", 50, "SpaceCat", "white", [540, 200])
        self.pressStart = Text("fonts\Inter\Inter.ttf", 50, "Press Start To Play", "white", [430, 450])

    def events(self, event):
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
         return super().events(event)

    def update(self):

        self.bg.update()
        self.title.draw()
        self.pressStart.drawFade()
        return super().update()
