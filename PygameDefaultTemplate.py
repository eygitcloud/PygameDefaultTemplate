# Program Pattern

import pygame as pg
from os import environ


if True:
    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (150,40)
    pg.init()

    windowL, windowH = 800, 800
    mainLayer = pg.display.set_mode((windowL, windowH))
    pg.display.set_caption("Default Template")



class ProgramController:
    def __init__(self, _fps):
        self.fpsLimiter, self._fps = pg.time.Clock(), _fps
        self.progTime, self.isRunning = 0, True
        self.mousePosition = pg.mouse.get_pos()

        # Define Program Variables Here


        # End Def


    def MainLoop(self):
        while self.isRunning:
            self.fpsLimiter.tick(self._fps)
            self.progTime += 1
            self.mousePosition = pg.mouse.get_pos()
            self.LB, self.MB, self.RB = pg.mouse.get_pressed()

            # Clear Screen
            mainLayer.fill((40,40,40))

            # Input Check
            self.checkKeyEvents()

            # Implement your activity here



            # End Act


            # Update Screen
            pg.display.flip()

    

    def checkKeyEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.isRunning = False

            if event.type == pg.KEYDOWN:
                pass

if __name__ == "__main__":
    PC = ProgramController(30)
    PC.MainLoop()

pg.quit()