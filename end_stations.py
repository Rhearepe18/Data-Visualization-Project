import csv
import pandas as pd


#Data

data1 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Oct-Dec 2018/Oct-Dec_2018.csv')

topstation1 = data1.groupby(['end station name']).size().reset_index(name='counts')

data2 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Jan-Mar 2019/Jan-Mar_2019.csv')
topstation2 = data2.groupby(['end station name']).size().reset_index(name='counts')

data3 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Apr-Jun 2019/Apr_Jun_2019.csv')
topstation3 = data3.groupby(['end station name']).size().reset_index(name='counts')

data4 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/post/July-Sep_2019.csv')
topstation4 = data4.groupby(['end station name']).size().reset_index(name='counts')


topstation1.to_csv('top_endstations1.csv')
topstation2.to_csv('top_endstations2.csv')
topstation3.to_csv('top_endstations3.csv')
topstation4.to_csv('top_endstations4.csv')