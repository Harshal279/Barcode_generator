import numpy as np 
import cv2 
num = 456564465405465
binary = (bin(num)[2:])
print(binary)
bin_str = str (binary)
img = np.ones((700, 700, 3), dtype = "uint8") *225 
a=0
for n in bin_str :
    start = (100 + a ,50)
    end = (100 + a ,300)
    if (n=='0') :
        cv2.line(img, start, end, (0, 0, 0), 2)
    else :
        cv2.line(img, start, end, (225, 225, 225), 2)
    a = a + 3
cv2.imshow('dark', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 