# This script crops RGB image into small ones with less background
# Please put the file in the directory with images
import os
from PIL import Image
import glob
import errno


# create a directory to store output data
# current is the working directory
def createDir(current):
    outputPath = current + '/output'
    success = False  # indicate if the directory is successfully found or created
    try:
        os.mkdir(outputPath)
        success = True
    except errno.EACCES and FileExistsError:
        if not os.path.exists(outputPath):
            print('Program does not have access to create a directory\n'
                  'Please create a directory called \'output\'')
            success = False
        else:
            success = True
    return outputPath, success


def cropping(imageName, outputPath):
    outputPath = outputPath + f'/{imageName}'
    imageFile = Image.open(imageName)
    left = 627
    top = 1400
    right = 1427
    bottom = 2362
    cropped = imageFile.crop((left, top, right, bottom))
    cropped.save(outputPath)


def main():
    currentPath = os.getcwd()
    outputDir, success = createDir(currentPath)
    if success is False:
        return
    files = glob.glob('*.png')
    for eachFile in files:
        cropping(eachFile, outputDir)


if __name__ == '__main__':
    main()
