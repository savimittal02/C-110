import csv
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random
import pandas as pd

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()

def randomSetOfMean(counter):
    dataSet =[]
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean


def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["average"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines", name = "MEAN"))
    fig.show()


def setup():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)

    showFig(meanList)
    mean = statistics.mean(meanList)
    print("mean of sampling distribution",mean)

setup()

def stdev():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)

    #showFig(meanList)
    stdev = statistics.stdev(meanList)
    print("stdev of sampling distribution",stdev)

stdev()
    
