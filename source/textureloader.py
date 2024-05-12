
import pygame as pg
import moderngl as mgl

def load_texture(app, name):

    texture = pg.image.load(f'assets/{name}.png')
    texture = app.ctx.texture(
        size = texture.get_size(),
        components = 4,
        data = texture.get_view('1')
    )

    texture.swizzle = 'RGBA'
    texture.filter = (mgl.NEAREST, mgl.NEAREST)

    return texture

