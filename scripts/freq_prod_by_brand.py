import matplotlib.pyplot as plt
import matplotlib.style as style
import pandas as pd

style.use('seaborn-v0_8-darkgrid')

# data=pd.read_csv('source_files/actual_data_indonesia.csv')
data=pd.read_csv('source_files/india_data.csv')


result_db = pd.DataFrame({
        'Frequency' : data['Brand'].value_counts(sort=False),
        'Percentage' : data['Brand'].value_counts(normalize=True, sort=False)*100,
        'Cumulative Percentage' : round(data['Brand'].value_counts(normalize=True, sort=False).cumsum()*100, 2)
}, index=data['Brand'].unique())

# print(result_db.to_string())
result_db.to_csv('source_files/india_brand_freq_cumufreq.csv')

x = data['Brand'].unique()
y = data['Brand'].value_counts(sort=False)

fig, ax = plt.subplots(figsize=(13, 15))
plt.bar(x, y, width=0.8)
plt.xticks(rotation=90)
plt.xlabel('Brands', fontsize=20)
plt.ylabel('Frequency')
plt.title('Frequency of Products by Brand', fontsize=30)

# plt.show()
plt.savefig('images/India-graphs/brand_freq.pdf')
