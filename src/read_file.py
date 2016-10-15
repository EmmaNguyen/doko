import pandas as pd
import numpy as np

def read_file(fileName, print_=True):
    """
    Return a DataFrame from a Mongo Database.

    INPUT:
    - fileName (str): File Name, include path to directory.
    - print_ (boolean): Print columns names.

    OUTPUT:
    - DataFrame.
    - (Default) Name of columns in DataFrame.
    """

    print "Reading file " + fileName + "..."

    with open(fileName,'rb') as f:
         data = f.readlines()

    # Fix trailling error.
    data = map(lambda x: x.strip(), data)
    data_json_str = "[" + ",".join(data) + "]"
    df = pd.read_json(data_json_str)

    # Print structure of dataframe up to second level
    if print_:
        print "STRUCTURE:"
        for col in df.columns:
            print "   |" + col
            try:
                if type(df[col][0]) == dict:
                    for key in df[col][0].keys():
                        print "      |" + key
                        try:
                            if type(df[col][0][0]) == dict:
                                for key in df[col][0][0].keys():
                                    print "         |" + key
                        except (KeyError):
                            pass
            except (KeyError):
                pass
        print ""
        print "-------------------------------------"
        print ""
    return df
