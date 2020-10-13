from binascii import *

def imagecreator(array):
    pre_imagelength = len(array)
    i = pre_imagelength // 2
    print(array)
    print("preimagelength = ", pre_imagelength)
    print("i = ", i)


def fileopening(int):
    if int == 1:
        file_path = input("Enter your binary file path: ")
        file = open(file_path, "r+")
        lines = file.readlines()
        for line in lines:
            line_string = line
            pre_image = []
            for letter in line_string:
                pre_image.append(letter)
    else:
        file_path = input("Enter your ascii file path: ")
        file = open(file_path, "r+")
        lines = file.readlines()
        for line in lines:
            line_string = line
            pre_image = []
            for letter in line_string:
                ascii_value = a2b_uu(letter) #Convert the caracters from ascii to binary code
                pre_image.append(ascii_value)
    imagecreator(pre_image)
