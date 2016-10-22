import graphlab as gl

class recommender:
    '''
    A class to build a recomendations for a user at a city in community.
    '''
    def __int__(self):
    	pass

    def get_data(self):
        '''
        Get data from tips and businesses.
        '''
	businesses = gl.SFrame.read_json("../data/yelp_academic_dataset_business.json",orient='lines')
	tips = gl.SFrame.read_json("../data/yelp_academic_dataset_tip.json", orient='lines')
	data = tips.join(businesses,on='business_id',how="right")
	return data

    def build(self,userID, community, city,k):
        '''
        '''
	#city = "Carnegie"
        #userID = "fHtTaujcyKvXglE33Z5yIw"

	rawData = self.get_data()
	print "Raw Data: --------"
	print rawData

	communityData = self.get_community(rawData, community)
	print "Community data: -------"
	print communityData

        #rellevantData = self.get_city(communityData, city)
	
        metaData = self.get_review(communityData)
	print "Meta data: --------- "
	print metaData

	fullResults = self.get_result(userID,metaData)
        print "Recommendation --------"

	results = fullResults.filter_by(city,'city')
        print "Result of a city --////----", city

	return fullResults[:k]['city','latitude','longitude','name','text']
        
    def get_community(self, data, community):
        '''
        '''
        return data.filter_by(community,'user_id')

    def get_review(self,data):
        '''
        '''
	data = data.dropna('text')
	reviewData = gl.SFrame({'text':data['text']})
	m = gl.sentiment_analysis.create(reviewData,features=['text'])
	data['rating'] = m.predict(reviewData)
	return data

    def get_result(self,user,data):
        '''
        '''
	recData = data['user_id','business_id','rating']   
	m = gl.ranking_factorization_recommender.create(recData,'user_id','business_id',target='rating')
	recList = m.recommend()
	recData = data.join(recList,on='user_id',how='left')
	return recData

if __name__=="__main__":
    #name = "Jeremy"
    #userID, community = run_model(name)
    #city = "ABC"
    #k = 5

    recs = recommender()
    recs.build(userID, community, city,k)



	

