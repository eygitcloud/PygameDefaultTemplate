# Program Pattern

import pygame as py
from os import environ


if True:
    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (150,40)
    py.init()

    windowL, windowH = 800, 800
    mainLayer = py.display.set_mode((windowL, windowH))
    py.display.set_caption("Default Template")



class ProgramController:
    def __init__(self, _fps):
        self.fpsLimiter, self._fps = py.time.Clock(), _fps
        self.progTime, self.isRunning = 0, True
        self.mousePosition = py.mouse.get_pos()

        # Define Program Variables Here


        # End Def


    def MainLoop(self):
        while self.isRunning:
            self.fpsLimiter.tick(self._fps)
            self.progTime += 1
            self.mousePosition = py.mouse.get_pos()
            self.LB, self.MB, self.RB = py.mouse.get_pressed()

            # Clear Screen
            mainLayer.fill((40,40,40))

            # Input Check
            self.checkKeyEvents()

            # Implement your activity here



            # End Act


            # Update Screen
            py.display.flip()

    

    def checkKeyEvents(self):
        for event in py.event.get():            
            if event.type == py.QUIT:
                self.isRunning = False

            if event.type == py.KEYDOWN:                
                pass

if __name__ == "__main__":
    PC = ProgramController(30)
    PC.MainLoop()

py.quit()