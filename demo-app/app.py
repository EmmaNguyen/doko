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

from forms import TravelForm

from model import read_data

from os import path
  

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

        session['city'] = city
        session['community'] = "&".join(run_model(username))

        return redirect(url_for('fullmap'))
    return render_template('index.html',form=form)

@app.route('/fullmap')
def fullmap():
    '''
    Return results on Google Map.
    '''
    city = session['city']
    community = session['community']
    community = community.split('&')

    top5 = build_recommender(community,city)

    lat1, lng1, info1 = list(top5.iloc[0])
    lat2, lng2, info2 = list(top5.iloc[1])
    lat3, lng3, info3 = list(top5.iloc[2])
    lat4, lng4, info4 = list(top5.iloc[3])
    lat5, lng5, info5 = list(top5.iloc[4])

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
        
        markers=[
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'title': info1, 
                'lat': lat1,
                'lng': lng1,
                'infobox': "Coool!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'title': info2, 
                'lat': lat2,
                'lng': lng2,
                'infobox': "Awesome!"            
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'title': info3, 
                'lat': lat3,
                'lng': lng3,
                'infobox': "Hahaha Food is great!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/orange-dot.png',
                'title': info4, 
                'lat': lat4,
                'lng': lng4,
                'infobox': "Special Promotion in this weekend!!!"
            },
	    {
                'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'title': info5, 
                'lat': lat5,
                'lng': lng5,
                'infobox': "Super special discount for ALLLLL!"
            }

        ],
         maptype = "TERRAIN",
        # zoom="5"
    )
    return render_template('fullmap.html')


#--------------------End of web app------------------------#

def run_model(username,modelName='kmodel'):
    model = gl.load_model(modelName)
    data = read_data()
    dataset =data[data["name"]==username]
    community_id = list(set(model.predict(dataset)))[0]
    return list(data[model.predict(data)==community_id]['user_id'])

def build_recommender():
    r = recommender()
    return r.build()
    
def main():
    app.run(debug=True)
if __name__ == '__main__': 
    main()

