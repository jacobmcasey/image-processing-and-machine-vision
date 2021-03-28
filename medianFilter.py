#Jacob Casey
#Code to implement median filter by a 3x3 filter on hardcoded numpy array


import cv2
import numpy as np 

#2d array to represent an image with pixels
""" arr = np.array([[5, 5, 6, 7,  8, 8],
                [5, 5, 6, 7,  8, 8],
                [0, 0, 6, 7,  8, 8],
                [5, 5, 6, 15, 8, 8],
                [5, 5, 6, 7,  8, 8],
                [5, 5, 6, 7,  8, 8]]) """

arr = [[1,2,3],[1,2,3],[1,2,3]]

#Scan Right to left, top to bottom with arr[i][j]
for i in range(len(arr)-1):
    for j in range(len(arr[0])-1):
     arr[i][j] = round((arr[i+1][j+1] + arr[i][j+1] + arr[i][j] + arr[i+1][j] + arr[i-1][j] + arr[i-1][j-1] + arr[i][j-1] + arr[i+1][j-1] + arr[i-1][j+1]) / 9)

print(arr)