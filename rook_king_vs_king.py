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

from sklearn.model_selection import cross_val_score

from sklearn.model_selection import GridSearchCV

dataset = "datasets/chess.csv"

df = pd.read_csv(dataset)


columns_to_encode = ['white_king_file', 'white_rook_file', 'black_king_file']
y_value = "result"


df = pd.get_dummies(data=df, columns=columns_to_encode)
df = df.sample(frac=1)

n_samples = df.shape[0]

train_size = int(n_samples *0.7)
test_size = n_samples - train_size

df_X = df.drop('result', axis=1)
df_y = df['result']



train_X = df_X[:train_size]
train_y = df_y[:train_size]

test_X = df_X[train_size:]
test_y = df_y[train_size:]

training = []
testing = []

#max_depth = [1]

#DecisionTreeClassifier
#criterion="entropy", max_depth=100, min_samples_split=2, min_samples_leaf=1
#~80%

#KNeighborsClassifier
#n_neighbors=15, algorithm="kd_tree", p=1
#~68%

#RandomForestClassifier
#criterion="entropy", max_depth=100, min_samples_split=3
#~67%

dt_params = [
    {
        "max_depth": [100, 200, 500, 1000, 2000, 3000, 5000, None],
        "criterion": ["entropy", "gini"],
        "min_samples_split": [2, 3, 4, 5, 10],
    }
]

rf_params = [
    {
        "max_depth": [100, 200, 500, 1000, 2000, 3000, 5000, None],
        "criterion": ["entropy", "gini"],
        "min_samples_split": [2, 3, 4, 5, 10],
    }
]

knn_params = [
    {
        "n_neighbors": [2, 3, 4, 5, 10, 12, 15],
        "p": [1, 2],
        "algorithm": ["ball_tree", "kd_tree"]
    },
]

results = []
#for depth in max_depth:
classifier = DecisionTreeClassifier(criterion="entropy", max_depth=100, min_samples_split=2, min_samples_leaf=1)

#dt_experimenter = GridSearchCV(classifier, dt_params, cv=5)
#dt_experimenter.fit(train_X, train_y)
classifier.fit(train_X, train_y)

#print("Best parameter set found: ")
#print(dt_experimenter.best_params_)


#knn_model = KNeighborsClassifier()
#knn_exp = GridSearchCV(knn_model, knn_params, cv=5)

#knn_exp.fit(train_X, train_y)

#print("Best parameter set found: ")
#print(knn_exp.best_params_)


    #scores = cross_val_score(classifier, train_X, train_y, cv=5)
    #print(scores)
#results = classifier.predict(test_X)
   

train_acc = classifier.score(train_X, train_y)
test_acc = classifier.score(test_X, test_y)



print("Train:", train_acc)
print("Test", test_acc)


# Create confusion matrix
'''
nn_best_preds = dt_experimenter.predict(test_X)
nn_conf_mat = confusion_matrix(test_y, nn_best_preds)

sns.heatmap(nn_conf_mat, square=True, annot=True, cbar=False)
plt.xlabel('Predicted label')
plt.ylabel('Actual label')
'''
#training = classifier.predict(train_X)
#testing = classifier.predict(test_X)

#print(test_X)
#for x in range(10):
 	#print(results[x])
  
#print(test_y)