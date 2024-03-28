import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("source_files/actual_data_indonesia.csv")
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

fig, ax = plt.subplots()

# Outer circle
pie, labels, autotexts = ax.pie(percentage, labels=type_of_prod, autopct='%1.0f%%', startangle=140, labeldistance=1.05)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

for label in labels:
    label.set_fontsize(15)
for autotext in autotexts:
    autotext.set_fontsize(15)

# Draw a white circle at the center to make it look like a donut
center_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(center_circle)

plt.title('Percentage by Type', fontsize=25)

plt.show()