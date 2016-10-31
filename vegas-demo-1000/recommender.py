import graphlab as gl

class recommender:
    '''
    A class to build a recomendations for a user at a city in community.
    '''
    def __int__(self):
    	pass

    def get_data(self):
        '''
        INPUT: None
        OUTPUT: None

        Get data from tips and businesses.
        '''
	filename_biz = "../data/vegas_user1000.json"
	data = gl.SFrame.read_json(filename_biz,orient='records')
	return data

    def build(self,userID, community,k):
        '''
        INPUT: 
         - userID: string
         - community: list of strings
         - k: int, number of top results
        OUTPUT: SFrame
        
        Return a list of top results
        '''
	rawData = self.get_data()
	#print "Raw Data: --------"
	#print rawData

	communityData = self.get_community(rawData, community)
	#print "Community data: -------"
	#print communityData

        metaData = self.get_review(communityData)
	#print "Meta data: --------- "
	#print metaData

	fullResults = self.get_result(userID,metaData)
        #print "Recommendation for", userID
        #print fullResults

	return fullResults.filter_by(userID,'user_id')[:k]
        
    def get_community(self, data, community):
        '''
        INPUT:
         - data: SFrame
         - community: a list of strings
        OUTPUT: Sframe

        Return data only of community
        '''
        return data.filter_by(community,'user_id')

    def get_review(self,data):
        '''
        INPUT:
        - data: SFrame

        OUTPUT: Sframe

	Return data with a new column called 'rating' by doing sentiment analysis
        '''
	data = data.dropna('text')
	reviewData = gl.SFrame({'text':data['text']})
	m = gl.sentiment_analysis.create(reviewData,features=['text'])
	data['rating'] = m.predict(reviewData)
	return data

    def get_result(self,userID,data):
        '''
        INPUT:
          - userID: str
          - data: SFrame
        OUTPUT:
        Return data of SFrame with the information, 
        including user_id, b_name, latitude longitude, text
        '''
	recData = data['user_id','business_id','rating']   
	m = gl.ranking_factorization_recommender.create(recData,user_id='user_id',item_id='business_id',target='rating')
	recList = m.recommend()
	data.remove_column('user_id')
	recList = recList.join(data,on='business_id',how='left')

	return recList['user_id','b_name','latitude','longitude','text'].unique()
        
if __name__=="__main__":
    recs = recommender()
    recs.build(userID, community, k)



	

