#API = Application Programming Interface
# an api is just like a bank manager who is between us and money we want to withdraw . it is to verify and act as a layer between our website and the data we want from other website
#API Endpoint is necessary for API call .
import requests
import datetime
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status() #this is because if there is error in api endpoint it will tell to us . https = hypertext transfer protocol security
# # print(response.json())
# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]
# coordinate = (longitude,latitude)
# print(coordinate)

#-------API Calls with parameters--------#
parameters = {
    "lat":30.3398,
    "lng":76.3869,
    "formatted":0
}
response = requests.get("https://api.sunrise-sunset.org/json",params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

date = datetime.datetime.now()
print(date.hour)
