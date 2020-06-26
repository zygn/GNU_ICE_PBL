import tensorflow as tf
from tensorflow.keras import datasets, layers, models


x = np.load('D:/ML/X.npy')
y = np.load('D:/ML/Y.npy')

print(x.shape, y.shape)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(300, 300, 3),padding='same',strides=1))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu',padding='same',strides=1))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(8, activation='softmax'))
model.summary()
model.compile(optimizer='adam',loss='categorical_crossentropy')
model.fit(x, y, epochs=50)

model.save('D:/ML/_model/50md.h5')