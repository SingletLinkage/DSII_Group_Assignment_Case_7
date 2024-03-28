import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import os

style.use('seaborn-v0_8-darkgrid')

# Create a DataFrame with data from Indonesian Lip Products
database = pd.read_csv('./source_files/actual_data_indonesia.csv')

products = database['Lip Product']
shades = database['Shades']

fig, ax = plt.subplots(figsize=(25, 9))

cmap = plt.cm.bwr

# Normalize the shade counts to the range [0, 1] for colormap mapping
norm = plt.Normalize(np.percentile(shades, 10), np.percentile(shades, 90))

# Map the shade counts to colors using the colormap
colors = [cmap(norm(count)) for count in shades]

# Create a horizontal bar plot
ax.barh(products, shades, color=colors)

# Add labels and title
ax.set_xlabel('Number of Shades', fontsize=20)
ax.set_ylabel('Products', fontsize=20)
ax.set_title('Number of Shades by Products', fontsize=30)

# # Show color bar for reference
# sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
# sm.set_array([])
# plt.colorbar(sm, label='Count of Shades')

# Show the plot
plt.savefig(os.path.join(os.getcwd(), 'images', 'TotalShadesByProduct.pdf'), dpi=800)