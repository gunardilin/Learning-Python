"""Hello World for ML.
Source: https://codelabs.developers.google.com/codelabs/tensorflow-lab1-helloworld/#0"""
import tensorflow as tf
import numpy as np
from tensorflow import keras
import datetime
startTime = datetime.datetime.now()
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

model.fit(xs, ys, epochs=5000)

if __name__ == "__main__":
    print(model.predict([10.0]))
    endTime = datetime.datetime.now()
    duration = endTime - startTime
    print(duration.total_seconds())