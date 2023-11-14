# from scipy.misc import imresize
# import imageio.v2 as imageio
from skimage.transform import resize
from imageio.v2 import imread
# from keras.preprocessing.image import save_img
from keras.utils import image_utils
# import cv2
# Read an JPEG image into a numpy array
img = imread('./assets/cat.jpg')
print(img.dtype, img.shape)  # Prints "uint8 (400, 248, 3)"

# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (400, 248, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively.
img_tinted = img * [1, 0.95, 0.9]

# Resize the tinted image to be 300 by 300 pixels.
img_tinted = resize(img_tinted, (300, 300))
print(img_tinted.dtype, img_tinted.shape)

# # Write the tinted image back to disk
image_utils.save_img('assets/cat_tinted.jpg', img_tinted)