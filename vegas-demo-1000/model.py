import graphlab as gl

def read_data(filename='../data/vegas_user1000.json'):
    '''
    INPUT: filename, default is none
    OUTPUT: SFrame

    Return a SFrame of data
    '''
    return gl.SFrame.read_json(filename, orient='records')

def feature_engineer(sf,features):
    '''
    INPUT: 
    - sf: SFrame
    - features: a list of features
    OUTPUT: SFrame
    
    Return a SFrame with selected features. 
    '''
    return sf[features]

def train_model(data):
    '''
    INPUT: SFrame
    OUTPUT: None
   
    Create a k-means model.
    '''
    model = gl.kmeans.create(data, num_clusters=10)
    model.save('kmodel')

if __name__=="__main__":
    raw_data = read_data()
    data = feature_engineer(raw_data, features=['average_stars','compliments','fans','votes','name','user_id'])
    train_model(data)
