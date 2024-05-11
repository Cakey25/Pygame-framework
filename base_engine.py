

import sys
import pygame as pg
import moderngl as mgl

from hypermodernGL import *
from config import *


class Engine:
    def __init__(self):
        pg.init()

        # Create window
        self.screen = pg.display.set_mode(WINDOWSIZE)

        # Setup variables
        self.running = True
        self.clock = pg.time.Clock()

    def events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.KEYDOWN:
                if event.type == pg.K_ESCAPE:
                    self.running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill((23, 53, 235))

        pg.display.flip()


if __name__ == '__main__':
    engine = Engine()

    while engine.running:

        engine.events()
        engine.update()
        engine.render()

        engine.clock.tick(FPS)

pg.quit()
sys.exit()

