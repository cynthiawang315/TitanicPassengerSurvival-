"""
Note this file contains _NO_ flask functionality.
Instead it makes a file that takes the input dictionary Flask gives us,
and returns the desired result.

This allows us to test if our modeling is working, without having to worry
about whether Flask is working. A short check is run at the bottom of the file.
"""

import pickle as pickle
import numpy as np
import pandas as pd

with open("./models/gbm.pickle", "rb") as f:
    gbm = pickle.load(f)



def make_prediction(feature_dict):
    """
    Input:
    feature_dict: a dictionary of the form {"feature_name": "value"}

    Function makes sure the features are fed to the model in the same order the
    model expects them.

    Output:
    Returns (x_inputs, probs) where
      x_inputs: a list of feature values in the order they appear in the model
      probs: a list of dictionaries with keys 'name', 'prob'
    """
    if (len(feature_dict) == 0):
        return (0, 0)


    pclass = float(feature_dict.get('pclass', 3))
    sibsp = float(feature_dict.get('sibsp',0))
    parch = float(feature_dict.get('parch', 0))
    group_size = float(feature_dict.get('group_size', 0)) + 1
    individual_fare = float(feature_dict.get('individual_fare', 0)) / 20  # convert currency into current dollars
    fare = individual_fare * group_size
    fam_size = sibsp + parch

    sex_male = 0
    embarked_Q = 0
    embarked_S = 0
    title_Master = 0
    title_Mr = 0
    title_Mrs = 0
    age_group_12to18 = 0
    age_group_25to35 = 0
    age_group_35to45 = 0
    age_group_less_than_12 = 0
    age_group_more_than_45 = 0



    if feature_dict['gender'] == 'male':
        sex_male = 1

    if feature_dict['embark'] == 'Q':
        embarked_Q = 1
    if feature_dict['embark'] == 'S':
        embarked_S = 1

    if feature_dict['title'] == 'Mr':
        title_Mr = 1
    if feature_dict['title'] == 'Mrs':
        title_Mrs = 1
    if feature_dict['title'] == 'Master':
        title_Master = 1
    if feature_dict['title'] == 'Dr' and sex_male == 1:
        title_Mr = 1
    if feature_dict['title'] == 'Dr' and sex_male == 0:
        title_Mr = 1

    if feature_dict['age'] == '<12':
        age_group_less_than_12 = 1
    if feature_dict['age'] == '12-18':
        age_group_12to18 = 1
    if feature_dict['age'] == '25-35':
        age_group_25to35 = 1
    if feature_dict['age'] == '35-45':
        age_group_35to45 = 1
    if feature_dict['age'] == '>45':
        age_group_more_than_45 = 1

    x_input = [pclass,sibsp,parch,fare,group_size,individual_fare,fam_size,sex_male,
             embarked_Q,embarked_S,title_Master,title_Mr,title_Mrs,
             age_group_12to18,age_group_25to35,age_group_35to45,age_group_less_than_12,
             age_group_more_than_45]

    x_input_dict = dict(zip(gbm.feature_names, x_input))
    x_input_df = pd.DataFrame(x_input_dict, index=[0])

    prob = float(gbm.predict_proba(x_input_df)[:,1])

    x_userinput = []
    for x in feature_dict.values():
        x_userinput.append(x)
    print(x_userinput)

    return (x_userinput, prob)



# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing
if __name__ == '__main__':
    # from pprint import pprint
    # print("Checking to see what setting all params to 0 predicts")
    # features = {f: '0' for f in feature_names}
    # print('Features are')
    # pprint(features)
    #
    # x_input, probs = make_prediction(features)
    # print(f'Input values: {x_input}')
    # print('Output probabilities')
    # pprint(probs)
    print('No error')
