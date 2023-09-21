import requests
from datetime import datetime

USERNAME="hasan03"
TOKEN="hsaihiu4684164sd65f4sd6f4"
graph_id="week1"

pixela_endpoint="https://pixe.la/v1/users"
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint=f"{graph_endpoint}/{graph_id}"
pixel_update=f"{pixel_endpoint}/20230920"

parameters={
    "token":"hsaihiu4684164sd65f4sd6f4",
    "username":"hasan03",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#user request for creating account
# response=requests.post(url=pixela_endpoint,json=parameters)
# print(response.text)

graph_parameters={
    "id":"week1",
    "name":"Coding",
    "unit":"Hours",
    "type":"float",
    "color":"momiji"
    }

header={
    "X-USER-TOKEN":TOKEN
}
#graph request
# response1=requests.post(url=graph_endpoint,json=graph_parameters,headers=header)
# # print(response1.text)
# today=datetime.now()   # for current date
# date=datetime(year=2023,month=9,day=18)  # for previous date


# pixel_parameters={
#     "date":date.strftime("%Y%m%d"),
#  #1 "quantity":"6.5, #or
#  #2 "quantity":input(:How many hours did you coding today)   #for user input
# }
#pixel request
# response2=requests.post(url=pixel_endpoint,json=pixel_parameters,headers=header)
# print(response2.text)

#pixel update
# pixel_parameters1={
#     "quantity":"7.5",
# }
# response3=requests.put(url=pixel_update,json=pixel_parameters1,headers=header)
# print(response3.text)

#delete pixel
# response3=requests.delete(url=pixel_update,headers=header)
# print(response3.text)