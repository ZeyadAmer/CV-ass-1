import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

im = Image.open("Capture.PNG")
image_array = np.array(im)


def CalculateCooccurrence(arr):
    """
    Calculate the Co-occurrence array buy North-South implementation
    ehna benros kol el pixels from smallest to biggest then ben count
    kam mara kol 2 pixels kano north we south leba3d we ben stroe el big matrix da 
    3ashan hanesta3melo lama negy nehseb el contrast
    """
    co_matrix = np.zeros(
        (256, 256))  # ba3mel matrix kebeer kolo zeros we kda kda akbar pixel 256
    rows = len(arr) - 1
    columns = len(arr[0])
    """""
    el columns betkoon el north wel rows betkoon el south 3ashan kda lama hanegy ne store el values el r+1
    hatkoon el ola 3ashan el r+1 da el south 
    """
    for r in range(rows):
        for c in range(columns):
            co_matrix[arr[r][c]-1][arr[r+1][c]-1] += 1

    return co_matrix


def CalculateContrast(arr):
    contrastValue = 0
    rows = len(arr) - 1
    columns = len(arr[0])
    for r in range(rows):
        for c in range(columns):
            if (c-r != 0):
                contrastValue += (arr[r][c] * ((c+1)-(r+1)) / ((c+1)-(r+1)))

    return contrastValue


def CalculateHistogram(arr):
    """
    to calculate the 1d histogram array you need to calculate the occurence of each pixel
    so we will define an empty 1d array with 256 size the max number of pixels and count
    """
    histo_matrix = np.zeros((256))
    rows = len(arr)
    columns = len(arr[0])
    for r in range(rows):
        for c in range(columns):
            histo_matrix[arr[r][c]-1] += 1

    return histo_matrix
# Example usage:


my_2d_array = [[5, 5, 7, 8, 8], [8, 6, 8, 8, 6], [
    8, 7, 8, 7, 6], [9, 8, 200, 200, 5], [9, 8, 9, 7, 2]]

histo = CalculateHistogram(my_2d_array)

print(histo)
