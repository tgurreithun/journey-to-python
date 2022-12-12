'''
DATA COLLECTION IS HARD!
This is a list of all the functions created to collect data and clean it up 
for analysis 
'''
# importing stuff
import pandas as pnd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import matplotlib as mpl
import scipy.stats as stats
import math as math


##removes Nans from a data set
def trimNanData(xs):
    xs = np.array(xs)[np.logical_not(np.isnan(np.array(xs)))]
    return xs

##grab the colomn titles from a csv file
def getColumnTitles(file):
    data = pnd.read_csv(str(file))
    list_of_column_names = list(data.columns)

    # displaying the list of column names
    print('List of column names : ',
          list_of_column_names)
    return

def getData(file):
    df = pnd.read_csv(str(file))
    return(df)


# there is NAN data in here that we need to remove, but we have to be careful 
# if one array has Nan that we delete that index entry in both arrays
def trimNanTuples (xs, ys):
    if len(xs) != len(ys) :
        raise ValueError("Arrays must have the same size")
    else:  
        nans = [] #keep track of nan indeces
        for i in range(len(xs)):
            if math.isnan(xs[i]) == True:
                nans.append(i)
            elif math.isnan(ys[i]) == True: 
                nans.append(i)
    #print(len(nans))
    for index in sorted(nans, reverse=True):
        del xs[index]
        del ys[index]
    return    

def trimNanTriads (xs, ys,zs):
    if len(xs) != len(ys) :
        raise ValueError("Arrays must have the same size")
    elif len(xs) != len(zs):
        raise ValueError("Arrays must have the same size")
    else:  
        nans = [] #keep track of nan indeces
        for i in range(len(xs)):
            if math.isnan(xs[i]) == True:
                nans.append(i)
            elif math.isnan(ys[i]) == True: 
                nans.append(i)
    #print(len(nans))
    for index in sorted(nans, reverse=True):
        del xs[index]
        del ys[index]
        del zs[index]
    return   