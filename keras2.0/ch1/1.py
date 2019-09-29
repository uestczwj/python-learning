import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.layers as layers


print(tf.__version__)
print(keras.__version__)

model = keras.Sequential()
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer = keras.optimizers.Adam(0.001),
              loss      = keras.losses.categorical_crossentropy,
              metrics   = [keras.metrics.categorical_accuracy])

train_x = np.random.random((1000, 72))
train_y = np.random.random((1000, 10))
val_x   = np.random.random((200, 72))
val_y   = np.random.random((200, 10))

model.fit(train_x,
          train_y,
          epochs          = 10,
          batch_size      = 100,
          validation_data = (val_x, val_y))

dataset = tf.data.Dataset.from_tensor_slices((train_x, train_y))
dataset = dataset.batch(32)
dataset = dataset.repeat()

val_dataset = tf.data.Dataset.from_tensor_slices((val_x, val_y))
val_dataset = val_dataset.batch(32)
val_dataset = val_dataset.repeat()
model.fit(dataset,
          epochs           = 10,
          steps_per_epoch  = 30,
          validation_data  = val_dataset,
          validation_steps = 3)

test_x = np.random.random((1000, 72))
test_y = np.random.random((1000, 10))
model.evaluate(test_x, test_y, batch_size=32)

test_data = tf.data.Dataset.from_tensor_slices((test_x, test_y))
test_data = test_data.batch(32).repeat()
model.evaluate(test_data, steps=30)

# predict
result = model.predict(test_x, batch_size=32)
print(result)