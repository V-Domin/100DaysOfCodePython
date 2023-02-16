import requests
from datetime import datetime
import os

USERNAME = os.environ['USERNAME']
TOKEN = os.environ['TOKEN']
ID_GRAPH = 'graph1'
pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)


# graph_param = {
#     'id':ID_GRAPH,
#     'name':'from Zero to Hero -Programming',
#     'unit':'hour',
#     'type':'float',
#     'color':'sora',
# }
# headers = {
#     'X-USER-TOKEN':TOKEN,
# }
# graph_config_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# # response = requests.post(url=graph_config_endpoint, json=graph_param, headers=headers)
# # print(response.text)

now = datetime.now()
today = now.strftime('%Y%m%d')

headers = {
    'X-USER-TOKEN':TOKEN,
}

pixel_param = {
    'quantity': input("How long did you study today?(float) "),
    'date':today,
}

graph_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID_GRAPH}"

response = requests.post(url=graph_pixel_endpoint, headers=headers, json=pixel_param)
print(response.text)


