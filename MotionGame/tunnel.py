from ursina import Entity,color,scene,destroy,Vec3

class death_wall(Entity):
    def __init__(self,scale):
        super().__init__(model = "cube",color = color.green,texture = "white_cube",collider = 'box',ignore = True,
               parent = scene,
               origin_y = 2,scale = scale
               )
    def __del__(self):
        destroy(self)
        
    
        
class normal_wall(Entity):
    def __init__(self,scale):
        super().__init__(model = "cube",color = color.green,texture = "white_cube",ignore = True,
               parent = scene,
               origin_y = 2,scale = scale,
               )   

blockscale = 100

class death_tunnel():
    def __init__(self,position):

        for z in range (1):
            for x in range(10):

                ground = death_wall(scale = (blockscale,1,blockscale))
                ground.position= Vec3((x*blockscale),5,z*blockscale) + Vec3(0,0,position*blockscale)

        for z in range (1):
            for x in range(10):

                ground = death_wall(scale = (blockscale,1,blockscale))
                ground.position= Vec3(x*blockscale,10*blockscale,z*blockscale)+ Vec3(0,0,position*blockscale)

        for z in range (1):
            for y in range(10):

                ground = death_wall(scale = (1,blockscale,blockscale))
                ground.position= Vec3(-blockscale/2,y*blockscale+(blockscale/4)*10,z*blockscale)+ Vec3(0,0,position*blockscale)

        for z in range (1):
            for y in range(10):

                ground = death_wall(scale = (1,blockscale,blockscale))
                ground.position= Vec3(10*blockscale-blockscale/2,y*blockscale+(blockscale/4)*10,z*blockscale)+ Vec3(0,0,position*blockscale)

class tunnel():
    def __init__(self,position):

        for z in range (1):
            for x in range(10):

                ground = normal_wall(scale = (blockscale,1,blockscale))
                ground.position= Vec3((x*blockscale),5,z*blockscale) + Vec3(0,0,position*blockscale)

        for z in range (1):
            for x in range(10):

                ground = normal_wall(scale = (blockscale,1,blockscale))
                ground.position= Vec3(x*blockscale,10*blockscale,z*blockscale)+ Vec3(0,0,position*blockscale)

        for z in range (1):
            for y in range(10):

                ground = normal_wall(scale = (1,blockscale,blockscale))
                ground.position= Vec3(-blockscale/2,y*blockscale+(blockscale/4)*10,z*blockscale)+ Vec3(0,0,position*blockscale)

        for z in range (1):
            for y in range(10):

                ground = normal_wall(scale = (1,blockscale,blockscale))
                ground.position= Vec3(10*blockscale-blockscale/2,y*blockscale+(blockscale/4)*10,z*blockscale)+ Vec3(0,0,position*blockscale)
 
