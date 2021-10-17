#
# Generate dynamic color image --- futur spec
#

import numpy as np
from PIL import Image
import random

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result

lightcolor = [[230, 176, 170],[215, 189, 226],[169, 204, 227],[162, 217, 206 ],[249, 231, 159], [237, 187, 153],[229, 231, 233 ],[174, 182, 191],[248, 196, 113]]
bgcolorlight = random.choice(lightcolor)

darkcolor = [[123, 36, 28],[99, 57, 116],[26, 82, 118 ],[14, 102, 85 ],[29, 131, 72], [39, 88, 140],[125, 102, 8 ],[147, 81, 22],[81, 90, 90]]
bgcolordark = random.choice(darkcolor)
print(bgcolordark)


array = get_gradient_3d(800, 400, (0,0,0), (bgcolordark[0], bgcolordark[1], bgcolordark[1]), (True, True, True))
Image.fromarray(np.uint8(array)).save('gray_gradient_h.jpg', quality=95)

array = get_gradient_3d(512, 256, (0, 0, 0), (255, 255, 255), (False, True, True))
Image.fromarray(np.uint8(array)).save('gray_gradient_v.jpg', quality=95)