#Extracting longitude and latitude for map visualization by following columns

#start stations name, end station name, start and end station longitudes and latitudes
import pandas as pd

data1 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Oct-Dec 2018/Oct-Dec_2018.csv')
data2 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Jan-Mar 2019/Jan-Mar_2019.csv')
data3 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Apr-Jun 2019/Apr_Jun_2019.csv')
data4 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/post/July-Sep_2019.csv')



map_data1 = data1[['tripduration', 'start station id', 'end station id','start station name', 'end station name', 'start station longitude', 'start station latitude', 
                    'end station longitude', 'end station latitude']]


map_data2 = data2[['tripduration', 'start station id', 'end station id','start station name', 'end station name', 'start station longitude', 'start station latitude', 
                    'end station longitude', 'end station latitude']]


map_data3 = data3[['tripduration', 'start station id', 'end station id','start station name', 'end station name', 'start station longitude', 'start station latitude', 
                    'end station longitude', 'end station latitude']]

map_data4 = data4[['tripduration', 'start station id', 'end station id','start station name', 'end station name', 'start station longitude', 'start station latitude', 
                    'end station longitude', 'end station latitude']]



map_data1.to_csv('Map_data1.csv')
