import matplotlib.pyplot as plt
import matplotlib.style as style
import pandas as pd

style.use('seaborn-v0_8-darkgrid')

# data=pd.read_csv('source_files/actual_data_indonesia.csv')
data=pd.read_csv('source_files/india_data.csv')

result_db = pd.DataFrame({
        'Frequency' : data['Type of Lip Product'].value_counts(sort=False),
        'Percentage' : data['Type of Lip Product'].value_counts(normalize=True, sort=False)*100,
        'Cumulative Percentage' : round(data['Type of Lip Product'].value_counts(normalize=True, sort=False).cumsum()*100, 2)
}, index=data['Type of Lip Product'].unique())

# print(result_db.to_string())
result_db.to_csv('source_files/india_type_freq_cumufreq.csv')

x = data['Type of Lip Product'].unique()
y = data['Type of Lip Product'].value_counts(sort=False)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5']

fig, ax = plt.subplots(2, 1, figsize=(15, 19))
ax[0].bar(x, y, width=0.8, color=colors)
ax[0].set_xticklabels(x, fontsize=12, rotation=20)
ax[0].set_xlabel('Type of Lip Products', fontsize=20)
ax[0].set_ylabel('Frequency', fontsize=20)
ax[0].set_title('Frequency of Products by Type of Lip Product', fontsize=25)


# Outer circle
_, labels = ax[1].pie(result_db['Percentage'], startangle=140, colors=colors)
ax[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

for label in labels:
    label.set_fontsize(15)

# Draw a white circle at the center to make it look like a donut
center_circle = plt.Circle((0, 0), 0.7, color='white')
ax[1].add_artist(center_circle)
ax[1].set_title('Percentage of Products by Type of Lip Product', fontsize=25)

# Create legend based on data
legend_labels = [f'{label}: {percent:.0f}%' for label, percent in zip(x, result_db['Percentage'])]
ax[1].legend(legend_labels, loc='upper right', fontsize=13, title='Legend')

# plt.show()
plt.savefig('images/India-graphs/TotalProductsbyType.pdf')
