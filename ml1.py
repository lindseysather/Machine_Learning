from sklearn.datasets import load_digits

#digits dataset is a BUNCH OBJECT
# 3 attributes we care about:
#   1. digits.data  1797, 64
#   2. digits.target    1797
#   3. digits.images

digits = load_digits()
'''
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

#plt.show()

#iterating through the subplots (ravel), images, and targets at the same time
#ravel makes 2D into 1D (makes 1 row of 24 rather than 4x6)
for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    #sets tick marks to empty - no lines
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)

plt.tight_layout()
#plt.show()
'''

from sklearn.model_selection import train_test_split

#split data into training and testing (75% into training)
#normally don't need random_state (just for testing in class)
data_train, data_test, target_train, target_test = train_test_split(
    digits.data, digits.target, random_state=11
)

print(data_test[:10])
print(target_test[:10])
'''
#2D
print(data_train.shape)
print(data_test.shape)

#1D
print(target_train.shape)
print(target_test.shape)
'''

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

#notice x is uppercase, y is lowercase
#fit is the algorithm that does all the machine learning 
    #needs the data and the target
    #training the model
    #tells what data matches up with each target
knn.fit(X=data_train, y=target_train)

#print(data_train)
#print(target_train)


#predict will tell you the answer  (an array of all the targets)
predicted = knn.predict(X=data_test)
expected = target_test
#predicted and expected should match up - proves that the algorithm has learned and is working correctly

#print(predicted[:20])
#print(expected[:20])

#Tells you how well it does - how much the predicted matches up with expected (97.78%)
print(format(knn.score(data_test, target_test), ".2%"))

#prints wrong predictions - gets 10 wrong of the 450
wrong = [(p,e) for (p,e) in zip(predicted, expected) if p != e]
print(wrong)

'''
#CONFUSION MATRIX
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion)


#Heat Map
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt2

confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))

figure = plt2.figure(figsize=(7,6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt2.cm.nipy_spectral_r)

plt2.show()


'''
