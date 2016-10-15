import pandas as pd
import numpy as np
from read_file import read_file

class user(object):

    """

    Class function to read and process data from Yelp Challenge User Dataset.

    """

    def __init__(self):
        self.df = pd.DataFrame()         #All user information.
        self.friends = pd.DataFrame()    #user, [friend1, friend2,..].

    def load(self):
        """
        Load data from mongodb.

        INPUT: None.
        OUTPUT: None.
        """
        #self.df = read_file("../data/yelp_academic_dataset_user.json")  #Full Data.
        self.df = read_file("../data/user300.json")                      #For local machine.
        #self.get_friend_list()
        #self.save_friend_nodes()

    def preprocess(self):
        """
        Pre-process data.

        INPUT: None.
        OUTPUT: None.
        """ 
        self.get_dummies_dict()
        self.get_dummies_list()
        self.drop_columns()
        self.df.fillna(0,inplace=True)

    def get_friend_list(self):
        """
        Get an adjacency list of friends from a list of friends.

        INPUT: None.
        OUTPUT: None.
        """
        self.friends = self.df[['user_id','friends']]

    def save_friend_nodes(self):
        """
        Turn an adjacency list into an edge list.

	INPUT: None.
	OUTPUT: A .tsv file
        """
        print "Exporting to file tsv ..."
        count_edge = 0
        count_node = 0
        with open('../data/yelp.tsv','w') as f:
            for user in self.df['user_id']:
                for friends in self.df['friends']:
                    count_node += 1
                    for friend in friends:
                        f.write("%s\t%s\n" % (user, friend))
                        count_edge += 1
        print "Graph Summary:", count_node, "nodes,", count_edge, "edges."

    def get_dummies_dict(self, \
                         cols=['votes',\
                               'compliments'],\
                         drop_=True):
        """
        Get dummies for dictionaries.

        INPUT:
        - cols : (list) a list of columns names.
        - drop_: (boolean) a checker for dropping after dumifying.

        OUTPUT: None
        """
        for col in cols:
            print "Pre-processing " + col + "..."
            temp = pd.DataFrame(self.df[col].tolist())
            temp.columns = col + "_" + temp.columns
            if drop_:
                self.df.drop(col,axis = 1, inplace=True)
            self.df = pd.concat([self.df, temp],axis=1)

    def get_dummies_list(self, 
                         cols=['elite'],\
                         drop_=True):
        """
        Get dummies for lists.

        INPUT:
        - cols : (list) a list of columns names.
        - drop_: (boolean) a checker for dropping after dumifying.

        OUTPUT: None
        """
        for col in cols:
            print "Pre-processing " + col + "..."
            temp = pd.get_dummies(self.df[col].apply(pd.Series).stack(),drop_first=True)\
                                                   .astype(int).sum(level=0).astype(int)
            # temp.columns.apply(str).apply(lambda x: col + "_" + x)
            if drop_:
                self.df.drop(col,axis = 1, inplace=True)
            self.df = pd.concat([self.df, temp],axis=1)

    def drop_columns(self, \
                     cols=['_id',\
                          'friends',\
                          'type',\
                          'yelping_since']):
        """
        Remove nomial data.

        INPUT: None.
        OUTPUT: None.
        """
        for col in cols:
            del self.df[col]

class tip(object):
    '''
    '''
    def __init__(self):
        self.df = pd.DataFrame()

    def load(self):
        self.df = read_file("../data/yelp_academic_dataset_tip.json")
class business(object):
    '''
    '''
    def __init__(self):
        self.df = pd.DataFrame()

    def load(self):
        self.df = read_file("../data/yelp_academic_dataset_business.json")

class checkin(object):
    '''
    '''
    def __init__(self):
        self.df = pd.DataFrame()

    def load(self):
        self.df = read_file("../data/yelp_academic_dataset_checkin.json")

class review(object):
    '''
    '''
    def __init__(self):
        self.df = pd.DataFrame()

    def load(self):
        self.df = read_file("../data/yelp_academic_dataset_review.json")
