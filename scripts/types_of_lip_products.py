import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
data = pd.read_csv("source_files\\data_indonesia.csv")
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
print(types)
type_of_prod = list(types.keys())
number = list(types.values())
tot = sum(number)
percentage = []
for i in number :
    percentage.append(i/tot)

# plt.pie(percentage, labels = type_of_prod )
# plt.show() 


# Data to plot
explode = (0.1, 0.1, 0.1, 0.1)  
# Plot
#plt.figure(figsize=(8, 6))  # Aspect ratio 4:3

fig = plt.figure()
plt.pie(percentage, explode=explode, labels=type_of_prod, autopct='%1.1f%%', startangle=140)
plt.show()
plt.title('Percentage by brand')

# Equal aspect ratio ensures that pie is drawn as a circle
#plt.axis('equal')

# Show plot
#plt.show()



# print(types)
# print((data['Type of Lip Product'].loc(0)).value)
#print(data.get_loc(data['Type of Lip Product'].index[0]))
# #print(data.data.columns[2]) # types
# for i in data :
#     if data.loc(data['Index']==i)['Type of Lip Product'] not in types :
#         types[data['Type of Lip Product']] = 1
#     else :
#         types[data["Type of Lip Product"][i]] += 1