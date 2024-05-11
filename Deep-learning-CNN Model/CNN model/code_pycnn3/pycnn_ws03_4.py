import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input

model = load_model('best_model_ws03_3.h5',compile=False)

target_img_shape=(128,128)
test_image = load_img('fw3.jpg',target_size=target_img_shape)
test_image_show = test_image

test_image = img_to_array(test_image)
test_image = preprocess_input(test_image)

test_image = np.expand_dims(test_image,axis=0) # (1, 128, 128, 3)
print(test_image.shape)

result = model.predict(test_image)
print(result)

class_answer = np.argmax(result,axis=1)
if class_answer == 0:
    predict = 'rose'
elif class_answer == 1:
    predict = 'sunflower'
elif class_answer == 2:
    predict = 'tulip'
print(predict)

plt.imshow(test_image_show)
plt.show()



