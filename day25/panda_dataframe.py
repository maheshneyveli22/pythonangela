#Pandas documentation: https://pandas.pydata.org/docs/

import pandas

data = pandas.read_csv("./day25/weather_data.csv")
# Print particular column 
print(data["temp"])
# type of that particular data 
print(type(data))
print(type(data["temp"]))

data_json= data.to_json()
data_dict = data.to_dict()

print(data_json)
print(data_dict)

# {"day":{"0":"Monday","1":"Tuesday","2":"Wednesday","3":"Thursday","4":"Friday","5":"Saturday","6":"Sunday"},"temp":{"0":12,"1":14,"2":15,"3":14,"4":21,"5":22,"6":24},"condition":{"0":"Sunny","1":"Rain","2":"Rain","3":"Cloudy","4":"Sunny","5":"Sunny","6":"Sunny"}}
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

temp_list = data["temp"].to_list()
print(temp_list)
