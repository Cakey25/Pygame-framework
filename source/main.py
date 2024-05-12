
# Imports
import moderngl as mgl
import pygame as pg
import sys
# My modules
from config import *
from textureloader import load_texture
from rect import Rect
from shaderprogram import ShaderHandler

class Engine:

    def __init__(self) -> None:
        
        # Module initialization
        pg.init()

        # Window creation
        self.window = pg.display.set_mode(WINDOW_SIZE, pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        self.ctx.gc_mode = 'auto'

        # Other variables
        self.clock = pg.time.Clock()
        self.running = True

        self.textures = dict()
        self.program_handler = ShaderHandler(self)

    def load_data(self) -> None:
        tex = load_texture(self, 'coloured_tiles_sheet')
        self.textures['coloured_tiles_sheet'] = tex

    def create_scene(self) -> None:
        self.test_rect = Rect(self, pg.Vector2(0,0), pg.Vector2(0,0), pg.Vector2(64, 64))
        self.textures['coloured_tiles_sheet'].use(0)

    def render(self) -> None:
        
        self.ctx.clear()
        self.program_handler.render()

        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')
        pg.display.flip()

    def update(self) -> None:
        
        self.dt = self.clock.tick() / 1_000

        self.test_rect.update()

    def events(self) -> None:
        
        # Get all events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

if __name__ == '__main__':
    # Start game 
    game = Engine()
    game.load_data()
    game.create_scene()

    while game.running:
        # Main loop
        game.events()
        game.update()

        #game.clock.tick(FPS_TARGET)

        game.render()

    pg.quit()
    sys.exit()




