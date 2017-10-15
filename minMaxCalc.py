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

# apply algorithm for finding maxima in data    
max_data = []
for idx, item in enumerate(data):
    prev = data[idx-1][1]
    curr = item[1]
    if prev > curr:
        max_data.append(item + ("max",))
    else:
        max_data.append(item + ("",))
            
# apply algorithm for finding minima in data    
min_data = []
for idx, item in enumerate(max_data):
    # idx > 0
    prev = max_data[idx-1][1]
    curr = item[1]
    if prev < curr:
        min_data.append(item + ("min",))
    else:
        min_data.append(item + ("",))

all_data = min_data

# count maxima number
max_count = 0
for item in all_data:
    if item[2] == "max":
        max_count += 1 
#print(max_count)

# count minima number
min_count = 0
for item in all_data:
    if item[3] == "min":
        min_count += 1 
#print(min_count)

##############################################################################
    
# create db model
db = []

# create cache store
cache = []

for idx, item in enumerate(data):
    if idx > 0:
        prev = data[idx-1][1]
        curr = item[1]
        if prev > curr:
            cache.append(data[idx-1] + ("max",))
        else:
            cache.append(data[idx-1] + ("",))
            
            
"""
db 
_______
10

cache 
_______
10

info1
10 
5
2
40

info2
2
5
10
40


"""
trial_lst = load

#trial_lst = [0.5, 3, 6, 40, 90, 130.8, 129, 111, 8, 9, 0.01, 9, 40, 90, 130.1, 112, 108, 90, 77, 68, 0.9, 8, 40, 90, 92, 130.4]
#trial_lst = load
#indices = [x[0] for x in enumerate(map(lambda x:x<1, trial_lst)) if x[1]]
#print(indices)
#
#sublists = [trial_lst[i:j] for i,j in list(zip([0]+indices, indices+[None]))[1:]]
#
#for i,l in enumerate(sublists):
#    print(i, max((v,i) for (i,v) in enumerate(l)), min((v,i) for (i,v) in enumerate(l)))
    
trial_lst.sort(key=int)

totals = []

for count, items in enumerate(trial_lst):

    counter = count + 1
    last_object = (counter, trial_lst[count], trial_lst[(len(trial_lst)-1) - count])

    totals.append(last_object)
    
print(totals[:80])