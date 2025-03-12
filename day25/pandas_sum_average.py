import pandas

data = pandas.read_csv("./day25/weather_data.csv")
temp_list = data["temp"].to_list()
average = sum(temp_list)/len(temp_list)

print(average)

#average or mean directly from pandas 

mean_value= data["temp"].mean()
print(mean_value)

#nth largest 

fifthlargest = data["temp"].nlargest(5)
print(fifthlargest)

#max value 

max_value = data["temp"].max()
print(max_value)

#directly access the series 
print(data.condition)