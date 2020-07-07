from tensorflow.keras import models
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout,LSTM
from tensorflow.keras.utils import to_categorical, normalize
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l1,l2
import numpy as np
from load_dataset import load_data, preprocess_data
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from time import process_time
import matplotlib.pyplot as plt

data_dir = '/home/kangle/dataset/PedBicCarData'
train_data, train_label, test_data, test_label = load_data(data_dir, 2, 2)
train_data, train_label, test_data, test_label = preprocess_data(train_data, train_label, test_data, test_label, 'rnn')

# train_data = np.squeeze(train_data)
# test_data = np.squeeze(test_data)
# train_data = np.transpose(train_data, (0,2,1))
# test_data = np.transpose(test_data, (0,2,1))

train_data, val_data, train_label, val_label = train_test_split(train_data, train_label, test_size=0.1, random_state=42)
print("Split training data into training and validation data:\n")
print("training data: %d" % train_data.shape[0])
print("validation data: %d" % val_data.shape[0])

model = models.Sequential()
model.add(LSTM(64, input_shape=(train_data.shape[1],train_data.shape[2])))
model.add(Dropout(0.2));
model.add(Dense(128, activation='relu'));
model.add(Dropout(0.2));
model.add(Dense(5, activation='softmax'))

opt = Adam(learning_rate=0.01)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_data,
                    train_label,
                    epochs=10,
                    batch_size=128,
                    verbose=2,
                    validation_data=(val_data, val_label))

# evaluate model
test_pred = model.predict(test_data)

t_start = process_time()
_,acc = model.evaluate(test_data, test_label, batch_size=128, verbose=2)
t_end = process_time()
t_cost = t_end - t_start
print(f"Test Accuracy: {acc:.4f}, Inference time: {t_cost:.2f}s")

plt.figure()
plt.subplot(211)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(['train', 'test'], loc='lower right')
plt.grid(True)
plt.subplot(212)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'test'], loc='upper right')
plt.grid(True)
plt.suptitle('model accuracy and loss')
plt.tight_layout()
plt.show()
