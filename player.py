
import config
import pygame as pg

import sprite

# Make a default class for something that has velocities and is effected by gravity

class Player(sprite.Sprite):
    def __init__(self, app) -> None:
        super().__init__(
            app=app,
            position=(0, 0),
            size=(512, 512),
            quad=app.player_quad
        )
        self.vel = pg.math.Vector2(0, 0)

    def update(self):

        if self.app.keys[pg.K_w] and not self.app.keys[pg.K_s]:
            self.vel[1] = config.PLAYER_SPEED
        elif self.app.keys[pg.K_s] and not self.app.keys[pg.K_w]:
            self.vel[1] = -config.PLAYER_SPEED
        else:
            self.vel[1] = 0

        if self.app.keys[pg.K_d] and not self.app.keys[pg.K_a]:
            self.vel[0] = config.PLAYER_SPEED
        elif self.app.keys[pg.K_a] and not self.app.keys[pg.K_d]:
            self.vel[0] = -config.PLAYER_SPEED
        else:
            self.vel[0] = 0
        
        self.render_rect.center += self.vel * self.app.dt
        
        self.add_vertex_data()
