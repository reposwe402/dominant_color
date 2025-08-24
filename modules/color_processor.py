import numpy as np


def find_dominant_colors(img, top_n=3):
    array = np.array(img)
    unique, counts = np.unique(array, return_counts=True)
    occurrence = dict(zip(unique, counts))
    sorted_keys = sorted(occurrence, key=occurrence.get, reverse=True)
    return sorted_keys[:top_n]


def create_color_image(color, size=(300, 300, 3)):
    image = np.zeros(size, np.uint8)
    image[:] = color
    return image
