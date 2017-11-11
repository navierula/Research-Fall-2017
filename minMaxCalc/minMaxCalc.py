atimport pandas as pd

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
    
lst = load

def get_groups(lst):
    up = False
    for i, (u, v) in enumerate(zip(lst, lst[1:])):
        if up:
            if v < u:
                yield 'End', i, u
                up = False
        else:
            if v > u:
                yield 'Start', i, u
                up = True
    if up:
        yield 'End', i + 1, lst[-1]


gen = get_groups(lst)
for i, (t1, t2) in enumerate(zip(gen, gen), 1):
    print(i, t1, t2)
    




#indices = [x[0] for x in enumerate(map(lambda x:x<1, trial_lst)) if x[1]]
#
#sublists = [trial_lst[i:j] for i,j in list(zip([0]+indices, indices+[None]))[1:]]
#
#count = 0
#for i,l in enumerate(sublists):
#    if count < 50:
#        print(i, max((v,i) for (i,v) in enumerate(l)), min((v,i) for (i,v) in enumerate(l)))
#        count += 1

##############################################################################
    
## create db model
#db = []
#
## create cache store
#cache = []
#
#load.sort(key=float) # previously key = int
#
#totals = []
#
#for count, items in enumerate(load):
#
#    counter = count + 1
#    last_object = (counter, load[count], load[(len(load)-1) - count])
#
#    totals.append(last_object)
#    
#our_totals = totals[:47]
#print(our_totals)
#
## append max and min label to relevant rows
#combine_data = []
#for i in data:
#    flag = 0
#    for j in our_totals:
#        if i[1] == j[1]:
#            combine_data.append(i + ("min",))
#            flag = 1
#        if i[1] == j[2]:
#            combine_data.append(i + ("max",))
#            flag = 1
#    if flag == 0:
#        combine_data.append(i + ("NA",))
#        
#all_experiment_data = []
#current_experiment_data = []
#for item in combine_data:
#    index, _, point_type = item
#    if point_type=="min" and current_experiment_data: #Starting a new experiment, flush the old one
#        all_experiment_data.append(current_experiment_data)
#        current_experiment_data = []
#    current_experiment_data.append(index)
#
##Flush the last experiment
#all_experiment_data.append(current_experiment_data)
#
## for item in all_experiment_data:
##     print(item)
#
#
#
#final = []
#for item in all_experiment_data:
#    final.append(item[-1]-item[0])
#    
#        
## min_sums = []
## max_sums = []
## for x, _, what in combine_data:
##     if what != 'NA':
##         current = min_sums if what == 'min' else max_sums
##         current.append(0)
##     current[-1] += x
#    
#
#
## try with smaller example before moving on!!
#
##cooling_time = 0
##heating_time = 0
##for item in combined_data:
##    if item[2] == "min":
##
#
#            
#    
#
#
#with open("cycleStartEnd.txt", "w") as fp:
#    for item in totals[:47]:
#        fp.write("Cycle: %s" % item[0] + "\n")
#        fp.write("Starting force: %s" % item[1] + "\n")
#        fp.write("Ending force: %s" % item[2] + "\n\n")
#        fp.write("Cooling time: %s" % j + "\n")
#        fp.write("Heating time: %s" % i + "\n")
        
    
        
    