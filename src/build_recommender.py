import collections
import graphlab as gl
import pandas as pd
import json
from pymongo import MongoClient

from sklearn.neighbors import DistanceMetric
dist = DistanceMetric.get_metric('haversine')


class recommender(object):
    def __init__(self, df_tip, df_biz):
        self.tip = df_tip
        self.biz = df_biz
        self.loc = None

    def build(self, community, city):
        ### Get information of community
        tip_community = self.tip.loc[self.tip['user_id'].isin(community)]

        if city is None:
            # Get a list of business.
            businesses = list(set(tip_community['business_id']))

            # Get information of businesses for biz.
            biz_community = self.biz.loc[df['business_id'].isin(businesses)]

            # Calculate distances from loc to business_id.
            biz_community.loc[:,'dist'] = biz_community[['longitude','latitude']].apply(lambda x: dist.pairwise(self.loc,x[np.newaxis,:])[0][0], axis = 1)

            # Get a list of rellevant businesses in diameter of 10 unit of distance.
            rellevant_businesses = list(set(business_info[business_info.loc[:,'dist'] < 10]['business_id']))

            # Get a rellevant information for tip_community.
            tip_community = tip_community.loc[self.tip['user_id'].isin(relevant_businesses)]
        else:
            print "-------------------------"
            print "Print list of locations visited by community"
            # Get rellevant businesses located in the same city.
            rellevant_businesses = list(set(self.biz[self.biz.city == city]['business_id']))
            # Get a rellevant businesses for tip_community.
            tip_community = tip_community.loc[self.tip['business_id'].isin(rellevant_businesses)]
            # Error: there is a case that city is not in the list
        print tip_community
        ### Build a recommender
        sf = gl.SFrame(tip_community.loc[:,['user_id','business_id','rating']])
        print "-------------------------------------"
        print "Printing data for recommender"
        print sf
        m2 = gl.ranking_factorization_recommender.create(sf,\
                                                        'user_id',\
                                                        'business_id',\
                                                         target='rating')
        recs = m2.recommend()
        recs_df = recs.to_dataframe()
	
	top5_df = recs_df[recs_df['rank'] <=5]
	top5_id = list(top5_df['business_id'])
	top5_loc = self.biz[self.biz['business_id'].isin(top5_id)][['name','longitude','latitude']]

        top5_df.join(top5_loc, on=['business_id'])
	print top5_df    
         # Here we identify top5 by all of users, since don't use all the amount of
         # data to reduce the effect of variance/bias.
	with open('top5.json','w') as f:	
	    f.write(json.dumps(top5_loc.to_json(orient="index")))
	return top5_loc


