import datetime
import functools
import uuid
import graphlab as gl

from bson.objectid import ObjectId
from flask import (
    Flask, flash, render_template, session, request, redirect, url_for)
from pymodm.errors import ValidationError
from pymongo.errors import DuplicateKeyError

from pymodm import connect
from flask import Flask, request, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

from model import read_data
from forms import TravelForm

from model import read_data

from os import path

import pymongo
from pymongo import MongoClient

from recommender import recommender
  

SECRET_KEY = str(uuid.uuid4())
app = Flask(__name__)
app.secret_key = SECRET_KEY

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

@app.route('/')
def result():
   '''
   Home Page
   '''
   return render_template('welcome.html')


@app.route('/explore',methods = ['GET','POST'])
def home():
    '''
    Get information: city and username
    '''
    form = TravelForm()

    if request.method == 'POST':
        username=form.username.data
        city=form.city.data

	userID, community = run_model(username)
	
        db.doko.insert_one({'userID':userID,'city':city,'community': community})
        session['userCity'] = city
	session['userID'] = userID
        #session['community'] = "&".join(community)
	
        return redirect(url_for('fullmap'))
    return render_template('index.html',form=form)

@app.route('/fullmap')
def fullmap():
    '''
    Return results on Google Map.
    '''
    city_ = session.get('userCity',None)
    userID = session.get('userID',None) 
    c = db.doko.find({'userID':userID}).limit(1)

    for line in c:
        data = line

    #cities = data["city"]
    userID = data["userID"]
    community = data["community"]
    
    print "----------fullmap---------------"
    print city_
    print userID
    print community

    #community = session.get('community', None)
    #print community
    #community = community.split('&')

    top5 = build_recommender(userID,community,city_)
    print "---------Top5--------------"
    print top5

    lng1, lng2, lng3, lng4, lng5 = top5['longitude']
    lat1, lat2, lat3, lat4, lat5 = top5['latitude']
    text1, text2, text3, text4, text5 = top5['text']
    name1, name2, name3, name4, name5 = top5['name']
    
    
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:100;"
        ),
        lat=lat1,
        lng=lng1,
        markers=[
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/purple-dot.png',
                'lat': lat1,
                'lng': lng1,
                'infobox': "Hello I am <b style='color:green;'>"+name1+"</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': lat2,
                'lng': lng2,
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/orange-dot.png',
                'lat': lat3,
                'lng': lng3,
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
             {
                'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': lat4,
                'lng': lng4,
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
            {
                'icon': icons.dots.yellow,
                'title': name5,
                'lat': lat5,
                'lng': lng5,
                'infobox': (
                    "Hello I am <b style='color:#ffcc00;'>YELLOW</b>!"
                    "<h2>It is HTML title</h2>"
                    "<img src='//placehold.it/50'>"
                    "<br>Images allowed!"
                )
            }
        ],
         maptype = "TERRAIN",
        # zoom="5"
    )
    return render_template('fullmap.html', fullmap=fullmap)


#--------------------End of web app------------------------#


def run_model(username,modelName='kmodel'):
    model = gl.load_model(modelName)
    data = read_data()

    userID = data.filter_by(username,'name')[0]['user_id']
    userData =  data.filter_by(userID,'user_id')
    community_id = list(set(model.predict(userData)))[0]

    return userData['user_id'][0], list(data[model.predict(gl.SFrame(data))==community_id]['user_id'])

def build_recommender(userID,community,city):
    r = recommender()
    return r.build(userID,community,city,5)
    
def main():
    app.run(debug=True)

if __name__ == '__main__': 
    client = MongoClient()
    db = client.doko
    print "Conneted to MongoDB"

    main()