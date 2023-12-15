# Install necessary packages
# pip install extcolors
# pip install webcolors

import numpy as np
import cv2
import extcolors 
from PIL import Image
import webcolors
import matplotlib.pyplot as plt

'''
functoins about the represent colors
'''
# pick At least 5 represent colors(rgb) in img
def best5ColorRGB(img):
    colors, pixel_count = extcolors.extract_from_image(img)
    best_rgb = []
    pixel_output = 0
    i = 1

    for c in colors:
        pixel_output += c[1]
        best_rgb.append(c[0])
        # print(f'{c[0]} : {round((c[1] / pixel_count) * 100, 2)}% ({c[1]})')
        i += 1
        if i > 5:
            break
    return best_rgb

# Find a color similar to the Original color
def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2, (g - rgb[1]) ** 2, (b - rgb[2]) ** 2])] = color_name

    num = min(differences.keys())
    return differences[num]
#Convert Color rgb to Color name
def rgb_to_colorname(color):
    try: # if rgb in in 
        cname = webcolors.rgb_to_name(color)
        print(f"The color is exactly {cname}")
    except ValueError:
        cname = closest_color(color)
        print(f"closest color: {cname}")

    return webcolors.name_to_rgb(cname)
#Display colors pallet using plt
def display_colors(colors):
    plt.figure(figsize=(len(colors) * 2, 2))
    for i, color in enumerate(colors):
        plt.subplot(1, len(colors), i + 1)
        plt.imshow([[color]])
        plt.axis('off')
    plt.show()


#main

IMG_PATH = "/image/cyan.jpg"
img_color = cv2.imread(IMG_PATH ) # Load the image in color
print('shape: ', img_color.shape)

height, width = img_color.shape[:2] # Get the height and width of the image
img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) # Convert the image to HSV color space

'''
(1) Show the represent colors pallet & color name
'''
img_pil = Image.fromarray(img_rgb)  # Convert NumPy array to PIL Image
best_rgb = best5ColorRGB(img_pil) # pick At least 5 represent colors in img
num = len(best_rgb)
# Display all colors(origin) pallet in a single plot
print(f"---top {num} colors in image---")
display_colors(best_rgb)
#Find similar colors name 
for i, c in enumerate(best_rgb):
        cname = rgb_to_colorname(c)
'''
(2) Extract a specific color
'''

# Define the HSV range for golden color
color_examples = {
    'blue': ([90, 50, 50], [130, 255, 255]),
    'red': ([0, 50, 50], [10, 255, 255]),
    'green': ([50, 50, 50], [70, 255, 255]),
    'yellow': ([20, 50, 50], [40, 255, 255]),
    'purple': ([140, 50, 50], [170, 255, 255]),
    'orange': ([10, 50, 50], [25, 255, 255]),
    'pink': ([160, 50, 50], [180, 255, 255]),
    'cyan': ([85, 50, 50], [100, 255, 255]),
    'brown': ([8, 50, 50], [20, 255, 255]),
    'gray': ([0, 0, 0], [180, 50, 150])
}

# The color is selected by the user.
print("다음 중 표시할 색상을 선택하세요:")
for i, color in enumerate(color_examples.keys()):
    print(f"{i+1}. {color}")

choice = int(input("번호를 입력하세요: "))
color_choice = list(color_examples.keys())[choice-1]
lower_color = np.array(color_examples[color_choice][0])
upper_color = np.array(color_examples[color_choice][1])

# Create a binary image (mask) based on the golden color range
img_mask = cv2.inRange(img_hsv, lower_color, upper_color)

# Use a binary image to display the part of the original image that corresponds to the selected color.
img_result = cv2.bitwise_and(img_color, img_color, mask=img_mask)

# Display the original image, mask, and the result


cv2.imshow('Original Image', img_color)
cv2.imshow('Binary Image', img_mask)
cv2.imshow('Color Detection Result', img_result)


cv2.waitKey(0)
cv2.destroyAllWindows()
