import os
import sys

import cv2
import numpy as np
from PIL import Image

import apriltag

# credential_path = "/Users/Lucas/Apps/Web/mathther-chefs/python/config/google_client_secrets.json"
dirname = os.path.dirname(__file__)
credential_path = os.path.join(dirname, '../../../config/google_client_secrets.json')
credential_path = os.path.abspath(credential_path)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def corner_finder(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    #Find Image Size

    # path = sys.argv[1]
    im = Image.open(path)

    x_width = im.size[0]
    y_height = im.size[1]

    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    #print('Number of objects found: {}'.format(len(objects)))
    x_coords = []
    y_coords = []
    coords_list =[]
    for object_ in objects:
       # print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
     #       print(' - ({}, {})'.format(vertex.x, vertex.y))
            x_coords.append(vertex.x)
            y_coords.append(vertex.y)



    x_coords = [x_width * i for i in x_coords]
    y_coords = [y_height * i for i in y_coords]

    for n in range(0,len(x_coords)):
        coords_list.append([x_coords[n],y_coords[n]])

    coords = open('coords.txt', 'w')
    coords.writelines(["%s\n" %item for item in coords_list])
    #print(x_coords)
    #print(y_coords)
    d1 = ( (x_coords[1] - x_coords[0])** 2 + (y_coords[1] - y_coords[0])**2)**(0.5)
    d2 = ( (x_coords[2] - x_coords[1])** 2 + (y_coords[2] - y_coords[1])**2)**(0.5)
    # imgBox = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
    # cv2.line(imgBox,(int(x_coords[0]),int(y_coords[0])),(int(x_coords[1]),int(y_coords[1]),(0,0,0),15)
    # cv2.imshow('image', imgBox)
    # cv2.waitKey(0)
    # print(d1,d2)
    # SA = d1 * d2
    # print(SA)
    # return SA
    f = open('/Users/Lucas/Apps/Web/mathther-chefs/python/assets/lengthFinder/python/lengthPerPixelInMetres.txt','r')
    lengthperpixel = f.read()

    SA = d1 * d2 *float(lengthperpixel) * float(lengthperpixel)
    return SA
