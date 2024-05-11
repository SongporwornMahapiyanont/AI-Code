import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

from tensorflow.keras.applications.inception_v3 import preprocess_input

model = load_model('best_model_ws05_1.h5',compile=False)

target_img_shape=(128,128)
test_image = load_img('ss1.jpg',target_size=target_img_shape)
test_image_show = test_image

test_image = img_to_array(test_image)
test_image = preprocess_input(test_image)

test_image = np.expand_dims(test_image,axis=0) # (1, 128, 128, 3)
print(test_image.shape)

result = model.predict(test_image)
print(result)

class_answer = np.argmax(result,axis=1)
if class_answer == 0:
    predict = 'building'
elif class_answer == 1:
    predict = 'forest'
elif class_answer == 2:
    predict = 'mountain'
elif class_answer == 3:
    predict = 'sea'
elif class_answer == 4:
    predict = 'street'
print(predict)

plt.imshow(test_image_show)
plt.show()
