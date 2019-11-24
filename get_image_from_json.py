import json
import os
import glob
import numpy as np
from pprint import pprint as pp


def goTroughJson(fileName):
    result = []
    with open(fileName) as file:
        data = json.load(file)
    for key in data:
        each = data[key]
        result.append(each['filename'])
    return result


if __name__ == '__main__':
    working_dir = os.getcwd()
    files = glob.glob(os.path.join(working_dir, 'json/*.json'))
    # pp(files)
    images = []
    for eachFile in files:
        imagesInEach = goTroughJson(eachFile)
        for eachImage in imagesInEach:
            images.append(eachImage)


