import tensorflow as tf
import matplotlib.pyplot as plt

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.95):
      print("\nReached 95% accuracy so cancelling training!")
      self.model.stop_training = True

callbacks = myCallback()


mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images,test_labels) = mnist.load_data()
plt.imshow(train_images[0])


training_images=train_images/255.0
test_images=test_images/255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(),
                                   tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                   tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer="Adam",
              loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=90, callbacks=[callbacks])

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)

print(classifications[0])
print(test_labels[0])