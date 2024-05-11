
import pygame as pg
#import numba
import config
WINDOWSIZE = tuple(config.WINDOWSIZE)


#@numba.njit
def calc_uvs(size, pos):

    uvs_tl = (2*(pos[0] / WINDOWSIZE[0]) - 1, 2*(1 - (pos[1] / WINDOWSIZE[1])) - 1)
    uvs_br = (2*((pos[0] + size[0]) / WINDOWSIZE[0]) - 1, 2*(1 - ((pos[1] + size[1]) / WINDOWSIZE[1])) - 1)

    return uvs_tl, uvs_br

#@numba.njit 
def calc_mirrors(mirroring):
    corners = [0.0, 0.0,
               1.0, 0.0,
               0.0, 1.0,
               1.0, 1.0]
    
    if mirroring[0]:
        corners[0] = 1.0
        corners[2] = 0.0
        corners[4] = 1.0
        corners[6] = 0.0

    if mirroring[1]:
        corners[1] = 1.0
        corners[3] = 1.0
        corners[5] = 0.0
        corners[7] = 0.0

    return corners

class Sprite_data:
    def __init__(self, sprite_sets, shader, size, ID) -> None:
        
        self.sprite_sets = sprite_sets
        self.shader = shader
        self.id_ = ID

        self.current_set = 0
        self.index = 0

        self.render_rect = pg.FRect(0, 0, *size)

        self.mirroring = (False, False)
        self.corners = calc_mirrors(self.mirroring)

        self.render = True

    def update(self, x, y):
        self.render_rect.bottomleft = (x, y)

    

    

    
