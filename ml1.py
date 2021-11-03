from sklearn.datasets import load_digits

#digits dataset is a BUNCH OBJECT
# 3 attributes we care about:
#   1. digits.data  1797, 64
#   2. digits.target    1797
#   3. digits.images

digits = load_digits()

#print(digits.DESCR)

#tells you pixel intensity of image (64 pixels of an 8x8 image of a number):
#looking at the 5th sample:
print(digits.data[5])
#tells you what the image should be (prints 5 - looks like a 5)
print(digits.target[5])

#0-9 is a number, then it repeats itself with different samples of images (10 is 0, 11 is 1)
#1st row is 0 target, 2nd is 1 target, etc. 


#prints number of rows and columns (rows, columns)
#rows represent each sample, columns are each of the 64 pixels 
print(digits.data.shape)

#only 1 column because it just represents each sample (no intensity)
print(digits.target.shape)



import matplotlib.pyplot as plt 

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))

plt.show()