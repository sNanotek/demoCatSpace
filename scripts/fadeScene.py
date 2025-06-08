import pygame

class Fade:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.surface = pygame.Surface([1280, 720]).convert_alpha()
        self.surface.fill("black")

        self.alpha = 255

    def draw(self, speed):

        if self.alpha > 0:
            self.alpha -= speed

        self.surface.set_alpha(self.alpha)

        self.display.blit(self.surface, [0,0])
