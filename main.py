#Demaret Hugo
#SoundToImage - 2020
#This program transforms binary files into an image
from FileOpening import *

def main():
    print("Do you want to use an ascii file or a binary file? Conversion will be handled. \n")
    bin_or_not = input("Enter \"binary\" for a binary file and \"ascii\" for an ascii file: ")
    if bin_or_not == 'binary':
        truth = 1
    elif bin_or_not == 'ascii':
        truth = 0
    else:
        print("You have entered the wrong value! Please retry!")
        main()
    fileopening(truth)
main()
