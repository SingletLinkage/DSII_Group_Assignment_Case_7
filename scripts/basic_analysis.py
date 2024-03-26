
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('source_files\\actual_data_indonesia.csv')
plt.figure(figsize=(10, 6))
plt.hist(data['Price'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Lip Product Prices')
plt.xlabel('Price')
plt.xticks(rotation=90)
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


data['Price'] = data['Price'].str.replace(',', '').astype(float)

# Plot box plot with color and percentiles
plt.figure(figsize=(8, 6))
plt.boxplot(data['Price'], vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'))  
# Specify vert=True for vertical orientation, patch_artist=True for box color

# Add horizontal lines for percentiles
percentiles = [0, 10, 25, 50, 75, 90, 100]
percentile_values = [data['Price'].quantile(p/100) for p in percentiles]
colors = ['gray', 'red', 'orange', 'green', 'blue', 'purple', 'black']
linestyles = ['--', '--', '--', '-', '--', '--', '--']
labels = ['0th percentile', '10th percentile', '25th percentile', '50th percentile (median)', 
          '75th percentile', '90th percentile', '100th percentile']

for i in range(len(percentiles)):
    plt.axhline(y=percentile_values[i], color=colors[i], linestyle=linestyles[i], label=labels[i])

plt.title('Box Plot of Lip Product Prices with Percentiles')
plt.ylabel('Price')
plt.legend()  # Show legend
plt.grid(True, axis='y')  # Show gridlines along the y-axis
plt.show()