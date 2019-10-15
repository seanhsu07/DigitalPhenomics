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
    except Exception or FileExistsError:
        if not os.path.exists(outputPath):
            print('Program does not have access to create a directory\n'
                  'Please create a directory called \'output\'')
            success = False
        else:
            success = True
    return outputPath, success


# def convert(currentPath):
#     yourPath = currentPath
#     for root, dirs, files in os.walk(yourPath, topdown=False):
#         for name in files:
#             print(os.path.join(root, name))
#             if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
#                 if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
#                     print("A jpeg file already exists for %s" % name)
#                 # If a jpeg is *NOT* present, create one from the tiff.
#                 else:
#                     outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
#                     try:
#                         im = Image.open(os.path.join(root, name))
#                         print("Generating jpeg for %s" % name)
#                         im.thumbnail(im.size)
#                         im.save(outfile, "JPEG", quality=100)
#                     except Exception as e:
#                         print(e)


def cropping(imageName, outputPath):
    outputPath = outputPath + f'/{imageName}'
    imageFile = Image.open(imageName)
    imageFile.rotate(180)
    left = 627
    top = 1400
    right = 1427
    bottom = 2362
    cropped = imageFile.crop((left, top, right, bottom))
    cropped = imageFile
    cropped.save(outputPath) #+ f'/{imageName[0:-5]}.png', 'png'


def main():
    currentPath = os.getcwd()
    # convert(currentPath)
    outputDir, success = createDir(currentPath)
    if success is False:
        return
    files = glob.glob('*.tiff')
    for eachFile in files:
        cropping(eachFile, outputDir)


if __name__ == '__main__':
    main()
