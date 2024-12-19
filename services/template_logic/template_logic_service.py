import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
from services.service import Logic,Data


def callback(data:Data):
    print(f"Received data {Data.decode(data)}")

logic = Logic()

logic.setInput(('localhost',42069))

logic.start(callback)