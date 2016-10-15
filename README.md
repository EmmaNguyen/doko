### DOKO: Galvanize Capstone Project

Notice: This is an early stage of work and there will be more updates. Stay stuned!

Doko - A smart tour guider for world-traveler. Explore and travel without planning. This is a sample of work as a result of 14-day work for a capstone project of data science immersive program at Galvanize.

### Overview

The ultimate goal is to create a web app that helps people explore new places. I apply unsupervised learning models including K-means (Clustering), Topological Data Analysis (Computational Topology) and Kohonen Map (Artificial Neural Network) to segment user data into similar groups and build a recommendation of business ids. The data set is taken from Yelp dataset challenge under the condition of Academic/Education purpose. 

This is just a simple demo of Kmeans clustering to run on a local machine based on 1000 users. I am testing some more models on Spark with AWS with amount of data arround 2 TB. More work will be updated later. 

## About demo

This is going to run a model based on a simple model called Kmeans, which is one of the most common algorithms to deal with high dimension and complex datasets. The above command is gonna return a model to create a user-by-user similarity matrix, and then use that matrix to build a recommendation system built upon a personal preference that suggest a list of matching locations in a city.

**Warning** The demo is still under constructed so there will be some bugs inside. Really sorry if it happens to you. I will try to fix the code soon. 

### How to run demo (Applied to Linux worked in terminal and )

Download this git repo by running this command:

'''python
git clone https://github.com/emmanguyen/doko
'''

Install pip and python 

'''
sudo apt-get install pip
'''

Install graphlab (Only used for demo)

'''python
pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/emma.mphuong@gmail.com/67C9-CA45-DD45-8D71-0330-C232-78D2-BA37/GraphLab-Create-License.tar.gz
'''

Install from requirements

'''python 
pip install -r requirements.txt
'''

Run demo-app in terminal:

'''python
cd demo-app
'''

Go to the folder:

'''python
cd demo-app
'''

To build a model, run this command:

'''
cd python model.py
'''

### Reference:

Soon to be added.
