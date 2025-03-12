import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "maheswaran"
TOKEN = "12345678"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#TODO 1 create user account
# response = requests.post(url = pixela_endpoint, json = user_params)
# Response #{'message': "Success. Let's visit https://pixe.la/@maheswaran , it is your profile page!", 'isSuccess': True}
# print(response.json())
# print(response.status_code)


#TODO 2. Create Graph definition
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "ajisai"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url = graph_endpoint, json= graph_config,headers=headers)
# print(response.text)


#TODO 3. Posting value to the graph
pixela_creation_graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
pixel_creation_headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#https://www.w3schools.com/python/python_datetime.asp
today = datetime.now()
formatted_date = today.strftime(("%Y%m%d"))
print(today)

pixel_data_request_body = {
    "date": formatted_date,
    "quantity": "9.74",
}

# response = requests.post(url=pixel_creation_endpoint,json = pixel_data_request_body, headers = pixel_creation_headers)
# print(response.text)
# Can be viewed here: https://pixe.la/v1/users/maheswaran/graphs/graph1.html

#TODO .4 UPDATE

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
#
# new_pixel_update_body_data = {
#     "quantity": "4.5"
# }
#
# response = requests.put(url = update_endpoint, json = new_pixel_update_body_data, headers=pixel_creation_headers)
# print(response.text)


#TODO . DELETE

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

response = requests.delete(url=delete_endpoint, headers = pixel_creation_headers)
print(response.text)