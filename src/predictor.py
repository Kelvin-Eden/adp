import os
# import pickle
import numpy as np
import pandas as pd
# from scipy.stats import mode
from statistics import mode
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import *
from sklearn.metrics._pairwise_distances_reduction import *
#from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import joblib

proj_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create an object of dataset to be able to get the data
data_path = os.path.join(proj_dir, 'dataset/Training.csv')
# Read the dataset to get data used to train the model
data = pd.read_csv(data_path).dropna(axis=1)
# encode  the values of prognosis
encoder = LabelEncoder()

data['prognosis'] = encoder.fit_transform(data['prognosis'])
# split the data for training and testing the models
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Training the models on whole data
# rf_model = RandomForestClassifier(random_state=18)
# rf_model.fit(X.values, y)
# filename = os.path.join(proj_dir, 'models/random_forest_classifier.pickle')
#
# # save the model
# pickle.dump(rf_model, open(filename, 'wb'))
# # load the model


# ----------------------Testing the model----------------
# Reading the test data

# test_data = pd.read_csv("./dataset/Testing.csv").dropna(axis=1)
#
# test_X = test_data.iloc[:, :-1]
#
# encoder = LabelEncoder()
#
# test_data['prognosis'] = encoder.fit_transform(test_data['prognosis'])
# test_Y = test_data.iloc[:, -1]

# Making prediction by take mode of predictions
# made by all the classifiers

# preds = dt_model.predict(test_X)
#
# score = accuracy_score(test_Y, preds)
#
# print(score)

# try:
#     svm_model = pickle.load(open(os.path.join(proj_dir, 'models/svc_model.pickle'), 'rb'))
#     nb_model = pickle.load(open(os.path.join(proj_dir, 'models/gaussian_naive_bayes.pickle'), 'rb'))
#     rf_model = pickle.load(open(os.path.join(proj_dir, 'models/random_forest_classifier.pickle'), 'rb'))
#     dt_model = pickle.load(open(os.path.join(proj_dir, 'models/decision_tree_model.pickle'), 'rb'))
# except ModuleNotFoundError:


svm_model = joblib.load(os.path.join(proj_dir, 'models/svc_model.sav'))
nb_model = joblib.load(os.path.join(proj_dir, 'models/gaussian_naive_bayes.sav'))
rf_model = joblib.load(os.path.join(proj_dir, 'models/random_forest_classifier.sav'))
dt_model = joblib.load(os.path.join(proj_dir, 'models/decision_tree_classifier.sav'))

# filename_rf = os.path.join(proj_dir, 'models/random_forest_classifier.sav')
# filename_nb = os.path.join(proj_dir, 'models/gaussian_naive_bayes.sav')
# filename_svc = os.path.join(proj_dir, 'models/svc_model.sav')
# filename_dc = os.path.join(proj_dir, 'models/decision_tree_classifier.sav')
#
# svm_model.fit(X.values, y)
# nb_model.fit(X.values, y)
# rf_model.fit(X.values, y)
# dt_model.fit(X.values, y)
#
# joblib.dump(rf_model, filename_rf)
# joblib.dump(svm_model, filename_svc)
# joblib.dump(nb_model, filename_nb)
# joblib.dump(dt_model, filename_dc)


# pickle.dump(svm_model, open(filename, 'wb'))

criteria = X.columns.values

criterion_index = {}

for index, value in enumerate(criteria):
    criterion = " ".join([i.capitalize() for i in value.split("_")])

    criterion_index[criterion] = index

data_dict = {

    "criterion_index": criterion_index,

    "predictions_classes": encoder.classes_
}


def predictDisease(symptoms):
    symptoms = symptoms.split(",")

    # creating input data for the models

    input_data = [0] * len(data_dict["criterion_index"])

    for symptom in symptoms:
        idx = data_dict["criterion_index"][symptom]

        input_data[idx] = 1

    # reshaping the input data and converting it

    # into suitable format for model predictions

    input_data = np.array(input_data).reshape(1, -1)

    # generating individual outputs

    rf_prediction = data_dict["predictions_classes"][rf_model.predict(input_data)[0]]

    nb_prediction = data_dict["predictions_classes"][nb_model.predict(input_data)[0]]

    svm_prediction = data_dict["predictions_classes"][svm_model.predict(input_data)[0]]
    dt_prediction = data_dict["predictions_classes"][dt_model.predict(input_data)[0]]

    # making final prediction by taking mode of all predictions
    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction, dt_prediction])

    predictions = {

        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": svm_prediction,
        'decision_tree_prediction': dt_prediction,
        "final_prediction": final_prediction
    }

    return predictions

