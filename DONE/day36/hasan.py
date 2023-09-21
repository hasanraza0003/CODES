import requests
import random
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# Alpha vantage Stock api
api_key="U0SR5JVPZB2D9CEQ"
#news api
api_keyn="ca64814b88224bdb8e24ae13f23bbb6e"
#twilio api
account_sid="AC93b0ed09125bfa0b95b739dac5eded2e"
auth_token="ad4086974da01e95f8be4a7db983563a"
twilio_number= "+12564190115"
#parameters
parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":api_key
}

std={
    "q":COMPANY_NAME,
    "apiKey":api_keyn
}

#stockapi call
response=requests.get(url=STOCK_ENDPOINT,params=parameters)
data=response.json()["Time Series (Daily)"]
data_list=[float(value["4. close"]) for (key,value) in data.items()]
yest=300 #data_list[0]
bef_yest=data_list[1]
diff = abs(bef_yest-yest)
percentage_diff= (diff/yest)*100

#news api call
news=requests.get(url=NEWS_ENDPOINT,params=std)
get_news=news.json()["articles"]
slice_news=[n for n in get_news[:3]]
title_list=[]
for x in range(3):
    new_list=slice_news[x]["title"],slice_news[x]["description"]
    title_list.append(new_list)

rand=random.randint(0,2)
up_down = None

if percentage_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


if percentage_diff > 5:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f" \n TSLA: {up_down} {percentage_diff}% \n Headline :{title_list[rand][0]} \n Brief : {title_list[rand][1]}",
        from_="+12564190115",
        to="+917895568599"
    )
    print(message.status)


