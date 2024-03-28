import matplotlib.pyplot as plt
import matplotlib.style as style
import pandas as pd

style.use('seaborn-darkgrid')

data=pd.read_csv('source_files/actual_data_indonesia.csv')

result_db = pd.DataFrame({
        'Frequency' : data['Type of Lip Product'].value_counts(sort=False),
        'Percentage' : data['Type of Lip Product'].value_counts(normalize=True, sort=False)*100,
        'Cumulative Percentage' : round(data['Type of Lip Product'].value_counts(normalize=True, sort=False).cumsum()*100, 2)
}, index=data['Type of Lip Product'].unique())

# print(result_db.to_string())
result_db.to_csv('source_files/type_freq_cumufreq.csv')

x = data['Type of Lip Product'].unique()
y = data['Type of Lip Product'].value_counts(sort=False)

fig, ax = plt.subplots(figsize=(13, 15))
plt.bar(x, y, width=0.8)
plt.xticks(rotation=90)
plt.xlabel('Type of Lip Products', fontsize=30)
plt.ylabel('Frequency', fontsize=30)
plt.title('Frequency of Products by Type of Lip Product', fontsize=40)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)

# plt.show()
plt.savefig('images/TotalProductsbyType.pdf')
