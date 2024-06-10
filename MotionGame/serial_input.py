
import threading
import serial


class input_data:# serial monitor and input 
    def __init__(self,comport, baudrate):
        self.data = [1,1,1]
        self.ser = serial.Serial(comport, baudrate, timeout=0.5)# 1/timeout is the frequency at which the port is read

        thread = threading.Thread(target= self.read_data,daemon=True)
        thread.start()

    def read_data(self):
        while True:
            data = self.ser.readline().decode().strip()

            self.data = [float(info.replace("(","").replace(")","")) for info in data.split(',')]
            # list comprehision for data input, becase serial is reading all portions of the input
            # we need to filter the tuples () and ,











