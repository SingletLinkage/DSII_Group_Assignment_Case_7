import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import os
#print(style.available)
# according to the version available, use either seaborn-darkgrid or seaborn-v0_8-daarkgrid
style.use('seaborn-v0_8-darkgrid')

# Create a DataFrame with data from Indonesian Lip Products
database = pd.read_csv('./source_files/actual_data_indonesia.csv')

shades = database['Shades'].unique()
products = database.groupby('Shades').size()

fig, ax = plt.subplots(figsize=(13, 9))

cmap = plt.cm.bwr

# Normalize the shade counts to the range [0, 1] for colormap mapping
norm = plt.Normalize(min(products), max(products))

# Map the shade counts to colors using the colormap
colors = [cmap(norm(count)) for count in products]

# Create a horizontal bar plot
ax.barh(shades, products, color=colors)

# Add labels and title
ax.set_xlabel('Number of Shades', fontsize=20)
ax.set_ylabel('Number of Products', fontsize=20)
ax.set_title('Number of Products by Number of Available Shades', fontsize=30)

# Show color bar for reference
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
#plt.colorbar(sm, label='Count of Shades')

# Show the plot
#plt.savefig(os.path.join(os.getcwd(), 'images', 'TotalProductsByShades.pdf'))
plt.show()
