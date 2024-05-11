
import moderngl as mgl
import numba as nb
import numpy as np

class Quad:
    def __init__(self, app) -> None:
        self.ctx = app.ctx
        self.program = app.shader_programs.quad_shader

        self.vertex_data = []

    def get_vertex_array_obj(self):

        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(self.program, [(vbo, '2f 2f', 'vert', 'texcoord')])

        return vao

    def rebuild_vertex_buffer(self):

        self.vao = self.get_vertex_array_obj()
        self.vertex_data = []

    def render(self):
        self.vao.render(mgl.TRIANGLES)

    def get_vertex_data(self):
        
        vertex_data = np.array(self.vertex_data, dtype='f')
       
        return vertex_data
