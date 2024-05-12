

from quad import Quad

class Rect:

    def __init__(self, app, pos, offset, size) -> None:
    
        self.app = app

        self.pos = pos
        # Calculate the postions of the corners of the rectangle
        self.corners = [
            pos.x + offset.x - size.x/2, pos.y + offset.y + size.y/2,
            pos.x + offset.x + size.x/2, pos.y + offset.y + size.y/2,
            pos.x + offset.x - size.x/2, pos.y + offset.y - size.y/2,
            pos.x + offset.x + size.x/2, pos.y + offset.y - size.y/2,
        ]
        
        self.quad = Quad(self)

    def update(self) -> None:
        self.quad.update()

