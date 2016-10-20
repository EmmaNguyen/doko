## DOKO: Galvanize Capstone Project

Notice: This is an early stage of work and there will be more updates. Stay stuned!

Doko - A smart tour guider for world-traveler. Explore and travel without planning. This is a sample of work as a result of 14-day work for a capstone project of data science immersive program at Galvanize.

### Overview

This demo is mainly created by Flask, a light-weighted framework for web development with jinja2. The template of homepage is taken from abc with something I don't remember. You can find the original template here. For submit page, I create by using WTF take the main keleton from one page of Inkquick, an wonderful app of finding the matching tatoo artist, created by Lee Murray, with courtesy. The last page I is created by Flask-GoogleMaps. 

## About demo

This is a demo app to run a model based on a simple model called Kmeans, which is one of the most common algorithms to deal with high dimension and complex datasets. It is gonna return a model to create a user-by-user similarity matrix, and then use that matrix to build a recommendation system built upon a personal preference that suggest a list of matching locations in a city.

**Warning** The demo is still under constructed so there will be some bugs inside. Really sorry if it happens to you. I will try to fix the code soon. 

### How to run demo (Applied to Linux worked in terminal and )

First of all, please run this command to download dataset:


Download this git repo by running this command:

```python

git clone https://github.com/emmanguyen/doko

```

```cmd

mkdir data

wget https://s3.amazonaws.com/yelp-academic-dataset-ser/yelp_academic_dataset_tip.json

wget https://s3.amazonaws.com/yelp-academic-dataset-ser/yelp_academic_dataset_user.json

wget https://s3.amazonaws.com/yelp-academic-dataset-ser/yelp_academic_dataset_business.json
```


If your computer haven't had python yet, please install pip and python 

```python

sudo apt-get install pip

```


Before getting started, make sure you have set up an virtual enviroment for your machine. If not, it is very easy to do by simply following these commands:

```python
sudo apt-get install python-virtualenv

### initialize venv
virtualenv -p /usr/bin/python2.7 venv

### activate venv
source venv/bin/actiavate

```



Install graphlab (Only used for demo)

```python

pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/emma.mphuong@gmail.com/67C9-CA45-DD45-8D71-0330-C232-78D2-BA37/GraphLab-Create-License.tar.gz

```

Install from requirements

```python 

pip install -r requirements.txt

```

Run demo-app in terminal:

```python

cd demo-app

```

Go to the folder:

```python

cd demo-app

```

To build a model, run this command:

```
cd python model.py

```

## Acknowledgement

I would like to send my thank to Galvanize for my time at data immersive program which gives me a ton of experience in my journey of seeking for knowledge. 




