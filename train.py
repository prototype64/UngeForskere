import numpy as np
from tensorflow import keras
from tensorflow.keras import layers


# loading the dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# pixel values for one of the dataset examples before grayscaling
print(x_train[0])

"""nomalize the data since we want every pixel to have a value between 0 and 1 we need to normalize it
   because the current dataset gives every pixel a vlue between 0 and 255 that's because it's colord
   and not greyscaled which means that we are basically grayscaling the dataset.
"""
x_train = tf.keras.utils.normalize(x_train, axis=1).reshape(x_train.shape[0], -1)
x_test = tf.keras.utils.normalize(x_test, axis=1).reshape(x_test.shape[0], -1)

# pixel values for one of the dataset examples after grayscaling
print(x_train[0])

# The ML model
# A sequential model just means that the data that it is going to be trained on is in order
model = tf.keras.models.Sequential()

# The input layer which has 784 neurons since the input image is going to be 28x28 pixels
model.add(tf.keras.layers.Flatten())

"""The hidden layers are the ones that makes all the calculations
   Our first hidden layer is going to have a dense connection between all of our neurons
   which means " a fully connected neural network"
   where each neuron connects to each neuron in the next layer 
   this layer is going to have 128 neurons
   and an activation function
"""   
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, input_shape= x_train.shape[1:]))

# the second hidden layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

"""the output layer it has 10 neurons. each represents every possible output.
   we use Softmax for probability distribution
"""
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# now we compile
model.compile(optimizer='adam',
              # how will we calculate our "error." Neural network aims to minimize loss.
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# now we train. epoch means th amount of times the ML model trains through the whole dataset 
model.fit(x_train, y_train, epochs=5)

# evaluation
val_loss, val_acc = model.evaluate(x_test, y_test)

# model's loss (error)
print(val_loss) 

# model's accuracy
print(val_acc)

model.save("model.h5")


# # number of different digits in dataset
# num_classes = 10
# # pixel, pixel
# input_shape = (28, 28, 1)

""" giving every pixel a value between o and 1
    we are dividing with 255 because every pixel value can go upto 255
"""
# x_train = x_train.astype("float32") / 255
# x_test = x_test.astype("float32") / 255

# # Make sure images have correct dimensions
# x_train = np.expand_dims(x_train, -1)
# x_test = np.expand_dims(x_test, -1)

# print("x_train shape:", x_train.shape)
# print(x_train.shape[0], "train samples")
# print(x_test.shape[0], "test samples")

# y_train = keras.utils.to_categorical(y_train, num_classes)
# y_test = keras.utils.to_categorical(y_test, num_classes)

# # the ML model
# model = keras.Sequential(
#     [
#         #input laget
#         keras.Input(shape=input_shape),
#         # neuron netværks lag der komprimere billedet til en 3x3 format.
#         # en "activation function" er en funktion der 
#         layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
#         # yderligere komprimereing af forrige lag.
#         layers.MaxPooling2D(pool_size=(2, 2)),
#         # neuron netværks lag der komprimere billedet til en 3x3 format.
#         layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
#         # # yderligere komprimereing af forrige lag.
#         layers.MaxPooling2D(pool_size=(2, 2)),
#         # komprimer forrige lag til 1d
#         layers.Flatten(),
#         # mindsker tiden der kræves til træning
#         layers.Dropout(0.5),
#         #output laget
#         layers.Dense(num_classes, activation="softmax"),
#     ]
# )

# # model.summary()

# # Training model
# batch_size = 128
# # number of times the whole dataset gets through the ML model 
# epochs = 15 

# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# #evaluate 
# score = model.evaluate(x_test, y_test, verbose=0)
# print("Test loss:", score[0])
# print("Test accuracy:", score[1])