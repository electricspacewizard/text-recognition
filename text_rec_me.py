import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time
from functools import reduce

# A fucntion to create an array of exmaples to train the 
# image recognition tool
def create_examples():
    number_array_exmaples = open('numArx.txt', 'a')                 # File does not exist at the start of the script
    numbers_we_have = range(0, 10)                                  # Range of characters from 0 to 9
    versions_we_have = range(1, 10)                                 # Number of each example 1 to 9

    for each_num in numbers_we_have:
        for each_version in versions_we_have:
            #print(str(each_num) + '.' + str(each_version))
            image_file_path = 'images/numbers/' + str(each_num) + '.' + str(each_version) + '.png'
            example_image = Image.open(image_file_path)                       # open each image
            example_image_array = np.array(example_image.getdata())               # create an array of images
            example_image_array1 = str(example_image_array.tolist())    # convert the array to list
            line_to_write = str(each_num) + '::' + example_image_array1 + '\n'
            number_array_exmaples.write(line_to_write)

create_examples()



# A function to turn an image to black and white so its easier
# for the character recognition to see patterns in characters
def threshold(image_array):
    balance_array = []                                              # varaible to find the avaerage colour of the array and determine whether it is black or white
    new_array = image_array

    for each_row in image_array:
        for each_pixel in each_row:
            average = reduce(lambda x, y: int(x) + int(y), each_pixel[:3])/len(each_pixel[:3])                # lambda function to average the pixels         
            balance_array.append(average)
    balance = reduce(lambda x, y: int(x) + int(y), balance_array)/len(balance_array)  
    for each_row in new_array:
        for each_pixel in each_row:
            if reduce(lambda x, y: int(x) + int(y), each_pixel[:3])/len(each_pixel[:3]) > balance:
                each_pixel[0] = 255
                each_pixel[1] = 255
                each_pixel[2] = 255
                each_pixel[3] = 255
            else:
                each_pixel[0] = 0
                each_pixel[1] = 0
                each_pixel[2] = 0
                each_pixel[3] = 255
    return new_array

i1 = Image.open('images/numbers/0.1.png')
image_array1 = np.array(i1)                                       # turn the image pixels into arrays

i2 = Image.open('images/numbers/y0.4.png')
image_array2 = np.array(i2)                                       # turn the image pixels into arrays

i3 = Image.open('images/numbers/y0.5.png')
image_array3 = np.array(i3)                                       # turn the image pixels into arrays

i4 = Image.open('images/sentdex.png')
image_array4 = np.array(i4)                                       # turn the image pixels into arrays




"""
threshold(image_array1)
threshold(image_array2)
threshold(image_array3)
threshold(image_array4)

fig = plt.figure()                                                  # create a figure to plot 4 exmaple numbers
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)          # create positions of the subplots
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)      
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)      
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)      

ax1.imshow(image_array1)                                            # place image arrays on subplots
ax2.imshow(image_array2)
ax3.imshow(image_array3)
ax4.imshow(image_array4)

plt.show()
"""