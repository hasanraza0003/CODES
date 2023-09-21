# # #twilio api
# # from twilio.rest import Client

# # account_sid="AC93b0ed09125bfa0b95b739dac5eded2e"
# # auth_token="ad4086974da01e95f8be4a7db983563a"
# # twilio_number= "+12564190115"

# # client = Client(account_sid, auth_token)
# # message = client.messages \
# #         .create(
# #         body="",
# #         from_="+12564190115",
# #         to="+917895568599"
# #     )
# # print(message.status)

# # # sheety api

# import requests
# sheet_endpoint ="https://api.sheety.co/ce97b88d96a132611868c3615b46979d/flightDeals2/prices"

# #to update info in the sheets
# sheet_update_end=f"https://api.sheety.co/ce97b88d96a132611868c3615b46979d/flightDeals2/prices/{id_no}"

# sheet_inputs = {
#         "price":
#         {
#          "lowestPrice": ""#cheapest_flight_rate
#         }  
#     }
# sheet_resp=requests.put(url=sheet_update_end,json=sheet_inputs)
# print(sheet_resp.text)

#to get info from the sheets
# sheet_endpoint ="https://api.sheety.co/ce97b88d96a132611868c3615b46979d/flightDeals2/prices"
# sheet_response = requests.get(sheet_endpoint)
# x=sheet_response.json()["prices"]
# iataCode=x[0]["iataCode"]
# city=x[0]["city"]
#id=x[0]["id"]
# lowestPrice=x[0]["lowestPrice"]










# import requests
# from datetime import date
# from dateutil.relativedelta import relativedelta

# #tequila api
# tequila_api_key = "qpjjzmNQV-Y2XtKEaNASOeFmuH-zOIk7"
# tequila_endpoint = "https://api.tequila.kiwi.com/v2/search"

# header={
#     "apikey":tequila_api_key
# }
# fly_from="BOM"
# fly_to="DXB"
# date_from=date.today().strftime("%d/%m/%Y")
# date_to=date.today() + relativedelta(months=+6)

# parameters={
#     "fly_from":fly_from,
#     "fly_to":  fly_to,
#     "date_from": date_from,
#     "date_to":date_to,
# }

# response=requests.get(url=tequila_endpoint,params=parameters,headers=header)

# data=response.json()["data"]
# cheapest_frate=data[0]["price"]
# cityFrom=data[0]["cityFrom"]
# cityTo=data[0]["cityTo"]

