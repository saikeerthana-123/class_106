import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Marks = []
    Attendence = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Attendence.append(float(row["Days Present"]))
        
    return {"x":Marks, "y":Attendence}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation Between Marks In Percentage vs Days Present:- \n", corelation[0,1])

def setup():
    data_path = "student.csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)

setup()