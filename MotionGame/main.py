
from ursina import Ursina,Text,Vec2,Vec3,Button,camera,update
from ursina import application
import math

from tunnel import *
from wallpatterns import get_random_wallpattern,make_random_wallpatterns
from serial_input import input_data
from player import Player

arduino_input= input_data("COM9",11520)# create serial connection use proper COM port

app = Ursina()# start game engine

wall_speed = 10#inital wall speed
score = 0

player = Player()# use created player class and set start positon
player.position = Vec3(500,500,10)

score_text = Text("SCORE:0",scale=2)
score_text.origin = Vec2(3,-9)

walls: list[death_wall] = []# create a list of useable wall peices
moving_walls: list[death_wall] = []# create a list of only the moving walls

for x in range (-10,50):# make a tunnel for visuals 
    if x <2 and x >-2:
        death_tunnel(position= x)# make a portion of the tunnel coliadable
    else:
        tunnel(position=x)

def spawn_moving_wall():# make walls to move, max being y range times x range
    for y in range(10):
        for x in range(10):
            moving_wall = death_wall(scale = (blockscale,blockscale,150))
            moving_wall.color = color.blue
            moving_wall.position= Vec3((blockscale)-1000,blockscale-1000,0) + Vec3(0,250,5*10*blockscale)
            walls.append(moving_wall)

def reset_wall(wall):
    wall.position = Vec3(blockscale-1000,blockscale-1000,0) + Vec3(0,250,5*10*blockscale)

def place_wall(wall_pattern,walls = walls):# postion walls at end of tunnel for movement
    y_placement = -1
    x_placement = -1
    wall_index = -1
    for row in wall_pattern:
        y_placement +=1
        x_placement = -1
        for block in row:
            x_placement +=1
            wall_index +=1
            if block == 1:
                moving_walls.append(walls[wall_index])# add appropriate walls to list for moving
                walls[wall_index].position = Vec3((x_placement*blockscale),y_placement*blockscale,0) + Vec3(0,250,5*10*blockscale)

def move_wall(moving_walls = moving_walls):
    global wall_speed
    global score
    global score_text

    if moving_walls != []:
        for wall in moving_walls:
            wall.z -=wall_speed
            if wall.z <= -50:
                moving_walls.remove(wall)
                reset_wall(wall)

    else:
        wall_speed += 1
        score += 1
        score_text.text = "SCORE:" + str(score)
        place_wall(make_random_wallpatterns())


def start_up():# initialization

    spawn_moving_wall()
    place_wall(get_random_wallpattern())

start_up()

pause_handler = Entity(ignore_paused=True)
pause_text = Text('PAUSED', origin=(0,0), scale=2, enabled=False) # Make a Text saying "PAUSED" just to make it clear when it's paused.

def pause_handler_input(key):# make a way to pause if needed
    if key == 'escape':
        application.paused = not application.paused # Pause/unpause the game.
        pause_text.enabled = application.paused     # Also toggle "PAUSED" graphic.

pause_handler.input = pause_handler_input

def end_game():# end conditions
    end_game = Button('END',ignore_paused=True, on_click = app.destroy)
    application.pause()



def update(): # method of running the game
    camera.position = player.position + Vec3(0,5,-200)# make camera follow player

    x_vect = arduino_input.data[0]# read in data from plyground express
    y_vect= arduino_input.data[1]
    z_vect = arduino_input.data[2]
    maganatude = math.sqrt(pow(x_vect,2)+pow(y_vect,2)+pow(z_vect,2))# create magantude of vector for calculations
    roll = (math.acos(y_vect/maganatude)*(180/math.pi))-90 # calculate the roll and pitch amounts
    pitch= (math.acos(x_vect/maganatude)*(180/math.pi))-90

    player.rotate(Vec3(roll/100,0,pitch/100)) # rotate player with a scaling factor to decrease sensativity
    player.rotation_y = 0

    #print(player.rotation_z,player.rotation_x)
    player.position += Vec3(player.rotation_z/10,-player.rotation_x/10,0)# create force vector based on roll and pirch

    #print(player.position)
    if player.intersects():##end condition
        player.world_position = Vec3(500,500,10)
        player.rotation = Vec3(0,0,0)

        end_game()

    move_wall()

app.run()# start
