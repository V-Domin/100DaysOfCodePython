import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_color = len(data[data['Primary Fur Color'] == 'Gray'])
red_color = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_color = len(data[data['Primary Fur Color'] == 'Black'])

color_dictionary = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'Number': [gray_color, red_color, black_color]
}

df = pd.DataFrame(color_dictionary)

df.to_csv('count_colors_table.csv')