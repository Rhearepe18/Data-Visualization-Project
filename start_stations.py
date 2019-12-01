import csv
import pandas as pd


#October-December 2018
data1 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Oct-Dec 2018/Oct-Dec_2018.csv')
data1.head()


topstation1 = data.groupby(['start station name']).size().reset_index(name='counts')
top_quarter1 = topstation1.sort_values('counts', ascending=False).head(10)


bottomstation1 = data1.groupby(['start station name']).size().reset_index(name='counts')
bottom_quarter1 = bottomstation1.sort_values('counts', ascending=True).head(10)

#Jan-March 2019

data2 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Jan-Mar 2019/Jan-Mar_2019.csv')
data2.head()


topstation2 = data2.groupby(['start station name']).size().reset_index(name='counts')
top_quarter2 = topstation2.sort_values('counts', ascending=False).head(10)



bottomstation2 = data2.groupby(['start station name']).size().reset_index(name='counts')
bottom_quarter2 = bottomstation2.sort_values('counts', ascending=True).head(10)


#Apr-June 2019

data3 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Apr-Jun 2019/Apr_Jun_2019.csv')
data3.head()


topstation3 = data3.groupby(['start station name']).size().reset_index(name='counts')
top_quarter3 = topstation3.sort_values('counts', ascending=False).head(10)



bottomstation3 = data3.groupby(['start station name']).size().reset_index(name='counts')
bottom_quarter3 = bottomstation3.sort_values('counts', ascending=True).head(10)

#July-Sept 2019

data4 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/post/July-Sep_2019.csv')
data4.head()


topstation4 = data4.groupby(['start station name']).size().reset_index(name='counts')
top_quarter4 = topstation4.sort_values('counts', ascending=False).head(10)



bottomstation4 = data4.groupby(['start station name']).size().reset_index(name='counts')
bottom_quarter4 = bottomstation4.sort_values('counts', ascending=True).head(10)


#Convert top start stations to csv
topstation1.to_csv('top_stations1.csv')
topstation2.to_csv('top_stations2.csv')
topstation3.to_csv('top_stations3.csv')
topstation4.to_csv('top_stations4.csv')