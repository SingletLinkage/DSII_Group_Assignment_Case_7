import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.style as style

# Setting the style
style.use('seaborn-v0_8-darkgrid')

# Load data
# data=pd.read_csv('source_files/actual_data_indonesia.csv')
data=pd.read_csv('source_files/india_data.csv')


# Ensure 'Shades' is numeric for the purpose of this example
shade_counts = data['Shades'].value_counts()


x = shade_counts.index
y = shade_counts.values
coefficients = np.polyfit(x, y, 4)  # Use a degree of 2 for a curve
polynomial = np.poly1d(coefficients)
ys = polynomial(x)

plt.figure(figsize=(10, 6))
plt.barh(shade_counts.index, shade_counts.values, color='aqua', edgecolor='black')
x_smooth = np.linspace(x.min(), x.max(), 500)  # Change 500 to the number of points you want
ys_smooth = polynomial(x_smooth)
plt.plot(ys_smooth, x_smooth, color='red') # Add the curve
plt.title('Bar Plot of Lip Product Shades')
plt.xlabel('Frequency')
plt.ylabel('Shades')
plt.grid(True)
plt.savefig('images/India-graphs/KDE_Shades.pdf')