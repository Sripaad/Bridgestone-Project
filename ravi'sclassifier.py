#importing libraries and splitting datasets
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from IPython.display import display
from PIL import Image
import numpy as np

classifier=Sequential()

classifier.add(Conv2D(32,3,3,input_shape=(64,64,3),activation='relu'))

classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Flatten())
#CNN LAYERS
classifier.add(Dense(output_dim=128,activation='relu'))
classifier.add(Dense(output_dim=128,activation='sigmoid'))

classifier.compile(optimizer='adam' , loss= 'binary_crossentropy', metrics=['accuracy'])

train_datagen=ImageDataGenerator(rescale=1./255,shear_range=(64,64),zoom_range=32,horizontal_flip=True)

test_datagen=ImageDataGenerator(rescale=1./255)

training_set=train_datagen.flow_from_directory('minion_evilminion/minion',target_size=(64,64),batch_size=32,class_mode='binary')

test_set=test_datagen.flow_from_directory('minion_evilminion/evilminion',target_size=(64,64),batch_size=32,class_mode='binary')

classifier.fit_generator(training_set,steps_per_epoch=8000,epochs=10,validation_data=test_set,validation_step=800)

test_image=image.load_img('place-your-image.jpg',target_size=(64,64))
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=classifier.predict(test_image)
training_set.class_indices
if result[0][0]>=0.5:
	prediction='minion'
else:
	prediction='evil_minion'
print(prediction)		
