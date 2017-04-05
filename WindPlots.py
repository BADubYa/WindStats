"""
WindPlots.py

written for python 3.4 and up
"""

import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pylab as pl
import sqlite3
import csv
import datetime


FILE_LOCATION = "C:/Code Projects/_SailPython/Sailing Data_python.xlsx"
SQLITE_FILE = './sailing.db'

def fill_table_WindStats(SQLITE_FILE):
    conn = sqlite3.connect(SQLITE_FILE)
    c = conn.cursor()
    with open("Sailing Data_python.csv", 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            c.execute("""INSERT INTO WindStats (WindCategory, Date, Data) VALUES (?,?,?)""", (row[0], row[1], row[2]))
            conn.commit()
    conn.close()

def create_sailing_db(SQLITE_FILE):
    
    conn = sqlite3.connect(SQLITE_FILE)
    c = conn.cursor()
    
    """Drops all the Tables"""
    try:
        c.execute("""DROP TABLE WindStats""")
    except Exception as e: 
        pass

    """Creates Table"""
    c.execute("""CREATE TABLE WindStats (Wind_ID integer Primary Key AUTOINCREMENT, WindCategory text, Date datetime, Data integer)""")
    
    """Fills all the Tables with data"""
    fill_table_WindStats(SQLITE_FILE)

    conn.commit()
    conn.close()    

def plot_NoWind(SQLITE_FILE):
    conn = sqlite3.connect(SQLITE_FILE)
    c = conn.cursor()
    xData = []
    yData = []

    c.execute("""SELECT Data FROM WindStats WHERE WindCategory = 'No Wind'""")
    y = c.fetchall()
    for item in y:
        ydataPoint = item[0]
        yData.append(ydataPoint)

    x = range(len(yData))
    y_mean = [np.mean(yData) for i in x]
    plt.scatter(x, yData)
    mean_line = plt.plot(x, y_mean, label = 'Average', linestyle = '--')
    plt.title('No Wind Prediction (0 Knots)')
    plt.ylabel('Actual Wind Speed')
    plt.show()
 
def plot_LightWind(SQLITE_FILE):
    conn = sqlite3.connect(SQLITE_FILE)
    c = conn.cursor()
    xData = []
    yData = []

    c.execute("""SELECT Data FROM WindStats WHERE WindCategory = 'Light Wind'""")
    y = c.fetchall()
    for item in y:
        ydataPoint = item[0]
        yData.append(ydataPoint)

    x = range(len(yData))
    y_mean = [np.mean(yData) for i in x]
    plt.scatter(x, yData)
    mean_line = plt.plot(x, y_mean, label = 'Average', linestyle = '--')
    plt.title('Light Wind Prediction (5 Knots)')
    plt.ylabel('Actual Wind Speed')
    plt.show() 

def plot_ModerateWind(SQLITE_FILE):
    conn = sqlite3.connect(SQLITE_FILE)
    c = conn.cursor()
    xData = []
    yData = []

    c.execute("""SELECT Data FROM WindStats WHERE WindCategory = 'Moderate Wind'""")
    y = c.fetchall()
    for item in y:
        ydataPoint = item[0]
        yData.append(ydataPoint)

    x = range(len(yData))
    y_mean = [np.mean(yData) for i in x]
    plt.scatter(x, yData)
    mean_line = plt.plot(x, y_mean, label = 'Average', linestyle = '--')
    plt.title('Moderate Wind Prediction (10-12 Knots)')
    plt.ylabel('Actual Wind Speed')
    plt.show() 

def plot_StrongWind(SQLITE_FILE):
    conn = sqlite3.connect(SQLITE_FILE)
    c = conn.cursor()
    xData = []
    yData = []

    c.execute("""SELECT Data FROM WindStats WHERE WindCategory = 'Strong Wind'""")
    y = c.fetchall()
    for item in y:
        ydataPoint = item[0]
        yData.append(ydataPoint)

    x = range(len(yData))
    y_mean = [np.mean(yData) for i in x]
    plt.scatter(x, yData)
    mean_line = plt.plot(x, y_mean, label = 'Average', linestyle = '--')
    plt.title('Strong Wind Prediction (15-20 Knots)')
    plt.ylabel('Actual Wind Speed')
    plt.show() 

"""
def main():
    create_sailing_db(SQLITE_FILE)
    plot_NoWind(SQLITE_FILE)
    plot_LightWind(SQLITE_FILE)
    plot_ModerateWind(SQLITE_FILE)
    plot_StrongWind(SQLITE_FILE)
"""

if __name__=="__main__":
    pass


