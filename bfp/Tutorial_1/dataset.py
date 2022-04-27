import pandas as pd
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
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


class DataSet:
    def __init__(self):
        self.__dataframe = None
        self.__filename = None
        self.__predictions = None

        # This could have been put in a setter method, but for now I just
        # stuck it in the init method.
        self.__models = [
            ('LR', LogisticRegression(solver='liblinear', multi_class='ovr')),
            ('LDA', LinearDiscriminantAnalysis()),
            ('KNN', KNeighborsClassifier()),
            ('CART', DecisionTreeClassifier()),
            ('NB', GaussianNB()),
            ('SVM', SVC(gamma='auto')),
        ]

    '''
    Methods
    '''
    def from_csv(self, filename, names=None):
        self.__dataframe = pd.read_csv(filename, names=names)
        self.__filename = filename

    def box_plot(self, subplots, layout, sharex, sharey):
        self.__dataframe.plot(
            kind="box", 
            subplots=subplots, 
            layout=layout, 
            sharex=sharex,
            sharey=sharey)

    def histogram(self):
        self.__dataframe.hist()

    def scatter_matrix_plot(self):
        scatter_matrix(self.__dataframe)

    def show_plot(self):
        pyplot.show()

    def split_test_train(self, index):
        array = self.__dataframe.values
        # Data
        X = array[:, 0:index]
        # Names
        Y = array[:, index]
        return train_test_split(
            X, 
            Y, 
            test_size=0.20, 
            random_state=1)

    def model_comparison(self, X_train, Y_train):
        results = []
        names = []
        for name, model in self.__models:
            k_fold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
            cv_results = cross_val_score(model, X_train, Y_train, cv=k_fold, scoring='accuracy')
            results.append(cv_results)
            names.append(name)
            print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

        pyplot.boxplot(results, labels=names)
        pyplot.title("Algorithm Comparison")
        pyplot.show()

    def create_predictions(self, X_train, Y_train, X_validation):
        model = SVC(gamma='auto')
        model.fit(X_train, Y_train)
        self.__predictions = model.predict(X_validation)

    def evaluate_predictions(self, Y_validation):
        print(accuracy_score(Y_validation, self.__predictions))
        print(confusion_matrix(Y_validation, self.__predictions))
        print(classification_report(Y_validation, self.__predictions))

    '''
    Properties
    '''
    @property
    def dataframe(self):
        return self.__dataframe

    @property
    def filename(self):
        return self.__filename

    @property
    def array(self):
        return self.__dataframe.values

    @property
    def models(self):
        return self.__models


def main():
    # Initialize dataset and populate it.
    chump_dataset = DataSet()

    filename = "iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    chump_dataset.from_csv(filename, names=names)

    # Box Plot
    chump_dataset.box_plot(subplots=True, layout=(2,2), sharex=False, sharey=False)
    chump_dataset.show_plot()

    # Histograms
    chump_dataset.histogram()
    chump_dataset.show_plot()

    # Scatter plot matrix
    chump_dataset.scatter_matrix_plot()
    chump_dataset.show_plot()

    # This breaks this all up into training data, and data to validate against.
    X_train, X_validation, Y_train, Y_validation = chump_dataset.split_test_train(4)

    # Evaluate each model in turn. I.E., we want to find the most accurate model to use.
    chump_dataset.model_comparison(X_train, Y_train)

    # Make predictions on validation dataset
    chump_dataset.create_predictions(X_train, Y_train, X_validation)

    # Evaluate predictions
    chump_dataset.evaluate_predictions(Y_validation)

main()