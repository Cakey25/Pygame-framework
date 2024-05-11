
from config import *
import glm

class Camera:
    def __init__(self, app) -> None:
        self.app = app
        self.position = glm.vec3(0, 0, 0)
        self.angles = glm.vec3(0, 0, 0)

        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        print(self.m_proj)
        self.m_view = glm.mat4()

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.m_view = glm.lookAt(self.position, self.position + self.forward, self.up)

    def update_vectors(self):
        self.forward.x = glm.cos(self.angles.x) * glm.cos(self.angles.x)
        self.forward.y = glm.sin(self.angles.y)
        self.forward.z = glm.sin(self.angles.x) * glm.cos(self.angles.x)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def rotate_roll(self, delta_z):
        self.angles.z -= delta_z

    def update_position(self, position):
        self.position = glm.vec3(position)
