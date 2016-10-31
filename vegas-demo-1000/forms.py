from flask_wtf import Form
from wtforms import StringField


class TravelForm(Form):
    username = StringField('Name of travler')
    city = StringField('City where you are ? (San Francisco/ LA/ New York/ Boston/ Chicago)')
    
