import cv2
import numpy as np

img = cv2. imread( '1.jpg')

largeur,hauteur = 250, 350
pts1 = np. float32([[398,459],[932,542],[92,1170],[960,1327]])
pts2 = np. float32([[0,0],[largeur,0],[0,hauteur],[largeur,hauteur]])
matrice = cv2. getPerspectiveTransform(pts1,pts2)
imgOutput = cv2. warpPerspective(img,matrice,(largeur,hauteur))


cv2. imshow('image',img)
cv2. imshow('output',imgOutput)

cv2. waitKey(0)

