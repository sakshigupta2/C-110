import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import pandas as pd 
import csv
import random
import statistics
df = pd.read_csv("data.csv")
templist = df["temp"].to_list()
fig = ff.create_distplot([templist],["Temperature"])
#fig.show()
tempmean = statistics.mean(templist)
tempmedian = statistics.median(templist)
tempmode = statistics.mode(templist)
tempstdDev = statistics.stdev(templist)
print("Mean, Median, Mode of the data is {}, {}, {} respectively".format(tempmean, tempmedian, tempmode))
print("Standard Deviation of the data is {}".format(tempstdDev))
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(templist)-1)
        value = templist[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
def showFig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([templist],["Temperature"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2], mode = "lines", name = "Mean"))
    fig.show()
def setUp():
    mean_list = []
    for i in range(0,1000):
        SetOfMean = randomSetOfMean(100)
        mean_list.append(SetOfMean)
    showFig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of the sampling: ", mean)

setUp()
def standardDeviation():
    mean_list = []
    for i in range(0,1000):
        SetOfMean = randomSetOfMean(100)
        mean_list.append(SetOfMean)
    stdDev = statistics.stdev(mean_list)
    print("Standard Deviation of the Sample: ",stdDev)
standardDeviation()

    
