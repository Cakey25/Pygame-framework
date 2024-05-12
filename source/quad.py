

class Quad:

    def __init__(self, rect) -> None:
        
        self.rect = rect
        self.program = rect.app.program_handler.quad_shader
        # so turn the shader program into what the quad
        # acts like in the previous code and this will
        # contain the coordinates of vertices and stuff
        # while that has the vao and stuff only once


    # Combine the Rect and quad class
    def update(self) -> None:

        vertex_data = [self.rect.corners[0], self.rect.corners[1], 0.0, 0.0,
                       self.rect.corners[4], self.rect.corners[5], 1.0, 0.0,
                       self.rect.corners[2], self.rect.corners[3], 0.0, 1.0,
                       self.rect.corners[2], self.rect.corners[3], 0.0, 1.0,
                       self.rect.corners[4], self.rect.corners[5], 1.0, 0.0,
                       self.rect.corners[6], self.rect.corners[7], 1.0, 1.0]

        self.program.vertex_data += vertex_data
        
