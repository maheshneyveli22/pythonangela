import os 

print(os.getcwd())

# O/P:
# C:\Workspace\pythonangela

with open("/Workspace/pythonangela/day25/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

# O/P:    
# ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']
