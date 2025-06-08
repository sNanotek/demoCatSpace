from scripts.obj import Obj as criaImagem

class Shot(criaImagem):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 40

    def update(self):

        if self.rect.x > 1280:
            self.kill()

        self.rect.x += self.speed