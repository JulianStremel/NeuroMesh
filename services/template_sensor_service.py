# this service aims to take an input from the user from the cmdline and pass it though a tensorflow network in order to pass its output to the next services input
from service import Sensor,Data


sensor = Sensor()

sensor.setOutput(('localhost',42069))

sensor.send(Data([0.1,0.1,0.1,0.1]))