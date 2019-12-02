import pandas as pd

data1 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Oct-Dec 2018/Oct-Dec_2018.csv')
data2 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Jan-Mar 2019/Jan-Mar_2019.csv')
data3 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Apr-Jun 2019/Apr_Jun_2019.csv')
data4 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/post/July-Sep_2019.csv')

data1.head()

#Gender
data1['gender'].replace([0, 1, 2], ['Unknown', 'Male', 'Female'], inplace = True)
 
data2['gender'].replace([0, 1, 2], ['Unknown', 'Male', 'Female'], inplace = True)

data3['gender'].replace([0, 1, 2], ['Unknown', 'Male', 'Female'], inplace = True)

data4['gender'].replace([0, 1, 2], ['Unknown', 'Male', 'Female'], inplace = True)

#Add age column
current_year = 2019
data1['age'] = current_year - data1['birth year']
data2['age'] = current_year - data2['birth year']
data3['age'] = current_year - data3['birth year']
data4['age'] = current_year - data4['birth year']

user_data1 = data1[['bikeid', 'tripduration', 'starttime', 'stoptime', 'usertype', 'birth year', 'gender', 'age']]
user_data2 = data2[['bikeid', 'tripduration', 'starttime', 'stoptime', 'usertype', 'birth year', 'gender', 'age']]
user_data3 = data3[['bikeid', 'tripduration', 'starttime', 'stoptime', 'usertype', 'birth year', 'gender', 'age']]
user_data4 = data4[['bikeid', 'tripduration', 'starttime', 'stoptime', 'usertype', 'birth year', 'gender', 'age']]

user_data1.to_csv("user_data1.csv")
user_data2.to_csv("user_data2.csv")
user_data3.to_csv("user_data3.csv")
user_data4.to_csv("user_data4.csv")