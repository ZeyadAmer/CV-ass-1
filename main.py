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
    co_matrix = np.zeros((256, 256)) #ba3mel matrix kebeer kolo zeros we kda kda akbar pixel 256
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
    contrastValue= 0
    rows = len(arr) - 1 
    columns = len(arr[0])
    for r in range(rows):
        for c in range(columns):
            if(c-r != 0):
                 contrastValue += (arr[r][c] * ((c+1)-(r+1)) / ((c+1)-(r+1)))
            
    return contrastValue

# Example usage:

my_2d_array = [[1, 2, 3,4 ],[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
final = CalculateCooccurrence(my_2d_array)
answer = CalculateContrast(final)
print(final)
print(answer)