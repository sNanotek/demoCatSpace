import pygame
import random
from scripts.scene import Scene
from scripts.animatedbg import AnimatedBg
from scripts.spaceshipboss import SpaceShipBoss
from scripts.spaceship import SpaceShip
from scripts.meteoro import Meteoro
from scripts.obj import Obj as criaImagem
class Game(Scene):

    def __init__(self):
        super().__init__()

        self.number = random.randint(10, 800)
        self.contador = 0
        self.bg = AnimatedBg("assets\gameBg.png", [0,0], [1280,0], [self.all_sprites])
        self.catSpace = SpaceShip("assets\catSpace0.png", [30, 600], [self.all_sprites])
        self.enemyBoss = SpaceShipBoss("assets\catbossSpaceTest0.png", [920, 250], [self.all_sprites])
        self.meteoro = Meteoro("assets\meteoro.png", [self.number, -10], [self.all_sprites])
        self.soundGame = pygame.mixer.Sound("sounds\soundGame.mp3")
        self.vida = criaImagem("assets\kvida.png", [40, 30], [self.all_sprites])
        self.vida2 = criaImagem("assets\kvida.png", [90, 30], [self.all_sprites])
        self.vida3 = criaImagem("assets\kvida.png", [140, 30], [self.all_sprites])
        self.controle = 1

    def events(self, event):

        if self.active is not False and self.controle is not 0:
            self.soundGame.play(loops=-1)
            self.soundGame.set_volume(0.15)
            self.controle = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.soundGame.stop()
                self.active = False

    def update(self):

        self.contador += 1

        self.number = random.randint(10, 800)

        if self.contador == 150:
            self.meteoro = Meteoro("assets\meteoro.png", [self.number, -80], [self.all_sprites])
            self.contador = 0
        if self.meteoro.rect.y >= 650:
            self.meteoro.kill()

        self.meteoro.update()
        self.catSpace.shots.draw(self.display)
        self.catSpace.shots.update()
        self.enemyBoss.update(self.catSpace.shots)
        self.enemyBoss.shot.draw(self.display)
        self.enemyBoss.shot.update()
        self.catSpace.update()
        self.bg.update()
