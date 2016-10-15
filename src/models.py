import pandas as pd
import numpy as np
import pickle
import nltk
import scipy
#import mapper

from sklearn.cluster import KMeans
from scipy.spatial.distance import cosine
from nltk.cluster.kmeans import KMeansClusterer
# from mapper import fcluster

class kmeans_euclidean(object):
    def __init__(self,k):
        self.k = k
        self.model = KMeans(k, random_state=0)

    def build(self,X,p):
        """
        """
        self.model.fit(X)
        prediction = self.model.predict([p])
        cluster_id = self.model.labels_== prediction
        return cluster_id, prediction

    def save(self, filename = "model1.pkl"):
        """
        """
        with open(filename, 'w') as f:
            pickle.dump(self.model, f)


class kmeans_cosine(object):
    def __init__(self,k):
        self.k = k
        self.model = KMeansClusterer(k, distance=nltk.cluster.util.cosine_distance, repeats=25)

    def build(self,X,p):
        """
        """
        data = scipy.sparse.csr_matrix(X).toarray()
        kclusters= np.array(self.model.cluster(data, assign_clusters=True))
        prediction = self.model.classify(p)
        cluster_id = kclusters == prediction
        return cluster_id, prediction

    def save(self, filename = "model2.pkl"):
        """
        """
        with open(filename, 'w') as f:
            pickle.dump(self.model, f)

class topo_data_analysis(object):
    def __init__(self, X):
        self.X = X

    def build_fit_model(self,p):
        """
        """
        pass


    def save_model(self, model):
        """
        """
        with open("model3.pkl", 'w') as f:
            pickle.dump(model, f)

class kohonen(object):
    def __init__(self, X):
        self.X = X

    def build_fit_model(self,p):
        """
        """
        pass


    def save_model(self, model):
        """
        """
        with open("model4.pkl", 'w') as f:
            pickle.dump(model, f)
