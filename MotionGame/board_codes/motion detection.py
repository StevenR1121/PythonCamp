# Write your code here :-)
import time
import board
import adafruit_lis3dh
import busio


i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)## create access to accelrometer
lis3dh.range = adafruit_lis3dh.RANGE_8_G

while True:
    x, y, z = lis3dh.acceleration## break down outputs into x,y,z
    print((x, y, z))## print tuple to terminal for reading later
    time.sleep(0.1)
