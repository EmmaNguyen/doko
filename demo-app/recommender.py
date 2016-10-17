import graphlab as gl

class recommender:
    '''
    A class to build a recomendations for a user at a city in community.
    '''
    def __int__(self,k):
    	pass

    def build(self,userID, community, city,k):
        '''
        '''
	return self.recommendations(userID, community, city,k)

    def get_data(self):
        '''
        '''
	businesses = gl.SFrame.read_json("../data/yelp_academic_dataset_business.json",orient='lines')
	tips = gl.SFrame.read_json("../data/yelp_academic_dataset_tip.json", orient='lines')
	data = tips.join(businesses,on='business_id',how="right")
	return data

    def filter_data(self,data, community, city):
        '''
        '''
	data = data.filter_by(community,'user_id')
	print data.print_rows()

	rellevant_businesses = list(set(data[data['city'] == city]['business_id']))

        print rellevant_businesses
        print data

	data = data.filter_by(rellevant_businesses,'business_id')
	return data

    def get_review(self,data):
        '''
        '''
	data = data.dropna('text')
	reviewData = gl.SFrame({'stars':data['stars'],'text':data['text']})
	m = gl.sentiment_analysis.create(reviewData,'stars',features=['text'])
	data['rating'] = m.predict(reviewData)
	return data

    def build_recommendation(self,user, data):
        '''
        '''
	recData = data['user_id','business_id','rating']   
	m = gl.ranking_factorization_recommender.create(recData,'user_id','business_id',target='rating')
	results = m.recommend()
        print results
	results = results.join(data,on='user_id',how='right')
	return recData

    def recommendations(self,userID, community, city,k):
        '''
        '''
	#city = "Carnegie"
        #userID = "fHtTaujcyKvXglE33Z5yIw"

	rawData = self.get_data()

	rellevantData = self.filter_data(rawData, community, city)
	metaData = self.get_review(rellevantData)

	results = self.build_recommendation(userID,metaData)

	return self.recommendations[:k]['latitude','longitude','name','text']



	

