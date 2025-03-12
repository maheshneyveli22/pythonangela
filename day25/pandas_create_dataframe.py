# Create a dataframe from scratch 
import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("test.csv")
print(data)