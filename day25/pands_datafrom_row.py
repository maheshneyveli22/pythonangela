import pandas

data = pandas.read_csv("./day25/weather_data.csv")

#get data in row  based on conditions 

dayvalue = data[data.day =="Monday"]
print(dayvalue)

temp = data[data.temp >20]
print(temp)



print(data[data.day == "Monday"])

# get row with maximum temperature 
row_maxtemp = data[data.temp == data.temp.max()]
print(row_maxtemp)


# get row with minimum temperature 
row_mintemp = data[data.temp == data.temp.min()]
print(row_mintemp)


#get a particular element that suits the condition 
monday_value = data[data.day == "Monday"]
print(monday_value.condition)