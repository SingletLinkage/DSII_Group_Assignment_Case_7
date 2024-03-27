"Print mean,median,mode,stardard deviation,variance,quartile 1 and 3,interquartile  of the price and shades column in tabular format. take help of matplotlib in displaying the data in tabular format."

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.style as style


# Setting the style
style.use('Solarize_Light2')
data=pd.read_csv('source_files\\actual_data_indonesia.csv')
data['Price'] = data['Price'].astype(float)
data['Shades'] = data['Shades'].astype(float)

# Calculate statistics
price_stats = data['Price'].describe()
price_stats['mode'] = data['Price'].mode().values[0]
price_stats['variance'] = data['Price'].var()
price_stats['IQR'] = price_stats['75%'] - price_stats['25%']

shade_stats = data['Shades'].describe()
shade_stats['mode'] = data['Shades'].mode().values[0]
shade_stats['variance'] = data['Shades'].var()
shade_stats['IQR'] = shade_stats['75%'] - shade_stats['25%']

stats = pd.concat([price_stats, shade_stats], axis=1)
stats.columns = ['Price', 'Shades']

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
table = ax.table(cellText=stats.values, colLabels=stats.columns, rowLabels=stats.index, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 1.2)

# Access all cells
cells = table.get_celld()

# Iterate over the cells and set the facecolor
for cell in cells.values():
    cell.set_facecolor('white')

cells[0, 0].set_facecolor('coral')
cells[0, 1].set_facecolor('coral')
for i in range(1,9):
    cells[i, -1].set_facecolor('lightblue')

plt.show()

plt.show()
