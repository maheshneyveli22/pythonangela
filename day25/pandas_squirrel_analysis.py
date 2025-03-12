#Come up with how many cinnamon, black based on primary fur colour 

import pandas 

data = pandas.read_csv("./day25/squirrel_count.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(gray_squirrels)

#getting count
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

#Construct data frame 
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}

print(data_dict)

dataFrame = pandas.DataFrame(data_dict)
dataFrame.to_csv("generated_squirrel_count.csv")