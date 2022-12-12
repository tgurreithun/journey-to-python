'''
PLOTTING IS FUN!
This is a list of all the functions created to plot data
'''
# importing stuff
import pandas as pnd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import matplotlib as mpl
import scipy.stats as stats
from datetime import datetime
import csv as csv


def saveMetaData(savePath=0, title='nameless', dataset='dataset',researcher='TGE'):
    if savePath != 0: 
        now = datetime.now()
        date = now.strftime("%d-%m-%Y-%H")
        
        header = ['title','date','researcher','dataset']
        data = [title, date, researcher,dataset]
        
        with open(str(savePath)+str(title)+'-basic-stats.csv', 'w',newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
        
            # write the header
            writer.writerow(header)
            
            # write the data
            writer.writerow(data)
    
        
        return
    return 
    
    

##PLOT TWO HISTOGRAMS SIDE BY SIDE##
def compareTwoHists(x1,x2,title1='Plot 1',title2='Plot 2', color1='grey',color2='grey',pretest='pretest',cumulative=False): 
    N1=len(x1)
    N2=len(x2)
    
    
    fig, (ax1,ax2) = plt.subplots(1,2,sharey=True)

    array1 = np.array(x1)
    unique1 = np.unique(array1)
    items1 = len(unique1)  
    
    array2 = np.array(x2)
    unique2 = np.unique(array2)
    items2 = len(unique2)  
    
    if items1 >= items2: 
        bins = unique1
    else: bins = unique2
    
    bins = np.append(bins, [1.1])
    bins = [x - .05 for x in bins]
    
    
    print(pretest+' bins: '+bins)
    
    #left plot stuff
    ax1.hist(x1, density = True, bins=bins, edgecolor='black', color=str(color1),cumulative=cumulative)
    ax1.set_xlabel(str(pretest)+' score', size='x-large')
    #ax1.set_ylabel('density', size='x-large')
    ax1.set_title(str(title1)+' (N='+str(N1)+')', size='x-large')
    ax1.set_xlim([0, 1.1])

    #right plot stuff
    ax2.hist(x2, density = True, bins=bins, edgecolor='black',color=str(color2),cumulative=cumulative)
    ax2.set_xlabel(str(pretest)+' score', size='x-large')
    ax2.set_title(str(title2)+' (N='+str(N2)+')', size='x-large')
    ax2.set_xlim([0, 1.1])
    
    #resize the plot
    plt.rcParams['figure.figsize'] = [8, 4]

    #bring them close together
    plt.subplots_adjust(wspace=.05, hspace=0)

    
    return

def compareHists(x1,
                 x2,
                 x3,
                 title1='Plot 1',
                 title2='Plot 2',
                 title3='Plot 3', 
                 color1='grey',
                 color2='grey',
                 color3='grey',
                 item='item',
                 cumulative=False,
                 savePath= 0): 
    N1=len(x1)
    N2=len(x2)
    N3=len(x3)
    
    # now = datetime.now()
    # dt_string = now.strftime("%d-%m-%Y-%H")
    
    
    array1 = np.array(x1)
    unique1 = np.unique(array1)
    items1 = len(unique1)  
    
    array2 = np.array(x2)
    unique2 = np.unique(array2)
    items2 = len(unique2)  
    
    if items1 >= items2: 
        bins = unique1
    else: bins = unique2
    
    binWidth = bins[2]-bins[1]
    newBin = 1 + binWidth
    
    #print(str(item)+' bins: '+str(bins))
    bins = np.append(bins, [newBin])
    bins = [x - binWidth/2 for x in bins]
    #print(str(item)+' bins after cleaning: '+str(bins))
    
    
    fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
    
    #super title
    #plt.suptitle(str(item)+' ('+str(len(bins)-2)+' questions)')
    
    #left plot stuff
    ax1.hist(x1, density = True, bins=bins, edgecolor='black', color=str(color1),cumulative=cumulative)
    #ax1.set_xlabel(str(item)+' score', size='x-large')
    #ax1.set_ylabel('density', size='x-large')
    ax1.set_title(str(title1)+' (N='+str(N1)+')', size='x-large')
    ax1.set_xlim([-.08, 1.08])

    #middle plot stuff
    ax2.hist(x2, density = True, bins=bins, edgecolor='black',color=str(color2),cumulative=cumulative)
    ax2.set_xlabel(str(item)+' score'+' ('+str(len(bins)-2)+' questions)', size='x-large')
    ax2.set_title(str(title2)+' (N='+str(N2)+')', size='x-large')
    ax2.set_xlim([-.08, 1.08])
    
    #right plot stuff
    ax3.hist(x3, density = True, bins=bins, edgecolor='black',color=str(color3),cumulative=cumulative)
    #ax3.set_xlabel(str(item)+' score', size='x-large')
    ax3.set_title(str(title3)+' (N='+str(N3)+')', size='x-large')
    ax3.set_xlim([-.08, 1.08])
    
    #resize the plot
    plt.rcParams['figure.figsize'] = [8, 4]

    #bring them close together
    plt.subplots_adjust(wspace=.05, hspace=0)
    
    plt.savefig(str(savePath)+str(item)+'-hists-'+str(title1)+'-'+str(title2)+'-'+str(title3)+'.png')
    
    plt.show()
    return



#PLOT TWO HISTOGRAMS ON TOP OF EACHOTHER
def overlapHists(x1,
                 x2,
                 qtrs1='?', #expects the number of quarters offered
                 qtrs2='?',
                 title1='Plot 1',
                 title2='Plot 2', 
                 color1='grey',
                 color2='grey',
                 item='item',
                 cumulative=False,
                 savePath=0): 
    
    N1=len(x1)
    N2=len(x2)
    
    # now = datetime.now()
    # dt_string = now.strftime("%d-%m-%Y-%H")
    
    array1 = np.array(x1)
    unique1 = np.unique(array1)
    items1 = len(unique1)  
    
    array2 = np.array(x2)
    unique2 = np.unique(array2)
    items2 = len(unique2)  
    
    if items1 >= items2: 
        bins = unique1
    else: bins = unique2
    
    binWidth = bins[2]-bins[1]
    newBin = 1 + binWidth
    
    bins = np.append(bins, [newBin])
    bins = [x - binWidth/2 for x in bins]
    
    #plot stuff
    plt.hist(x1, density=True, bins=bins,edgecolor='black',hatch= '..',color='white',label=str(title1)+' (N='+str(N1)+', '+str(qtrs1)+' quarters)',cumulative=cumulative)
    plt.hist(x2, density=True, bins=bins,edgecolor='black',alpha=.5,color=str(color2),label=str(title2)+' (N='+str(N2)+', '+str(qtrs2)+' quarters)',cumulative=cumulative)
    
    plt.title(str(title1)+' vs. '+str(title2), size='x-large')
    plt.xlabel(str(item)+' score ('+str(len(bins)-2)+" questions)", size='x-large')
    #plt.ylabel('density', size='x-large')
    plt.legend(loc='upper left')
    
    #resize the plot
    plt.rcParams['figure.figsize'] = [8, 4]
    
    plt.savefig(str(savePath)+str(item)+'-overlap-'+str(title1)+'-'+str(title2)+'.png')
    
    plt.show() 
    return




##PLOT DENSITIES OF TWO SCATTER PLOTS SIDE BY SIDE
def plotDensities(x1,
                  y1,
                  x2,
                  y2,
                  title1='Plot 1',
                  title2='Plot 2',
                  quad=0, 
                  xLabel='x label',
                  yLabel='y label',
                  savePath=0): 
    N1=len(x1)
    N2=len(x2)
    
    # now = datetime.now()
    # dt_string = now.strftime("%d-%m-%Y-%H")

    #get the density for each 
    xy = np.vstack([x1,y1])
    z = gaussian_kde(xy)(xy)
    
    # Sort the points by density, so that the densest points are plotted last
    idx = z.argsort()
    x1, y1, z1 = np.array(x1)[idx], np.array(y1)[idx], np.array(z)[idx]
    
    #get the density for each 
    xy = np.vstack([x2,y2])
    z = gaussian_kde(xy)(xy)
    
    # Sort the points by density, so that the densest points are plotted last
    idx = z.argsort()
    x2, y2, z2 = np.array(x2)[idx], np.array(y2)[idx], np.array(z)[idx]
    

    fig, (ax1,ax2) = plt.subplots(1,2,sharey=True)

    #left plot stuff
    ax1.scatter(x1, y1, c=z1, s=50)
    ax1.set_xlabel(xLabel,size='x-large')
    ax1.set_ylabel(yLabel,size='x-large')
    ax1.set_title(str(title1)+' (N='+str(N1)+')', size='x-large')
    ax1.axhline(y=2, color='k', linestyle='--', linewidth=1)           
    ax1.axvline(x=.5, color='k',linestyle='--', linewidth=1)

    #right plot stuff
    ax2.scatter(x2, y2, c=z2, s=50)
    ax2.set_xlabel(xLabel, size='x-large')
    ax2.set_title(str(title2)+' (N='+str(N2)+')', size='x-large')
    ax2.axhline(y=2, color='k', linestyle='--', linewidth=1)           
    ax2.axvline(x=.5, color='k',linestyle='--', linewidth=1) 

    #resize the plot
    plt.rcParams['figure.figsize'] = [8, 4]

    #bring them close together
    plt.subplots_adjust(wspace=.05, hspace=0)
    
    #add an option to choose the quadrant
    if quad == 0: 
        fig.suptitle("All students", size='x-large')
    if quad == 1:
        ax1.set_xlim([.5, 1])
        ax2.set_xlim([.5, 1])
        ax1.set_ylim([2, 4])
        ax2.set_ylim([2, 4])
        fig.suptitle("HighPre, HighPost", size='x-large')
    if quad == 2:
        ax1.set_xlim([0, .5])
        ax2.set_xlim([0, .5])
        ax1.set_ylim([2, 4])
        ax2.set_ylim([2, 4])
        fig.suptitle("LowPre, HighPost", size='x-large')
    if quad == 3:
        ax1.set_xlim([0, .5])
        ax2.set_xlim([0, .5])
        ax1.set_ylim([0, 2])
        ax2.set_ylim([0, 2])
        fig.suptitle("LowPre, LowPost", size='x-large')
    if quad == 4:
        ax1.set_xlim([.5, 1])
        ax2.set_xlim([.5, 1])
        ax1.set_ylim([0, 2])
        ax2.set_ylim([0, 2])
        fig.suptitle("HighPre,LowPost", size='x-large')
    
 
    plt.savefig(str(savePath)+'densities-'+str(xLabel)+'-vs-'+str(yLabel)+'-'+str(title1)+'-'+str(title2)+'.png')
    plt.show()
        
    return


def compareScatters(x1, y1,
                 x2,y2,
                 x3,y3,
                 title1='Plot 1',
                 title2='Plot 2',
                 title3='Plot 3', 
                 #color1='grey',
                 #color2='grey',
                 #color3='grey',
                 xlabel='x-label',
                 ylabel='y-label',
                 supTitle='Super Title!',
                 colormap = 'inferno',
                 preAve = 0,
                 aveLines = False,
                 mins = 1,
                 maxes = 1,
                 savePath= 0): 
    
    # now = datetime.now()
    # dt_string = now.strftime("%d-%m-%Y-%H")
    
    x1 = list(x1)
    x2 = list(x2)
    x3 = list(x3)
    
    fig, (ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
    
    fig.suptitle(supTitle)
    fig.set_figwidth(18)
    
    if aveLines == True: 
        ax1.axhline(y=preAve[0], color='gray', linestyle='--', linewidth=1)
        ax1.text(0.5,preAve[0]+.05,'PreCOVID ave:'+ str(round(preAve[0],2)))
        ax2.axhline(y=preAve[1], color='gray', linestyle='--', linewidth=1)  
        ax2.text(0.5,preAve[1]+.05,'PreCOVID ave:'+str(round(preAve[1],2)))
        ax3.axhline(y=preAve[2], color='gray', linestyle='--', linewidth=1)  
        ax3.text(0.5,preAve[2]+.05,'PreCOVID ave:'+str(round(preAve[2],2)))
        
        ax1.axhspan(ymin=(mins[0]),ymax=(maxes[0]),color='gray',alpha=0.25)
        ax2.axhspan(ymin=(mins[1]),ymax=(maxes[1]),color='gray',alpha=0.25)
        ax3.axhspan(ymin=(mins[2]),ymax=(maxes[2]),color='gray',alpha=0.25)
    
    #left plot stuff
    ax1.scatter(x1, y1, color=colormap)
    ax1.set_xlabel(str(xlabel), size='x-large')
    ax1.set_ylabel(ylabel, size='x-large')
    ax1.set_title(str(title1), size='x-large')
    ax1.set_ylim([0,1])
     
    #middle plot stuff
    ax2.scatter(x2, y2, color=colormap)
    ax2.set_xlabel(str(xlabel), size='x-large')
    ax2.set_title(str(title2), size='x-large')
    
    #right plot stuff
    ax3.scatter(x3, y3, color=colormap)
    ax3.set_xlabel(str(xlabel), size='x-large')
    ax3.set_title(str(title3), size='x-large')
    
    
        
    #resize the plot
    #plt.rcParams['figure.figsize'] = [8, 4]

    #bring them close together
    plt.subplots_adjust(wspace=.05, hspace=0)
    
    plt.savefig(str(savePath)+str(supTitle)+'-'+str(xlabel)+'-vs-'+str(ylabel)+'-scatter-'+str(title1)+'-'+str(title2)+'-'+str(title3)+'.png')
    
    plt.show()
    return

def plotTopMidBot(x1, y1,
                 x2,y2,
                 x3,y3,
                 title1='Plot 1',
                 title2='Plot 2',
                 title3='Plot 3', 
                 color1='grey',
                 color2='grey',
                 color3='grey',
                 xlabel='x-label',
                 ylabel='y-label',
                 savePath= 0): 
    print('done')
    
    
    
def covidScatter(x1, y1,
                 title1='Plot 1',
                 xlabel='x-label',
                 ylabel='y-label',
                 colormap = 'inferno',
                 preAve = 0,
                 aveLines = False,
                 maxes = 0,
                 mins = 0,
                 savePath= 0): 
    
    # now = datetime.now()
    # dt_string = now.strftime("%d-%m-%Y-%H")
    
    x1 = list(x1)

    if aveLines == True: 
        plt.axhline(y=preAve[0], color='gray', linestyle='--', linewidth=1)
        plt.text(0.5,preAve[0]+.05,'PreCOVID ave:'+ str(round(preAve[0],2)))     
        plt.axhspan(ymin=(mins[0]),ymax=(maxes[0]),color='gray',alpha=0.25)
        
        
    #left plot stuff
    plt.scatter(x1, y1, color=colormap)
    plt.xlabel(str(xlabel), size='x-large')
    plt.ylabel(ylabel, size='x-large')
    plt.title(str(title1), size='x-large')
    plt.ylim([0,1])
  
    #resize the plot
    #plt.rcParams['figure.figsize'] = [8, 4]

    #bring them close together
    plt.subplots_adjust(wspace=.05, hspace=0)
    
    plt.savefig(str(savePath)+str(xlabel)+'-vs-'+str(ylabel)+'-covid-scatter-'+str(title1)+'.png')
    
    plt.show()
    return    

def plotExamResults(item,
                    examsScores1,
                    examScores2,
                    savePath):
    
    
    
    plt.savefig(str(savePath)+str(item)+'exam.png')
    
    plt.show()
    print('done')