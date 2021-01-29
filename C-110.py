import csv
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random
import pandas as pd

df = pd.read_csv("newdata.csv")
avg = df["average"].tolist()
avgmean = statistics.mean(avg)
avgstd = statistics.stdev(avg)
fig = ff.create_distplot([avg],["average"],show_hist = False)
fig.add_trace(go.Scatter(x = [avgmean,avgmean],y = [0,1],mode = "lines", name = "MEAN"))

fig.show()
print(avgmean)
print(avgstd)

