""" Next we can sort by brand. Find the percentage of
    products by brand and also cumulative. We can do this by seeing how many products of each brand are present. Also plot graph of how many products of each brand are present """
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('source_files\data_indonesia.csv')
print(data['Brand'].value_counts(normalize=True))
print(data['Brand'].value_counts(normalize=True).cumsum())
data['Brand'].value_counts().plot(kind='bar') 
plt.show()