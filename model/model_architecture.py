from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import pandas as pd

filepath = "Dataset_Subsystem_2.csv"
data = pd.read_csv(filepath)

X = data.loc[:,"palm_root_x":"dorsal_pinky_4_y"]
Y = data.loc[:,"camera_facing_side":"gesture"]
Y = Y[["gesture", "camera_facing_side"]].agg('_'.join, axis=1)
Y = Y.to_numpy()

label_encoder = LabelEncoder()
Y = label_encoder.fit_transform(Y)
Y = to_categorical(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
print(X_test.iloc[0])
model = Sequential()
model.add(Input(shape=(80,)))
model.add(Dense(100, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.build()
print(model.summary())
adam = Adam(lr=0.01)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=3, batch_size=8, validation_split=0.2)
print(history)
val_loss, val_acc = model.evaluate(X_test, y_test)

print(val_loss, val_acc)
model.save("Sub2-weights.hdf5")

