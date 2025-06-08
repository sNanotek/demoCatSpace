import pygame

class Obj(pygame.sprite.Sprite):

    def __init__(self, img, pos, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft = pos)

        self.tick = 0
        self.contadorImagem = 0

    def animation(self, speed, n_img, path):
        self.tick += 2

        if self.tick > speed:
            self.tick = 0
            self.contadorImagem = ( self.contadorImagem + 1 ) % n_img
            self.image = pygame.image.load(path + str(self.contadorImagem) + ".png")