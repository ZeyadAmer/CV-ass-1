import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

im = Image.open("ghost+1.png").convert('L')
image_array = np.array(im)
# print(image_array)
# im.show()


# task 1


def CalculateCooccurrence(arr):
    """
    Calculate the Co-occurrence array buy North-South implementation
    ehna benros kol el pixels from smallest to biggest then ben count
    kam mara kol 2 pixels kano north we south leba3d we ben stroe el big matrix da 
    3ashan hanesta3melo lama negy nehseb el contrast
    """
    co_matrix = np.zeros(
        (256, 256),dtype=int)  # ba3mel matrix kebeer kolo zeros we kda kda akbar pixel 256
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
    up = 0
    down =0
    rows = len(arr) -1
    columns = len(arr[0])
    for r in range(rows):
        for c in range(columns):
            if (r-c != 0):
                up += ((arr[r][c]) * (abs(r-c)))
                down += (abs(r-c))
    contrastValue = up / down


    return contrastValue


# task 2


def CalculateHistogram(arr):
    """
    to calculate the 1d histogram array you need to calculate the occurence of each pixel
    so we will define an empty 1d array with 256 size the max number of pixels and count
    """
    histo_matrix = np.zeros((256),dtype=int)
    rows = len(arr)
    columns = len(arr[0])
    for r in range(rows):
        for c in range(columns):
            histo_matrix[arr[r][c]-1] += 1

    return histo_matrix


def CalculateCumulativeHistogram(arr):
    """
    to calculate the cumulative histogram hane3mel new 1d matrix bel max bardo
    hane3mel temp ne store fe el value we ne add kol index 
    """
    Cum_matrix = np.zeros((256),dtype=int)
    cumulative = 0
    for m in range(len(arr)):
        cumulative += arr[m]
        if (arr[m] != 0):
            Cum_matrix[m] = cumulative
    return Cum_matrix


def GetColorAtPercentage(arr, percentage):
    # Find the indices that correspond to the given percentage
    lower_percentage = np.max(arr) * percentage / 100
    upper_percentage = np.max(arr) - lower_percentage

    lower_index = np.argmax(arr >= lower_percentage)
    upper_index = np.argmax(arr >= upper_percentage)

    lower_intensity = lower_index + 1
    upper_intensity = upper_index + 1

    return lower_intensity, upper_intensity

# task 3

def StretchContrast(arr, a, b, c, d):
    stretched_image = arr.copy()
    scaling_factor = (b - a) / (d - c)
    
    rows = len(arr)
    columns = len(arr[0])
    for r in range(rows):
        for o in range(columns):
            pixel_value = arr[r][o]
            new_pixel_value = int(((pixel_value - c) * scaling_factor) + a)
            stretched_image[r][o] = np.array(new_pixel_value)
    stretched_image = Image.fromarray(stretched_image)
    stretched_image.show()

    
    return stretched_image

def EqualizedHistogram(arr,a,b):

    hist = CalculateHistogram(arr)
    cdf = hist.cumsum()
    cdf_normalized = ((cdf - cdf.min()) * (b-a)) / (cdf.max() - cdf.min()) 
    equalized_image = cdf_normalized[arr].astype(np.uint8)
    image = Image.fromarray(equalized_image)
    image.show()
    return image


def GrayScaleTransformation(arr, x1, y1, x2, y2):
        transformed = arr.copy()
        rows = len(arr)
        columns = len(arr[0])
        for r in range(rows):
            for o in range(columns):
                pixel_value = arr[r][o]
                if(pixel_value < x1):
                    new_pixel_value= pixel_value * (y1/x1)
                elif ( pixel_value < x2):
                    new_pixel_value= ((pixel_value-x1)*((y2-y1)/(x2-x1)))+y1
                elif ( x2< pixel_value): 
                    new_pixel_value= ((pixel_value-x2)* ((255-y2)/(255-x2)))+ y2
                elif(pixel_value-x2 == 0):
                    new_pixel_value = y2
                transformed[r][o] = np.array(new_pixel_value,dtype=int)
        transformed = Image.fromarray(transformed)
        transformed.show()
        return transformed

# Example usage:


my_2d_array = [[5, 5, 7, 8, 8], [8, 6, 8, 8, 6], [
    8, 7, 8, 7, 6], [9, 8, 200, 200, 5], [9, 8, 9, 7, 2]]

# task 1
# print(CalculateCooccurrence(image_array))
# print(CalculateContrast(CalculateCooccurrence(image_array)))


# task 2
histo = CalculateHistogram(image_array)
# cumm = CalculateCumulativeHistogram(histo)
# bakh = GetColorAtPercentage(cumm, 10)
# print(histo)
# Plot the histogram
# plt.bar(range(256), histo)
# plt.title("Histogram1")
# plt.xlabel("Pixel Value")
# plt.ylabel("Frequency")
# plt.show()
# print(cumm)
# print(bakh)


#task 3

# test = StretchContrast(image_array,0,255,88,151)
# image_arrayout = np.array(test)
# histoout= CalculateHistogram(image_arrayout)

# plt.bar(range(256), histoout)
# plt.title("Histogram2")
# plt.xlabel("Pixel Value")
# plt.ylabel("Frequency")
# plt.show()

test2 = EqualizedHistogram(image_array,0,255)
image_arrayout2 = np.array(test2)
histoout2= CalculateHistogram(image_arrayout2)

plt.bar(range(256), histoout2)
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()


# test3 = GrayScaleTransformation(image_array,88,5,151,250)
# image_arrayout3 = np.array(test3)
# print(image_arrayout3)
# histoout3= CalculateHistogram(image_arrayout3)

# plt.bar(range(256), histoout3)
# plt.title("Histogram")
# plt.xlabel("Pixel Value")
# plt.ylabel("Frequency")
# plt.show()

