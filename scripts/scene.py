import pygame
from scripts.obj import Obj

class Scene:

    def __init__(self):
        pygame.display.set_caption("SpaceCat")
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.active = True

    def events(self, event):
        pass

    def draw(self):
        self.all_sprites.draw(self.display)

    def update(self):
        self.all_sprites.update()
