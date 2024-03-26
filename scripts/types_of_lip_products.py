import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
data = pd.read_csv("C:\GIT\DSII_Group_Assignment_Case_7\source_files\data_indonesia.csv")
print(data)

types = {}
print(data.columns)
d = data["Type of Lip Product"]


print("Type of Lip product and their frequencies")
print(d)
d = dict(d)
#print(d)
for i in d :
    if d[i].lower() not in types :
        types[d[i].lower()]=1
    else :
        types[d[i].lower()]+=1
print()
for i in types :
    print(i.capitalize(),":",types[i])
type_of_prod = list(types.keys())
number = list(types.values())
tot = sum(number)
percentage = []
for i in number :
    percentage.append(i/tot)



# Data to plot
explode = (0.1, 0.1, 0.1, 0.1)  

fig = plt.figure()
plt.pie(percentage, explode=explode, labels=type_of_prod, autopct='%1.1f%%', startangle=140)
plt.show()
plt.title('Percentage by brand')

