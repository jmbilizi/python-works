# %%
# imports
from PIL import Image
import numpy as np
import csv
import matplotlib.pyplot as plt

# %%
# load data
# Read pixel values from the CSV file into a numpy array
csv_filename = './ASLData/User1/291982754_alphabet_a_right.csv'  # Replace with your CSV file name
pixel_values = []

with open(csv_filename, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        pixel_values.append([round(float(val)) for val in row])

# Convert the list of pixel values to a numpy array
pixel_array = np.array(pixel_values, dtype=np.uint8)

type(pixel_array)
# %%
# show the numpy array of pixel_array values
pixel_array
# %%
# preview the image
plt.imshow(pixel_array)
# %%
