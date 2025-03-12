import json

new_data = {
    "website":{
        "email": "email@test.com",
        "password": "PASSWORD"
    }
}
new_data_2 = {
    "website2":{
        "email": "email2@test.com",
        "password": "PASSWORD2"
    }
}
#with open("mahe.json","w") as data_file:
    # To write to json file
  #  json.dump(new_data,data_file, indent=4)
    # To read json file
    # data = json.load((data_file))

    # To update json file i.e append at the end and not override
    #1 read old data
with open("mahe.json","r") as data_file:
    data = json.load((data_file))
    #2 Updating old data with new data
    data.update(new_data_2)
    #3 Saving updated data
    #Open file again in write mode
with open("mahe.json","w") as data_file:
    json.dump(data, data_file, indent=4)
    print(data)
