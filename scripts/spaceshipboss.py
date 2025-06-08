from scripts.obj import Obj as criaImagem
import pygame
import random
from scripts.shotenemy import ShotEnemy

class SpaceShipBoss(criaImagem):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        self.number = random.choice([3, -3])
        self.speed = self.number
        self.shot = pygame.sprite.Group()

        self.contador = 0
        self.contador2 = 0

    def update(self, shot):

        self.contador += 1
        self.contador2 += 1

        if self.contador == 36:
            ShotEnemy("assets\shootEnemy0.png", [900, self.rect.y + 100], [self.shot])
            self.contador = 0

        if self.rect.y == -50:
            self.speed = 3
        if self.rect.y == 400:
            self.speed = -3

        if self.contador2 == 150:
            self.number = random.choice([3, -3])
            self.speed = self.number
            self.contador2 = 0


        self.rect.y += self.speed

        self.animation(27, 3, "assets\catbossSpaceTest")
