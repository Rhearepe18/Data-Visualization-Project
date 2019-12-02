#Peak hours
#Winter-October - March 
#Summer-April-September

import pandas as pd
import csv

userinfo1 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/userinfo/user_data1.csv')
userinfo2 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/userinfo/user_data2.csv')
userinfo3 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/userinfo/user_data3.csv')
userinfo4 = pd.read_csv('/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/userinfo/user_data4.csv')

#Change format to datetime and time to hours:minutes
userinfo1['starttime'] = pd.to_datetime(userinfo1['starttime'])
userinfo1['stoptime'] = pd.to_datetime(userinfo1['stoptime'])

userinfo1['starttime'] = userinfo1['starttime'].dt.strftime('%Y-%m-%d %H:%M')
userinfo1['stoptime'] = userinfo1['stoptime'].dt.strftime('%Y-%m-%d %H:%M')


userinfo2['starttime'] = pd.to_datetime(userinfo2['starttime'])
userinfo2['stoptime'] = pd.to_datetime(userinfo2['stoptime'])

userinfo2['starttime'] = userinfo2['starttime'].dt.strftime('%Y-%m-%d %H:%M')
userinfo2['stoptime'] = userinfo2['stoptime'].dt.strftime('%Y-%m-%d %H:%M')



userinfo3['starttime'] = pd.to_datetime(userinfo3['starttime'])
userinfo3['stoptime'] = pd.to_datetime(userinfo3['stoptime'])

userinfo3['starttime'] = userinfo3['starttime'].dt.strftime('%Y-%m-%d %H:%M')
userinfo3['stoptime'] = userinfo3['stoptime'].dt.strftime('%Y-%m-%d %H:%M')

userinfo4['starttime'] = pd.to_datetime(userinfo4['starttime'])
userinfo4['stoptime'] = pd.to_datetime(userinfo4['stoptime'])

userinfo4['starttime'] = userinfo4['starttime'].dt.strftime('%Y-%m-%d %H:%M')
userinfo4['stoptime'] = userinfo4['stoptime'].dt.strftime('%Y-%m-%d %H:%M')


#Sort data by time counts by start time
peaktimes1 = userinfo1.groupby(['starttime']).size().reset_index(name='counts')
peak_hours1 = peaktimes1.sort_values('counts', ascending=False)

peaktimes2 = userinfo2.groupby(['starttime']).size().reset_index(name='counts')
peak_hours2 = peaktimes2.sort_values('counts', ascending=False)

peaktimes3 = userinfo3.groupby(['starttime']).size().reset_index(name='counts')
peak_hours3 = peaktimes3.sort_values('counts', ascending=False)

peaktimes4 = userinfo4.groupby(['starttime']).size().reset_index(name='counts')
peak_hours4 = peaktimes4.sort_values('counts', ascending=False)


#Save to csv

peak_hours1.to_csv("Peakhours1.csv")
peak_hours2.to_csv("Peakhours2.csv")
peak_hours3.to_csv("Peakhours3.csv")
peak_hours4.to_csv("Peakhours4.csv")

#Sort data by time counts by end time

end_time1 = userinfo1.groupby(['stoptime']).size().reset_index(name='counts')
end_hours1 = end_time1.sort_values('counts', ascending=False)

end_time2 = userinfo2.groupby(['stoptime']).size().reset_index(name='counts')
end_hours2 = end_time2.sort_values('counts', ascending=False)

end_time3 = userinfo3.groupby(['stoptime']).size().reset_index(name='counts')
end_hours3 = end_time3.sort_values('counts', ascending=False)

end_time4 = userinfo4.groupby(['stoptime']).size().reset_index(name='counts')
end_hours4 = end_time4.sort_values('counts', ascending=False)

#Save to csv
end_hours1.to_csv("Endhours1.csv")

end_hours2.to_csv("Endhours2.csv")

end_hours3.to_csv("Endhours3.csv")

end_hours4.to_csv("Endhours4.csv")
