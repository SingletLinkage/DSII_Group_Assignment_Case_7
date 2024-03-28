import matplotlib.pyplot as plt
import matplotlib.style as style
import pandas as pd

style.use('seaborn-v0_8-darkgrid')


data=pd.read_csv('source_files/actual_data_indonesia.csv')

y = data['Brand'].value_counts(sort=False)
x = data['Brand'].unique()

plt.figure(figsize=(14, 9))

plt.barh(x, y, color='aqua', edgecolor='black')
plt.xlabel('Frequency', fontsize=15)
plt.ylabel('Brands', fontsize=15)
plt.title('Frequency of Lip Product by Brands', fontsize=20)
plt.savefig('images/Brand_Frequency.pdf')



