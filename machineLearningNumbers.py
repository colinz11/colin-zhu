# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, and performance metrics
from sklearn import datasets, metrics

# Import the Multi-Layer Perceptron Classifier. This is the model we will train.
from sklearn.neural_network import MLPClassifier

# This is a seed for the random number generator, we set this to make
# reproducible results
seed = 42

# The handwritten digits dataset
digits = datasets.load_digits()

# The data that we are interested in is made of 8x8 images of digits, let's
# have a look at the first 4 images, stored in the `images` attribute of the
# dataset.  If we were working from image files, we could load them using
# matplotlib.pyplot.imread.  Note that each image must have the same size. For these
# images, we know which digit they represent: it is given in the 'target' of
# the dataset.
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

# Each image right now is a 20 x 20 matrix of grayscale pixel values
# Here we print the first image's pixel values.
print(digits.images[0])


# To apply a classifier on this data, we need to flatten the image, to# To ap 
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
print(n_samples)

# Data is a list of vectors now, each vector is length 400, since the image dimensions are 20 x 20.
data = digits.images.reshape((n_samples, -1))

# We need to now create our test and train splits

# We'll train on 70% of our data
train_size = int(n_samples * 0.70)
train_X = data[:train_size]
train_y = digits.target[:train_size]
print(len(train_X))

# The remaining samples are for our test set
test_size = n_samples - train_size
test_X = data[train_size:]
test_y = digits.target[train_size:]
print(len(test_X))

assert n_samples == (len(test_X) + len(train_X))


# Now, we initialize a classifier object and fit it to our training set# Now,  
# TODO: Look at docs and add additional params here to try to increase
# accuracy after you go through the demo end-to-end.
classifier = MLPClassifier(random_state=seed, shuffle=True, learning_rate="constant", max_iter=10000, warm_start=False, hidden_layer_sizes=(10000))


# This fit() function is how we train the classifier
classifier.fit(train_X, train_y)


# Now that we've finished training, get the test and train errors.
print("==================== AFTER TRAINING ====================")

train_error = classifier.score(train_X, train_y)
print("Train Accuracy: {}".format(train_error))

test_error = classifier.score(test_X, test_y)
print("Test Accuracy: {}".format(test_error))

# Allow the classifier to make predictions on the test set using only the 
# features, not the labels
predicted = classifier.predict(test_X)

# TODO: Look up what precision, recall, and f1-score are.
# Explain why recall for 3 and 8 might be so low.
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(test_y, predicted)))

# TODO: Try to interpret what this might be.
print("Confusion matrix:\n%s" % metrics.confusion_matrix(test_y, predicted))



# It's nice to see visual representation of the results# It's n 
images_and_predictions = list(zip(digits.images[train_size:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)


# If you're running this outside of Jupyter notebook,# If you 
# uncomment this next line.
plt.show()