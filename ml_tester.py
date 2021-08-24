import tkinter as tk
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

#number of different digits in dataset
num_classes = 10
#pixel, pixel
input_shape = (28, 28, 1)

# splitting training and test data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# giving every pixel a value between o and 1
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Make sure images have correct dimensions
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# print("x_train shape:", x_train.shape)
# print(x_train.shape[0], "train samples")
# print(x_test.shape[0], "test samples")

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

#the ML model

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        
        layers.MaxPooling2D(pool_size=(2, 2)),
        
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        
        layers.MaxPooling2D(pool_size=(2, 2)),
        
        layers.Flatten(),
        
        layers.Dropout(0.5),
        
        layers.Dense(num_classes, activation="softmax"),
    ]
)

# model.summary()

#Training model

batch_size = 128

#number of times the whole dataset gets through the ML model 
epochs = 15


model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

#evaluate 
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])





# lastx, lasty = 0, 0

# Takes the coordinates of the mouse when you click the mouse
# def xy(event):
#     global lastx, lasty
#     lastx, lasty = event.x, event.y
 
# this makes the new starting point of the drawing
# def addLine(event):
#     global lastx, lasty
#     canvas.create_line((lastx, lasty, event.x, event.y))
#     lastx, lasty = event.x, event.y
 
# root = tk.Tk()
# root.geometry("1200x1000")
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
 
# canvas = tk.Canvas(root)
# canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
# canvas.bind("<Button-1>", xy)
# canvas.bind("<B1-Motion>", addLine)
 
# root.mainloop()