
from ursina import *

class Player(Entity):
    def __init__(self):
        super().__init__(model = "cube",color = color.red,texture = "white_cube",collider = 'box',scale = 10,origin_y = .5)

        self.cameraRect = Entity()

        self.cameraRect.parent = self

        self.cameraRect.position_setter(Vec3(0,5,-10))

        



