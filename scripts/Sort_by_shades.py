""" we can also create a distribution whidch shows the percentage of products by number of shades.
then we can create a histogram to organize this. We will get some outliers and graphs.  
Now using this, we can make a boxplot - which is basically classifying data into different quantiles """
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.style as style

# Setting the style
style.use('Solarize_Light2')

# Load data
data=pd.read_csv('source_files\\actual_data_indonesia.csv')

# Ensure 'Shades' is numeric for the purpose of this example
shade_counts = data['Shades'].value_counts()

plt.figure(figsize=(10, 6))
plt.barh(shade_counts.index, shade_counts.values, color='aqua', edgecolor='black')
plt.title('Bar Plot of Lip Product Shades')
plt.xlabel('Frequency')
plt.ylabel('Shades')
plt.grid(True)
plt.show()
