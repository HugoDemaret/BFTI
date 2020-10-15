from binascii import *
import math

def imagesize(array):
    pre_imagelength = len(array)
    matrix_size = math.floor(math.sqrt(pre_imagelength+1)) #Makes sure all the characters will fit inside the matrix
    return matrix_size
def imagecreate(array, int):
    matrix_size = int
    image = [[]*matrix_size]*matrix_size # n x n matrix, need to fix the first 3 arrays which are empty
    elements = array
    for element in elements:
        for i in range(matrix_size):
            image.append(element)
    print(image)

def fileopening(int):
    if int == 1:
        file_path = input("Enter your binary file path: ")
        file = open(file_path, "r+")
        lines = file.readlines()
        pre_image = []
        for line in lines:
            line_string = line
            for letter in line_string:
                pre_image.append(letter)
    else:
        file_path = input("Enter your ascii file path: ")
        file = open(file_path, "r+")
        lines = file.readlines()
        pre_image = []
        for line in lines:
            line_string = line
            for letter in line_string:
                ascii_value = a2b_uu(letter) #Converts the caracters from ascii to binary code
                pre_image.append(ascii_value)
    imagecreate(pre_image, imagesize(pre_image))
