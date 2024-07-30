# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:50:05 2023

@author: Asus
"""
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['figure.figsize'] = [16,8]

A = imread('Toyota_FJ_Cruiser.jpg')#open the image
X = np.mean(A,2);#convert RGB to grayscale

img = plt.imshow(X)#show image
img.set_cmap('gray')
plt.axis('off')
plt.show()

U , Sigma , VT = np.linalg.svd(X,full_matrices=False)
Sigma=np.diag(Sigma)

j=0
for r in(5,20,100):
    #construct approximate image
    Xapprox=U[:,:r] @ Sigma[0:r,:r] @ VT[:r,:]
    plt.figure(j+1)
    j+=1
    img=plt.imshow(Xapprox)
    img.set_cmap('gray')
    plt.axis('off')
    plt.title('r='+str(r))
    plt.show()
    