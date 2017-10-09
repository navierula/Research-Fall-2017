import pandas as pd

# read in dataset
xl = pd.ExcelFile("data/130N_Cycles_1-47.xlsx")
df = xl.parse("Specimen_RawData_1")
df

"""

This is what the dataset currently looks like - it has 170,101 rows and two columns.
The dataset contains data from 47 cycles following an experiment. 
The output of these experiments form the two columns:<br>
 - time (seconds)
 - load (exerted force, in Newtons)

My task is to find the local maxima and minima in the dataset, and mark these values in a 
database. Initially, the database will consist of four columns: time, load, max, and min. 
It can be modified or condensed later on to fit further requirements.

 This is the criteria I will use to find the maxima:
 - write each row in the db to a cache
 - initialize a flag value to false
 - if the force in the previous row is smaller than the force in the next row, write the new row to the cache (leave the flag as false)
 - if the force in the previous row is bigger than the force in the next row, write the new row to cache and mark it as a max cycle 
(change the flag to true)

This is the criteria I will use to find the minima:
 - write each row in the db to a cache
 - initialize a flag value to false
 - if the force in the previous row is bigger than the force in the next row, write the new row to the cache (leave the flag as false)
 - if the force in the previous row is smaller than the force in the next row, write the new row to the cache and mark it as a min cycle 
 (change the flag to true)
 

"""

# append data from time column to list
time = []
for item in df.index:
    time.append(df["Time"][item])

# append data from load column to list
load = []
for item in df.index:
    load.append(df["Load"][item])

# create list of tuples for time and load
data = []
for i, j in zip(time, load):
    data.append((i,j))
    
max_data = []
for idx, item in enumerate(data):
    if idx > 0:
        # next_item, prev_item
        print(item[1], data[idx-1])
    
    
li = range(10)

for i, item in enumerate(li):
    if i > 0:
        print(item, li[i-1])
    


#max_data = []
#flag = False
#for item in data:
#    
#    
#    
#    new.append(item + (,))
#print(new)

