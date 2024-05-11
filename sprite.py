
import pygame as pg
import numba as nb

class Sprite:
    def __init__(self, app, position, size, quad) -> None:
        self.app = app
        self.quad = quad

        self.size = size
        self.render_rect = pg.rect.FRect(*position, *self.size)
        self.rotation = 0
        self.scale = 1
        self.size = size


    def set_attributes(self, position, rotation, scale):
        self.render_rect.center = position
        self.rotation = rotation
        self.scale = scale

    def update(self):
        self.add_vertex_data()

    def add_vertex_data(self):
        self.quad.vertex_data += self.get_vertex_sprite_data()

    def get_vertex_sprite_data(self):

        
        tl = ((-self.size[0] / 2) + self.render_rect.center[0], (self.size[1] / 2) + self.render_rect.center[1])
        br = ((self.size[0] / 2) + self.render_rect.center[0], (-self.size[1] / 2) + self.render_rect.center[1])

        vertex_data = [

            tl[0], tl[1], 0.0, 0.0,
            tl[0], br[1], 1.0, 0.0,
            br[0], tl[1], 0.0, 1.0,
            br[0], tl[1], 0.0, 1.0,
            tl[0], br[1], 1.0, 0.0,
            br[0], br[1], 1.0, 1.0]

        return vertex_data
        
