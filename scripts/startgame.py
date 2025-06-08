import pygame, sys
from scripts.menu import Menu
from scripts.game import Game
from scripts.gameover import GameOver
from scripts.settings import *
from scripts.fadeScene import Fade

class StartGame:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.fps = pygame.time.Clock()
        self.display = pygame.display.set_mode([WIDTH,HEIGHT])
        pygame.display.set_caption("SpaceCat")
        self.scene = "menu"
        self.current_scene = Menu()
        self.fade = Fade()

    def run(self):

        while True:

            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"

                self.current_scene = Game()
            elif self.scene == "game" and self.current_scene.active == False:
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.current_scene.events(event)

            self.display.fill("black")
            self.current_scene.draw()
            self.fade.draw(2)
            self.current_scene.update()
            self.fps.tick(60)
            pygame.display.flip()
