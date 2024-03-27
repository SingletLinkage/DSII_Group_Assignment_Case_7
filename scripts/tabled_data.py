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
price_stats=price_stats.drop(price_stats.index)
price_stats['N']=data['Price'].count()
price_stats['Mean']=data['Price'].mean()
price_stats['Median']=data['Price'].median()
price_stats['Mode']=data['Price'].mode().values[0]
price_stats['Standard Deviation']=data['Price'].std()
price_stats['Variance']=data['Price'].var()
price_stats['Minimum']=data['Price'].min()
price_stats['Maximum']=data['Price'].max()
price_stats['25 percentile']=data['Price'].quantile(0.25)
price_stats['50 percentile']=data['Price'].quantile(0.50)
price_stats['75 percentile']=data['Price'].quantile(0.75)    
price_stats=price_stats.round(2)

shade_stats = data['Shades'].describe()
shade_stats=shade_stats.drop(shade_stats.index)
shade_stats['N']=data['Shades'].count()
shade_stats['Mean']=data['Shades'].mean()
shade_stats['Median']=data['Shades'].median()
shade_stats['Mode']=data['Shades'].mode().values[0]
shade_stats['Standard Deviation']=data['Shades'].std()
shade_stats['Variance']=data['Shades'].var()
shade_stats['Minimum']=data['Shades'].min()
shade_stats['Maximum']=data['Shades'].max()
shade_stats['25 percentile']=data['Shades'].quantile(0.25)
shade_stats['50 percentile']=data['Shades'].quantile(0.50)
shade_stats['75 percentile']=data['Shades'].quantile(0.75)
shade_stats=shade_stats.round(2)

stats = pd.concat([price_stats, shade_stats], axis=1)
stats.columns = ['Price', 'Shades']

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')
ax.set_title('Descriptive Statistics')  # Set the title
table = ax.table(cellText=stats.values, colLabels=stats.columns, rowLabels=stats.index, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(13)
table.scale(0.9, 1.8)

# Access all cells
cells = table.get_celld()

# Iterate over the cells and set the facecolor
for cell in cells.values():
    cell.set_facecolor('white')

cells[0, 0].set_facecolor('coral')
cells[0, 1].set_facecolor('coral')
for i in range(1,12):
    cells[i, -1].set_facecolor('lightblue')
cells[0, 0].set_text_props(weight='bold')
cells[0, 1].set_text_props(weight='bold')
plt.show()


