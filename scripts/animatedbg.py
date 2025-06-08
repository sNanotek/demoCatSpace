from scripts.obj import Obj as criaImagem

class AnimatedBg:

    def __init__(self, img, pos1, pos2, group):

        self.bg = criaImagem(img, pos1, group)
        self.bg2 = criaImagem(img, pos2, group)
        self.speed = 3

    def update(self):

        self.bg.rect.x -= self.speed
        self.bg2.rect.x -= self.speed


        if self.bg.rect.right <= 0:
            self.bg.rect.left = self.bg2.rect.right

        if self.bg2.rect.right <= 0:
            self.bg2.rect.left = self.bg.rect.right

