import pandas

data = pandas.read_csv('weather_data.csv')


# list_tempr = data['temp'].to_list()
# average_num = data['temp'].mean()
# max_number = data['temp'].max()
#
# print(data[data.day == 'Monday'])

# highest_temp = data[data.temp == data.temp.max()]
# print(highest_temp)
#
# monday = data[data['day'] == 'Monday']
# print(monday)

# monday_temp_C = monday.temp
# monday_temp_F = (monday_temp_C * 1.8) + 32
# print(monday_temp_F)


# """Create DataFrame"""
#
# data_dict = {
#     "students": ['Anna', 'Vitaliy', 'Oliver'],
#     "scores": [97, 99, 72]
# }
#
# data = pandas.DataFrame(data_dict)
#
# data.to_csv('new_data.csv')
