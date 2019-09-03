import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time
from functools import reduce
from collections import Counter

# A fucntion to create an array of exmaples to train the 
# image recognition tool
def create_examples():
    number_array_exmaples = open('numArx.txt', 'a')                 # File does not exist at the start of the script
    numbers_we_have = range(0, 10)                                  # Range of characters from 0 to 9
    versions_we_have = range(1, 10)                                 # Number of each example 1 to 9

    for each_num in numbers_we_have:
        for each_version in versions_we_have:
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

def what_num_is_this(file_path):
    matched_array = []                                          # array to store matched examples
    load_examples = open('numArx.txt', 'r').read()              # read in the exmaples array
    load_examples = load_examples.split('\n')                   # split the examples array on new lines

    image = Image.open(file_path)
    image_array = np.array(image)
    image_array_list = image_array.tolist()

    in_question = str(image_array_list)

    for each_example in load_examples:
        if len(each_example) > 3:
            split_example = each_example.split('::')
            current_num = split_example[0]
            current_array = split_example[1]

            each_pixel_example = current_array.split('],')

            each_pixel_in_question = in_question.split('],')

            x = 0

            while x < len(each_pixel_example):
                if each_pixel_example[x] == each_pixel_in_question[x]:
                    matched_array.append(int(current_num))
                x += 1

    print(matched_array)
    y = Counter(matched_array)
    print(y)

what_num_is_this('images/test.png')