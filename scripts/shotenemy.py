from scripts.obj import Obj

class ShotEnemy(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 7

    def update(self):

        if self.rect.x == 0:
            self.kill()

        self.rect.x -= self.speed

        self.animation(15, 3, "assets\shootEnemy")