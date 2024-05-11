
import sys
import pygame as pg
import moderngl as mgl
import glm

import config
import texturer
import shader_program
import sprite
import quad


import player
import camera

WINDOWSIZE = config.WINDOWSIZE

class Engine:
    def __init__(self) -> None:
        pg.init()

        # Create window
        self.screen = pg.display.set_mode(WINDOWSIZE, pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        self.ctx.gc_mode = 'auto'

        # Setup variables
        self.running = True
        self.clock = pg.time.Clock()

        self.texturer = texturer.Textures(self)
        self.camera = camera.Camera(self)
        self.shader_programs = shader_program.ShaderProgram(self)
        
        

        self.player_quad = quad.Quad(self)

        #self.sprites = [sprite.Sprite(self, (0, 0), (32, 32), self.quad) for _ in range(300)]
        self.player = player.Player(self)

    def create_scene(self):
        # Generate test positions
        #x = -960
        #y = 500
        #for sprites in self.sprites:
        #    sprites.set_attributes((x, y), 0, 1)
        #    x += 32
        #    if x == 960:
        #        x = -960
        #        y -= 32
        pass

    def events(self):

        self.keys = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
 
 
    def update(self):
        
        self.dt = self.clock.tick() / 1_000
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

        

        self.player.update()

        self.camera.update_position(glm.vec3(*self.player.render_rect.center, 0))

        #for sprite in self.sprites:
        #    sprite.update()


    def render(self):

        self.ctx.clear()

        self.rebuild_buffers() # Move all the quads and stuff to a differnect class or something that can load them in 

        # Replace with camera update methods in the update function


        self.shader_programs.update_quad_uniforms() # Good

        self.render_meshes()

        pg.display.flip()


    def rebuild_buffers(self):
        self.player_quad.rebuild_vertex_buffer()

    def render_meshes(self):
        self.player_quad.render()

fps_test = True
time_cutoff = 10

if __name__ == '__main__':

    engine = Engine()
    engine.create_scene()

    frame_count = 0

    while engine.running:

        frame_count += 1

        engine.events()
        engine.update()
        engine.render()

        if fps_test:
            if pg.time.get_ticks() > time_cutoff * 1000:
                print(f'Number of frames rendered/s: {frame_count/10}')
                break
        else:
            engine.clock.tick(config.FPS)

    pg.quit()
    sys.exit()
