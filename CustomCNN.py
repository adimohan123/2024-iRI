import sys

# Add the project directory to the Python path
data_path = 'C:\\Users\\Aweso\\Downloads\\The folder\\Data\\PreProc'

# Verify the path was added correctly
print("Python path:")
print(data_path)

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds

# Import and register the custom dataset
try:
    import PreProc.db1  # Adjust this to match your actual module structure
    print("Custom dataset module imported successfully.")
except ImportError as e:
    print("Error importing custom dataset module:", e)

# Load the custom dataset
try:
    ds = tfds.load('db1')  # Replace 'my_dataset' with your actual dataset name
    print("Custom dataset loaded successfully.")
    print(ds)
except Exception as e:
    print("Error loading custom dataset:", e)





'''
model = models.Sequential()
model.add(layers.Conv1D(32,3,activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels))

model.summary()

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(test_acc)
'''