from scripts.obj import Obj as criaImagem
from scripts.shot import Shot
import pygame

class SpaceShip(criaImagem):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.shots = pygame.sprite.Group()

    def input(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.rect.y -= 10
        elif key[pygame.K_s]:
            self.rect.y += 10
        elif key[pygame.K_d]:
            self.rect.x += 10
        elif key[pygame.K_a]:
            self.rect.x -= 10

        if key[pygame.K_w] and key[pygame.K_d]:
            self.rect.y -= 10
            self.rect.x += 10

        elif key[pygame.K_w] and key[pygame.K_a]:
            self.rect.y -= 10
            self.rect.x -= 10

        elif key[pygame.K_s] and key[pygame.K_d]:
            self.rect.y += 10
            self.rect.x += 10

        elif key[pygame.K_s] and key[pygame.K_a]:
            self.rect.y += 10
            self.rect.x -= 10

        if key[pygame.K_SPACE]:
            Shot("assets\shotCat.png", [self.rect.x + 100, self.rect.y + 65], [self.shots])

    def limit(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 1280 - self.image.get_width():
            self.rect.x = 1280 - self.image.get_width()

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y >= 720 - self.image.get_height():
            self.rect.y = 720 - self.image.get_height()


    def update(self):

        self.animation(30, 3, "assets\catSpace")
        self.input()
        self.limit()