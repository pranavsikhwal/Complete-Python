# import requests
# from twilio.rest import Client
#
# api_key = "0bd8365847b6576244ed42de222cf860"
# #--------Sending Message--------#
# ACCOUNT_SID = "ACc4443bd628c75b424adb00d315ac5ca2"
# AUTH_TOKEN ="16e1003dcf04b3155bb2cae9bcfec637"
# #---------sending messages---------#
# params = {
#     "lat": 51.507351,
#     "lon": -0.127758,
#     "appid": api_key,
#     "cnt":4
# }
# will_rain = False
# forecast = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
# forecast.raise_for_status()
# #if we want to iterate a dictionary in a list then we can go this
# for x in forecast.json()['list']:
#     if int(x['weather'][0]['id'])<700:
#         will_rain = True
# if will_rain:
#     client = Client(ACCOUNT_SID,AUTH_TOKEN)
#     message = client.messages.create(body = "It is raining . Bring an umbrella!",from_ ="+13097416917",to ="+917014380327")
#     print(message.status)
#




