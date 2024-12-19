# this service aims to take an input from the user from the cmdline and pass it though a tensorflow network in order to pass its output to the next services input
from service import Logic,Data


def callback(data:Data):
    print(f"Received data {Data.decode(data)}")

logic = Logic()

logic.setInput(('localhost',42069))

logic.start(callback)