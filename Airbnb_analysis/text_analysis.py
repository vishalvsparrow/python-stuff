import pandas as pd
import numpy as np
import re
import csv
import plotly as py
import plotly.graph_objs as go

import nltk

my_data = pd.read_csv('amenities_deposit_cleaning.csv')

# print(my_data)
raw_amenities = my_data.amenities
# print (raw_amenities)

# null_data = my_data[raw_amenities.isnull().any(axis=1)]

print(np.size(raw_amenities), 'Size of the amenities object')
print(type(raw_amenities))

cleaned_amen = dict()
count = 0
amen_features = []
unique_amen = dict()

# A loop to iterate over the amenities object
for amen in raw_amenities:
    temp_inner_list = list()  # List of each individual training example list

    # split() returns a list
    temp_amen = amen.split(',')

    # This is where we iterate over each element in the list
    for temp_element in temp_amen:
        temp_element_1 = re.sub('[{}"]', '', temp_element)
        # print(temp_element_1)
        temp_inner_list.append(temp_element_1)

        if temp_element_1 not in amen_features:
            amen_features.append(temp_element_1)
            unique_amen[temp_element_1] = 1
            # print temp_inner_list
        else:
            unique_amen[temp_element_1] = unique_amen[temp_element_1] + 1

    cleaned_amen[count] = temp_inner_list
    count = count + 1

# print(amen_features)
# print(cleaned_amen)
# print(sorted(unique_amen.values()))
print(unique_amen)
# print(list(reversed(sorted(unique_amen.items(), key=lambda x: x[1]))))
# for clean in cleaned_amen:
#   for each_element in cleaned_amen[clean]:
#      print each_element

with open('amenities_freq.csv', 'w+') as csv_handler:
    writer = csv.writer(csv_handler)
    for amenities, freq in reversed(sorted(unique_amen.items(), key=lambda x: x[1])):
        writer.writerow([amenities, freq])

bar_graph = [go.Bar(y=unique_amen.values(), x=unique_amen.keys())]
py.offline.plot(bar_graph,filename='amenities_frequency')

''''
with open('vishal_amenities_cleaned.csv', 'w+') as csv_handler:
    writer = csv.writer(csv_handler)
    for key, value in cleaned_amen.items():
        writer.writerow([key+1, value])

'''
