import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
from services.service import Sensor,Data

sensor = Sensor()

sensor.setOutput(('localhost',42069))

sensor.send(Data([0.1,0.1,0.1,0.1]))