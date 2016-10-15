import graphlab as gl

def read_data(filename='../data/user1000.json'):
    return gl.SFrame.read_json(filename, orient='lines')

def feature_engineer(sf,features):
    return sf[features]

def train_model(data):
    model = gl.kmeans.create(data, num_clusters=3)
    model.save('kmodel')

if __name__=="__main__":
    raw_data = read_data()
    data = feature_engineer(raw_data, features=['average_stars','compliments','fans','votes'])
    train_model(data)
