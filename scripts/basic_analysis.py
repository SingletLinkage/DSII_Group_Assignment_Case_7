
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