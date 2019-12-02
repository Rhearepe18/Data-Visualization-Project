import os
import glob
import pandas as pd
import os
os.chdir("/Users/rhearepe/Documents/Financial Analytics/Sem 3/Data Visualization/citibike/2019/pre/Apr-Jun 2019")


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "Apr_Jun_2019.csv", index=False, encoding='utf-8-sig')