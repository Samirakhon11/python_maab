import numpy as np
from PIL import Image
import cv2

def flip_v_image(img_array):
    flipped_v = cv2.flip(img_array, 0)  
    return flipped_v

def flip_h_image(img_array):
    flipped_h = cv2.flip(img_array, 1)
    return flipped_h

img = Image.open('lesson-14/images/bird.jpg').convert("RGB") 
img_array = np.array(img)  

r, g, b = cv2.split(img_array) 
r = np.clip(r + 40, 0, 255) 
brightened_img = cv2.merge([r, g, b])  

noise_level = 30
noise = np.random.randint(-noise_level, noise_level, img_array.shape, dtype = np.int16)  
noisy_img = np.clip(img_array + noise, 0, 255).astype(np.uint8)  

flipped_v = flip_v_image(img_array)
flipped_h = flip_h_image(img_array)

Image.fromarray(flipped_v).save("flipped_v.jpg")   
Image.fromarray(flipped_h).save("flipped_h.jpg") 
Image.fromarray(brightened_img).save("brightened.jpg") 
Image.fromarray(noisy_img).save("noisy.jpg") 

while True:
    print("1. Original image")
    print("2. Flipped to the right")
    print("3. Upside down") 
    print("4. Brightened image")
    print("5. Image with noise") 
    print("6. Exit") 

    try:
        option = int(input("Which version of the picture do you want to see: "))
        if option < 1 or option > 6:
            raise ValueError("Enter a number between 1 and 6")
    except ValueError as e:
        print(e)
        continue  

    if option == 1:
        cv2.imshow("Original image", img_array)  
    elif option == 2:
        cv2.imshow("Flipped to the right", flipped_h)
    elif option == 3:
        cv2.imshow("Upside down", flipped_v) 
    elif option == 4:
        cv2.imshow("Brightened image", brightened_img)
    elif option == 5:
        cv2.imshow("Image with noise", noisy_img) 
    elif option == 6:
        break

    cv2.waitKey(0)  
    cv2.destroyAllWindows()