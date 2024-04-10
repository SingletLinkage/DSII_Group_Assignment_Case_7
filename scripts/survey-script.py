import pandas as pd
import matplotlib.pyplot as plt

def plot_donut(x, labels, title, filename=None):
    plt.pie(x, labels=labels, autopct='%1.1f%%', startangle=90, colors = ['#4CAF50', '#FF5722', '#2196F3', '#FF9800', '#9E9E9E'])
    center_circle = plt.Circle((0, 0), 0.8, color='white')
    plt.gca().add_artist(center_circle)
    plt.title(title, fontsize=15)
    if filename:
        plt.savefig(filename)
        plt.clf()
    else:
        plt.show()


# Importing the data:
data = pd.read_csv('source_files/survey_responses.csv')
data.columns = ['Timestamp', 'Gender', 'Age', 'Nykaa', 'Revlon', 'Mamaearth', 'Lotus Herbals', 'Elle 18', 'Maybelline', 'Lakme', 'Sugar Cosmetics', 'Miss Claire', 'L\'Oreal Paris', 'Remarks']

data_males = data[data['Gender']=='Male']
data_females = data[data['Gender']=='Female']
data_others = data[data['Gender']=='Prefer not to say']

# Plotting the data:

# Gender Distribution:
# x = data['Gender'].value_counts()
# label = data['Gender'].value_counts().index
# plt.pie(x, labels=label, autopct='%1.1f%%')
# center_circle = plt.Circle((0, 0), 0.7, color='white')
# plt.gca().add_artist(center_circle)
# plt.title('Gender Distribution in Responses', fontsize=15)
# plt.savefig('images/survey-graphs/gender-distribution.pdf')

# Individual Brand Preferences:
# plot all brands as a bar plot

brands = ['Nykaa', 'Revlon', 'Mamaearth', 'Lotus Herbals', 'Elle 18', 'Maybelline', 'Lakme', 'Sugar Cosmetics', 'Miss Claire', 'L\'Oreal Paris']
params = {
    'not_heard': 0, 
    'not_used':  0, 
    'rating_1':  0, 
    'rating_2':  0, 
    'rating_3':  0
}

all_details = {}

for brand in brands:
    all_details[brand] = params.copy()
    all_details[brand]['not_heard'] = data[brand].value_counts()['Haven\'t heard about this']
    all_details[brand]['not_used'] = data[brand].value_counts()['Heard about it - havent used it']
    all_details[brand]['rating_1'] = data[brand].value_counts()['Used it, Rating - 1/3']
    all_details[brand]['rating_2'] = data[brand].value_counts()['Used it, Rating - 2/3']
    all_details[brand]['rating_3'] = data[brand].value_counts()['Used it, Rating - 3/3']

# print(all_details)

brands = ['Nykaa', 'Revlon', 'Mamaearth', 'Lotus Herbals', 'Elle 18', 'Maybelline', 'Lakme', 'Sugar Cosmetics', 'Miss Claire', 'L\'Oreal Paris']
for brand in brands:
    plot_donut(all_details[brand].values(), labels=['Haven\'t Heard', 'Haven\'t Used', 'Rating: 1', 'Rating: 2', 'Rating: 3'], title=f'{brand} Brand Preference', filename=f'images/survey-graphs/{brand}-brand-preference.pdf')


plt.show()