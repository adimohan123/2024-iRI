import sys
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Assuming the dataset is in CSV format and the file path is correct
file_path = "C:\\Users\\Aweso\\Downloads\\The folder\\Data\\db1\\S9_A1_E3.csv"

# Define the column names and types (adjust these based on your dataset)
columns = [f'emg{x}' for x in range(10)]
columns.extend(["restimulus", "rerepetition", "exercise"])
print(columns)



# Load the CSV dataset
dataset = tf.data.experimental.make_csv_dataset(
    file_path,
    batch_size=32,
    column_names=columns,
    label_name='restimulus',
    num_epochs=1,
    header=True
)

for features, label in dataset.take(1):
    print('Features:', features)
    print('Label:', label)

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

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

print(test_acc)
'''
