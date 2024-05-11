
import pygame as pg
import moderngl as mgl

class Textures:
    def __init__(self, app) -> None:
        
        self.app = app
        self.ctx = app.ctx

        self.texture_0 = self.load_texture('coloured_tiles_sheet')

        self.texture_0.use(0)

    def load_texture(self, name):
        
        texture = pg.image.load(f'assets/{name}.png')

        texture = self.ctx.texture(
            size = texture.get_size(),
            components = 4,
            data=texture.get_view('1')
        )
        
        texture.swizzle = 'RBGA'
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        return texture