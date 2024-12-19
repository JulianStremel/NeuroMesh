import os
import sys
import tensorflow as tf
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
from services.service import Logic,Data

model = tf.keras.models.load_model('.\\services\\numbers_logic\\numbers_model.keras')

def callback(data:Data):
    data = Data.decode(data)
    prediction = model.predict([data])
    print(f"Received data {data} and predicted {np.argmax(prediction)}")

logic = Logic()

logic.setInput(('localhost',42069))

if __name__ == '__main__':
    logic.start(callback)