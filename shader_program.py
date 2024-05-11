 
import glm
import config

class ShaderProgram:
    def __init__(self, app) -> None:
        
        self.app = app

        self.quad_shader = self.get_program('quad')

        self.set_uniforms_on_init()

    
    def set_uniforms_on_init(self):
        self.quad_shader['tex'] = 0
        #self.quad_shader['window_size'].write(config.WINDOWSIZE)

        #self.quad_shader['m_proj'].write(self.app.camera.m_proj)
        #self.quad_shader['m_model'].write(glm.mat4())


    def update_quad_uniforms(self):
        #self.quad_shader['m_view'].write(self.app.camera.m_view)
        #self.quad_shader['position'].write()
        pass

    def get_program(self, name):

        with open(f'shaders/{name}.vert', 'r') as file:
            vertex_shader = file.read()

        with open(f'shaders/{name}.frag', 'r') as file:
            fragment_shader = file.read()

        program = self.app.ctx.program(
            vertex_shader=vertex_shader,
            fragment_shader=fragment_shader
        )
        return program
