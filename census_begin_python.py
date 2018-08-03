# Numerical library in python, gives us nice things like special kinds of arrays,
# useful math functions, random numbers, etc.
import numpy as np

# Pandas library gives us Series data and DataFrames, which are two really useful ways
# of representing data. Using pandas, we can easily filter, sort, or extract data.
# Very easy to convert this data into native numpy or native Python objects.
import pandas as pd

# Matplotlib is a standard library used in Data Science,
# especially pyplot
#import matplotlib.pyplot as plt

# Scikit-learn includes everything we need to take our data and run Supervised Learning
# or Unsupervised Learning algorithms on it.
import sklearn

# Import our Naive Bayes Classifier
from sklearn.naive_bayes import GaussianNB

# Import our Neural Network Classifier (Multi-Layer Perceptron Classifier)
from sklearn.neural_network import MLPClassifier

# Import our KNN Classifier
from sklearn.neighbors import KNeighborsClassifier

# Import our Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

# Import our Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

# Import our Support Vector Machine Classifier
from sklearn.svm import SVC

# We'll use this at the end for evaluating our models
from sklearn.metrics import confusion_matrix

# Use this new cleaned up dataset.
dataset = "datasets/full_census.csv"

# We can read in a properly formatted CSV using this helper function.
# This reads it in as a pandas dataframe object, which gives us a lot
# of the same functionality we get in Excel like filtering, sorting, etc
df = pd.read_csv(dataset)

# This head() function gives us the first 5 items, which Jupyter notebook
# formats nicely for us.
df.head()

# We can also use the describe function on a dataframe to get info on the categorical variables
df.describe()


cols = []
y_value = " wealth_class"

cols = [' workclass', ' education', ' education-num', ' marital-status', ' occupation', 
        ' relationship', ' sex', ' race', ' capital-gain', ' capital-loss', ' hours-per-week', ' native-country', 
          ]

df = pd.get_dummies(data=df, columns=cols)

# This is how many examples we have.
n_samples = df.shape[0]
print(n_samples)

# TODO: Compute train_size and test_size
train_size = int(n_samples * 0.70)
test_size = n_samples - train_size

print("Training set size: {}".format(train_size))
print("Test set size: {}".format(test_size))


df_X = df.drop(y_value, axis=1)
#df_X = x.drop(" fnlwgt", axis=1)
df_y = df[y_value]

# We need to now create our test and train splits

# We'll train on 70% of our data
train_X = df_X[:train_size]
train_y = df_y[:train_size]
# The remaining samples are for our test set

test_X = df_X[train_size:]
test_y = df_y[train_size:]


epoch_counts = [1] # We'll loop over this and set the MLP max iterations to this
classifiers = [] # Append your classifiers here after applying .fit() to them

train_accs = [] # Append train accuracies here
test_accs = [] # Append test accuracies here
results = []

predictions = []

for epoch_count in epoch_counts:
    # TODO: Use the epoch_count variable here, refer to MLP docs
    classifier = KNeighborsClassifier()
    # TODO: Use the fit() function here
    classifiers.append(classifier.fit(train_X, train_y))
    # TODO: Compute the accuracies below
    train_error = classifier.score(train_X, train_y)
    test_error = classifier.score(test_X, test_y)

    predictions = classifier.predict(train_X)
    results = classifier.predict(test_X)
    
    #results.append(classifier.predict(test_X))
    train_acc = train_error
    test_acc = test_error
    print("Train:", train_acc)
    print("Test", test_acc)
    train_accs.append(train_acc)
    test_accs.append(test_acc)
    
    # Now let's plot the results
print(test_X)
for x in range(10):
  print(results[x])
  
print(test_y)
'''
for result in predictions:
  if result != " Black":
    print(result)

for result in results:
  if result != " Black":
    print(result)
'''
print("done")   

#plt.plot(epoch_counts, train_accs, "g")
#plt.plot(epoch_counts, test_accs, "r")