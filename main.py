import pygame, sys, os
from scripts.startgame import StartGame


dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

if __name__ == "__main__":
    game = StartGame()
    game.run()
