# TODO: you will need to install cv2
# Run "pip3 install opencv-python" in CLI
import cv2
import sys
# Kaleidoscope requires numpy. Uncomment this line and install it if you need to.
import numpy as np


# Store command line arguments in variables
# TODO: change the next line to store the filename
filename = sys.argv[1]
manip = sys.argv[2]

# Open the image file
img = cv2.imread('../' + filename)
# Get the dimensions (in pixels) of the image
dimensions = img.shape
# Copy the original image into an image for manipulation
img_manip = cv2.resize(img, (dimensions[1], dimensions[0]))
# TODO: Store white in a list, where each of the three parts is on a scale of [0, 255]
white = [255,255,255]
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        if manip == 'flip':
            img_manip[x, y] = img[dimensions[0]-1-x, y]
        elif manip == 'mirror':
            # TODO: mirror the image and store in img_manip[x, y]
            img_manip[x, y] = img[x, dimensions[1]-1-y]
        elif manip == 'invert':
            # TODO: invert the image and store in img_manip[x, y]
            # Hint: img[x, y] returns the color of the pixel at that coordinate.
            # You can invert by subtracting that color from white.
            img_manip[x, y] = [255 - img[x,y][0], 255 - img[x, y][1],255 - img[x, y][2]]

# Displays the original image in the top left corner of the screen.
image = 'Original image'
cv2.namedWindow(image)
cv2.moveWindow(image, 0, 0)
cv2.imshow(image, img)
# TODO: Display the manipulated image alongside the original image.
new_image = 'Manipulated Image'
cv2.namedWindow(new_image)
cv2.moveWindow(new_image, 0, 25)
cv2.imshow(new_image, img_manip)


# TODO: Create a kaleidoscope image, display it, and save it to a file.
# This line puts two images side-by-side in one window.
flip = cv2.resize(img, (dimensions[1], dimensions[0]))
mirror = cv2.resize(img,(dimensions[1], dimensions[0]))
both = cv2.resize(img, (dimensions[1], dimensions[0]))
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        flip[x,y] = img[dimensions[0]-1-x, y]
        mirror[x,y] = img[x, dimensions[1]-y-1]
        both[x,y] = img[dimensions[0]-1-x, dimensions[1]-y-1]

# Note: you will need multiple concatenations to form the complete kaleidoscope image.
left_kal_side = np.concatenate((img, flip), axis=0)
right_kal_side = np.concatenate((mirror, both), axis=0)
whole_kal = np.concatenate((left_kal_side, right_kal_side),axis=1)

# TODO: Show the image
whole_kal_img = 'Kaleidoscope Image'
cv2.namedWindow(whole_kal_img)
cv2.moveWindow(whole_kal_img,0,50)
cv2.imshow(whole_kal_img,whole_kal)

# TODO: Save the image using the imwrite method from cv2
cv2.imwrite("kaleidoscope_result.jpg", whole_kal)


# Infinite loop to keep the windows open until the escape key is pressed.
while True:
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        exit()

