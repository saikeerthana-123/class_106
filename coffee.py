import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    CoffeeConsumed = []
    Sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            CoffeeConsumed.append(float(row["Coffee in ml"]))
            Sleep.append(float(row["sleep in hours"]))
        
    return {"x":CoffeeConsumed, "y":Sleep}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation Between Coffee in ml vs sleep in hours:- \n", corelation[0,1])

def setup():
    data_path = "coffee.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

setup()