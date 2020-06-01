from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import pandas as pd
from matplotlib import pyplot as plt
import sklearn as sk

filepath = "Dataset_Subsystem_2.csv"
data = pd.read_csv(filepath)

X = data.loc[:,"palm_root_x":"dorsal_pinky_4_y"]
Y = data.loc[:,"camera_facing_side":"gesture"]
Y = Y[["gesture", "camera_facing_side"]].agg('_'.join, axis=1)
Y = Y.to_numpy()

label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(Y)
Y = to_categorical(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.10, random_state=42)
print(X_test.iloc[0])


model = Sequential()
model.add(Input(shape=(80,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.build()
adam = Adam(lr=0.001)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=30, batch_size=8, validation_split=1/9) # 80 % train 10 % validation, 10 % test
print(history)
val_loss, val_acc = model.evaluate(X_test, y_test)
print(val_loss, val_acc)

training_loss = history.history['loss']
test_loss = history.history['val_loss']


# Create count of the number of epochs
epoch_count = range(1, len(training_loss) + 1)

# Visualize loss history
plt.plot(epoch_count, training_loss, 'r--')
plt.plot(epoch_count, test_loss, 'b-')
plt.legend(['Training Loss', 'Test Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show();

model.save("../RPSLSPlayer/model/Sub2-weights2-best.hdf5")


print("Model 1")
print(history)
print(val_loss, val_acc)

# Confusion matrix and classification report
predictions = model.predict(X_test)
y_pred = np.argmax(predictions, axis=1)
y_true = np.argmax(y_test, axis=1)
print('Confusion Matrix')
print(sk.metrics.confusion_matrix(y_true, y_pred))
print('Classification Report')
target_names = ['fistdorsal', 'fistpalm', 'opendorsal', 'openpalm',
       'three_fingersdorsal', 'three_fingerspalm']
print(sk.metrics.classification_report(y_true, y_pred, target_names=target_names))