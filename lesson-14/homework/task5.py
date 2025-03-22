import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def flip_image(img_array):
    flipped_h = np.fliplr(img_array)
    flipped_v = np.flipud(img_array) 
    return flipped_h, flipped_v 

def add_noise(img_array, noise_level = 30):
    noise = np.random.randint(-noise_level, noise_level, img_array.shape(), dtype=np.int16) 
    noise_img = np.clip(img_array + noise, 0, 255).astype(np.uint8) 
    return noise_img

def brighten_channels(img_array, brightness=40):
    brightened_img = np.clip(img_array + brightness, 0, 255).astype(np.uint8)
    return brightened_img

def apply_mask(img_array, mask_size=(100, 100)):
    h, w, _ = img_array.shape
    y_start, x_start = (h - mask_size[0]) // 2, (w - mask_size[1]) // 2
    img_array[y_start:y_start + mask_size[0], x_start:x_start + mask_size[1]] = [0, 0, 0]
    return img_array

def show_image(img_array, title="Image"):
    plt.figure(figsize=(5, 5))
    plt.imshow(img_array)
    plt.axis("off") 
    plt.title(title)
    plt.show()

img = Image.open('lesson-14/images/bird.jpg')
img_array = np.array(img)

flipped_h, flipped_v = flip_image(img_array)
noisy_img = add_noise(img_array)
brightened_img = brighten_channels(img_array)
masked_img = apply_mask(img_array.copy())

show_image(flipped_h, "Flipped Horizontally")
show_image(flipped_v, "Flipped Vertically")
show_image(noisy_img, "Noisy Image")
show_image(brightened_img, "Brightened Image")
show_image(masked_img, "Masked Image")

Image.fromarray(flipped_h).save("flipped_h.jpg")
Image.fromarray(flipped_v).save("flipped_v.jpg")
Image.fromarray(noisy_img).save("noisy.jpg")
Image.fromarray(brightened_img).save("brightened.jpg")
Image.fromarray(masked_img).save("masked.jpg")