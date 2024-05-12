

# Class to handle all shader program objects
import numpy as np
import moderngl as mgl

class ShaderHandler:

    def __init__(self, app) -> None:
        
        self.quad_shader = ShaderProgram(app, 'quad')

    def update_shaders(self) -> None:

        self.quad_shader.update_uniforms()

    def render(self) -> None:
        self.quad_shader.render()

# Class to contain a shader program - generally one where the world position will change a lot
# and there are not very many of them and they change numbers often
# Later could make different types of programs that inherit the shader importing but not the rendering
# Will also need to make new quad types and other objects
class ShaderProgram:

    def __init__(self, app, name: str) -> None:
        self.app = app 
        # Import shader code
        with open(f'shaders/{name}.vert', 'r') as file:
            vertex_shader = file.read()

        with open(f'shaders/{name}.frag', 'r') as file:
            fragment_shader = file.read()
        
        # Return it as a program object
        self.program = app.ctx.program(
            vertex_shader = vertex_shader,
            fragment_shader = fragment_shader
        )
        self.set_uniforms()

        self.vertex_data = []


    def set_uniforms(self) -> None:
        # Set the default uniforms for the shader 
        self.program['tex'] = 0

    def update_uniforms(self) -> None:
        # Will be used to update uniforms for render calls
        # Such as camera position or rotation
        pass

    def get_vao(self):

        vertex_data = np.array(self.vertex_data, dtype='f')
        vbo = self.app.ctx.buffer(vertex_data)
        self.vao = self.app.ctx.vertex_array(self.program, [(vbo, '2f 2f', 'vert', 'tex_uv')])
        
    def render(self) -> None:

        self.update_uniforms()
        self.get_vao()
        self.vao.render(mgl.TRIANGLES)

        self.vertex_data = []


    

