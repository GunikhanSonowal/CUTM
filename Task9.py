#Question number 9
#My system very old and so unable to show the graphic design means unable to install matplotiib
import pandas as pd
import numpy as np
import csv
import numpy as np
#import matplotlib as plt
def addition(list):
    sum = 0
    for i in list:
        sum = sum+i
    return sum
    


filename = 'canada.csv'
data = pd.read_csv(filename)


#display header name in list
print "The header name of the dataset before rename and dropping", data.columns.tolist()

#Remove unnecessary columns using Python code.
data.drop(["Type", "Coverage", "AREA", "REG", "DEV", "DevName"], inplace = True, axis=1) 

#rename the columans
data.rename(columns = {"OdName": "Country", "AreaName":"Continent",  "RegName": "Region"}, inplace=True)

#display header name in list
print "The header name of the dataset after modification", data.columns.tolist()

print "The size of dataset", data.shape[0]


i = 0
sum = 0
list1 = []
list2=[]
dict = {}
for row in range(1, data.shape[0]-1):
    
    list1= data.values[row]
    list2= list1[3:-1].tolist()
    l2 = [int(v) for v in list2]
    dict[list1[0]]= addition(l2)

#print dict
sorted_list = []
sorted_list1 = []
max_key = max(dict, key=dict.get)
print "The highest immigration from 1980 to 2013 is ", max_key
min_key = min(dict, key=dict.get)
print "The lowest immigration from 1980 to 2013. is ", min_key


print "10 countries with highest immigration to Canada"
sorted_list =  sorted(dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)

for i in range(10):
    print sorted_list[i]


print "10 countries with lowest immigration to Canada"
sorted_list1 =  sorted(dict.items(), key = lambda kv:(kv[1], kv[0]))

for i in range(10):
    print sorted_list1[i]


# pos = np.arange(len(dict.keys()))
# width = 1.0     # gives histogram aspect to the bar diagram

# ax = plt.axes()
# ax.set_xticks(pos + (width / 2))
# ax.set_xticklabels(dict.keys())

# plt.bar(dict.keys(),  width, color='g')
# #          ^^^^^^ what should I put here?
# plt.show()


        
if __name__ == "__main__":
    pass
    #fp = open("test1.txt", "r")
    #print smishing_verify(fp.read())
