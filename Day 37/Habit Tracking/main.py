import requests
from datetime import datetime

pixela_url = "https://pixe.la/v1/users"
user_name = "andrewsynelnyk"
token = "vkaskdvalisyu"

user_parameters = {
    "token": "vkaskdvalisyu",
    "username": "andrewsynelnyk",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_url, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_url}/{user_name}/graphs"

graph_config = {
"id": "graph1",
"name": "Coding Graph",
"unit": "min",
"type": "int",
"color": "sora",
}

headers = {
"X-USER-TOKEN": token,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph1_endpoint = f"{pixela_url}/{user_name}/graphs/{graph_config['id']}"

graph1_config = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("Enter the quantity (e.g., minutes): "),

}

response = requests.post(url=graph1_endpoint, json=graph1_config, headers=headers)
print(response.text)

# update_endpoint = f"{pixela_url}/{user_name}/graphs/{graph_config['id']}/{graph1_config['date']}"
#
# new_graph1_config = {
#     "quantity": input("Enter the quantity you want to change (e.g., minutes): "),
# }
#
# # response = requests.put(url=update_endpoint, json=new_graph1_config, headers=headers)
# # print(response.text)
#
#
# delete_endpoint = f"{pixela_url}/{user_name}/graphs/{graph_config['id']}/{graph1_config['date']}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)