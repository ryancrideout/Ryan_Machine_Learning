from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

'''
Extra credit - turn this into a class.
'''

# Load Dataset
filename = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(filename, names=names)

# # Box and whisker plots
# # Resource on what they are: 
# # https://www.simplypsychology.org/boxplots.html#:~:text=In%20descriptive%20statistics%2C%20a%20box,(or%20percentiles)%20and%20averages.
# dataset.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

# # Histograms
# dataset.hist()
# pyplot.show()

# # Scatter plot matrix
# scatter_matrix(dataset)
# pyplot.show()

# Split-out validation dataset
array = dataset.values
# Data
X = array[:, 0:4]
# Names
Y = array[:, 4]
# This breaks this all up into training data, and data to validate against.
# Question - why do we need to do this?
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.20, random_state=1)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto'))) # Most accurate model.

# Evaluate each model in turn. I.E., we want to find the most accurate model to use.
results = []
names = []
for name, model in models:
    k_fold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=k_fold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    # print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# # Compare Algorithms
# pyplot.boxplot(results, labels=names)
# pyplot.title("Algorithm Comparison")
# pyplot.show()

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# Here is the next project?
# https://machinelearningmastery.com/python-machine-learning-mini-course/
# https://www.w3schools.com/python/python_ml_getting_started.asp