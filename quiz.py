import pandas as pd 
import csv
import numpy

#Open files
data_train_file = pd.read_csv('gameratings.csv')
data_test_file = pd.read_csv('test_esrb.csv')

#Split into train and test
data_train = data_train_file.T.loc['console':'violence']
target_train = data_train_file.T.loc['Target']
data_test = data_test_file.T.loc['console':'violence']
target_test = data_test_file.T.loc['Target']

#Transpose to match shape
data_train = data_train.T
data_test = data_test.T

'''
#check shapes
print(data_train.shape)
print(data_test.shape)

print(target_train.shape)
print(target_test.shape)
'''

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()


#assign X and y
X=data_train
y=target_train
y=y.astype('int')

#Train model
knn.fit(X, y)

#Predict values
predicted = knn.predict(X=data_test)


#Make array of titles (gets rid of index values)
titles = data_test_file.T.loc['title']
titles = titles.to_numpy()

#Assign rating numbers to corresponding codes
rating_codes = {1: 'Everyone', 2:'Everyone 10+', 3:'Mature', 4:'Teen'}

#Write game titles and ratings to csv file 
with open('Video Game Predicted Ratings.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["title", "prediction"])  
    for x, y in zip(titles, predicted):
        for key in rating_codes:
            if y == key:
                y = rating_codes[key]
                writer.writerow([x, y])


#IGNORE: Unnecessary attempt to figure out how find wrong values
'''
target_test=target_test.astype('int')
target_test = target_test.to_numpy()
expected = target_test
print(expected[:5])

print(format(knn.score(data_test, target_test), ".2%"))

wrong = [(p,e) for (p,e) in zip(predicted, expected) if p != e]
print(wrong)
'''