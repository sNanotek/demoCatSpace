from scripts.obj import Obj as criaImagem
import random

class Meteoro(criaImagem):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

    def update(self):
        self.rect.y += 10

        if self.rect.y >= 1280:
            self.kill()
