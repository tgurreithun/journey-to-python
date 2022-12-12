'''
DATA ANALYSIS IS HARD!
This is a list of all the functions created to analyze data
'''
# importing stuff
import pandas as pnd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import matplotlib as mpl
import scipy.stats as stats
import csv as csv
import collect as co


def basicStats(xs,title='Title', description='description',savePath='C:\\Users\\tgurr\\Desktop\\research\\results\\stats\\'):
    #print(str(title),": ",str(description))
    N = len(xs)
    med = round(np.nanmedian(xs),2)
    ave = round(np.nanmean(xs),2)
    var = round(np.nanvar(xs),2)
    std = round(np.nanstd(xs),2)
    top25 = round(np.nanpercentile(xs,75),2)
    bot25 = round(np.nanpercentile(xs,25),2)
    
    ##now write that to a .csv
    
    header = ['title','description','N','med', 'ave', 'var', 'std', 'top25', 'bot25']
    data = [title, description, N, med, ave, var, std, top25, bot25]
    
    with open(str(savePath)+str(title)+'-basic-stats.csv', 'w',newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
    
        # write the header
        writer.writerow(header)
        
        # write the data
        writer.writerow(data)
        
    return [title, description, med, ave, var, std, top25, bot25]



### get variances and t-tests####
def twoPopStats (x1, x2,label='here are your stats:'):
    ave1 = round(np.mean(x1),2)
    ave2 = round(np.mean(x2),2)
    chng = round(ave2 - ave1,2)
    var1 = round(np.var(x1),2)
    var2 = round(np.var(x2),2)
    
    print(label)
    print('ave 1:',ave1,'ave 2:',ave2)
    print('var 1:',var1,'var 2:',var2)
    
    print('change in average:',chng)
    
    t = stats.ttest_ind(a=x1, b=x2, equal_var=False) #assuming unequal variances
    
    print(t)
          
    print()
    return


def runCompStats(x1, x2, x3,item='item',label1='group 1',label2='group2',label3='group3',savePath=0):
    N1 = len(x1)
    N2 = len(x2)
    N3 = len(x3)
    
    ave1 = round(np.mean(x1),2)
    ave2 = round(np.mean(x2),2)
    ave3 = round(np.mean(x3),2)
    
    chng12 = round(ave2 - ave1,2)
    chng13= round(ave3 - ave1,2)
    
    var1 = round(np.var(x1),2)
    var2 = round(np.var(x2),2)
    var3 = round(np.var(x3),2)
    
    
    t12 = stats.ttest_ind(a=x1, b=x2, equal_var=False) #assuming unequal variances
    t13 = stats.ttest_ind(a=x1, b=x3, equal_var=False) #assuming unequal variances
    
    ##now write that to a .csv
    
    header = ['item','label','N', 'ave','ave difference', 'var','t-test']
    data1 = [item, label1, N1, ave1, 0, var1,'baseline']
    data2 = [item, label2, N2, ave2, chng12, var2, t12]
    data3 = [item, label3, N3, ave3, chng13, var3, t13]
    
    
    with open(str(savePath)+str(item)+'-comparison-stats.csv', 'w',newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
    
        # write the header
        writer.writerow(header)
        
        # write the first set of data
        writer.writerow(data1)
        
        #write the second set of data
        writer.writerow(data2, )
        
        #write the third
        writer.writerow(data3)


def covidGroupPretests(allData, pretest):     
    #pull the data
    yrQtrs = np.array(allData['YrQtr'])
    pretestScores = np.array(allData[str(pretest)+'-score'])
    
    
    #create all the spaces we need
    preCOVID = []
    UWonline = []
    HSonline = []
    
    ##break the data into covid groups
    for y in range(len(yrQtrs)): 
        if yrQtrs[y] < 201:
            ##add 194 and earlier to preCOVID
            preCOVID.append(round(pretestScores[y],2))
        elif yrQtrs[y] >= 214: 
            ##add 214-present to HS online
            HSonline.append(round(pretestScores[y],2))
        else: 
            ###add 202-213 to UW online
            UWonline.append(round(pretestScores[y],2))
     
     #get rid of nan data                            
    co.trimNanData(HSonline)                         
    co.trimNanData(UWonline)                         
    co.trimNanData(preCOVID)
    
    return preCOVID, UWonline, HSonline
