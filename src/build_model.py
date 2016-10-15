import pandas as pd
import numpy as np
import pickle
import nltk
import scipy
import graphlab as gl

from read_data import user, tip, business
from models import kmeans_euclidean, kmeans_cosine#, topo_data_analysis, kohonen
#from build_recomender import recommender

from sklearn.cluster import KMeans
from scipy.spatial.distance import cosine
from nltk.cluster.kmeans import KMeansClusterer

import itertools

yelp_usr = user()
yelp_tip = tip()
yelp_biz = business()

# Load data
yelp_usr.load()
yelp_tip.load()
yelp_biz.load()

# preprocess data
yelp_usr.preprocess()

# get data
X = yelp_usr.df.drop(['user_id','name'],axis=1).values

# New data point
p = np.ones(X.shape[1])

# Model1: Similar metric: Euclidean
model1 = kmeans_euclidean(3)
cluster1_id, prediction1 = model1.build(X,p)
community1 = set(yelp_usr.df[cluster1_id]['user_id'])
model1.save()

# Model2: Similar metric: Cosine
try:
   model2 = kmeans_cosine(3)
   cluster2_id, prediction2 = model2.build(X,p)
   community2 = set(yelp_usr.df[cluster2_id]['user_id'])
   model2.save()
except (AssertionError):
   pass
# Build rec_model

### Get subjective preference from tip_community
data  = gl.SFrame(yelp_tip.df.loc[:,'text'])
print "-------------------------------------"
print "Printing data for sentiment_analysis"
print data
m1 = gl.sentiment_analysis.create(data, features=["X1"])
# rating = the degree of positive feedback
yelp_tip.df.loc[:,'rating'] = m1.predict(data).to_numpy()


###
import build_recommender as br
test = br.recommender(yelp_tip.df, yelp_biz.df)
recs = test.build(community1, 'Phoenix')
print recs

