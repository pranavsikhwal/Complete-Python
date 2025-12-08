import requests
import datetime
# Parameters ={
# 'token':"ass12@QWE1@#$VEDW",
# "username":"pranav1213",
# "agreeTermsOfService":"yes",
# "notMinor":"yes"
# }
# x = requests.post("https://pixe.la/v1/users",json = Parameters)
# print(x.json())

#--------Create as graph for habit tracker--------#
# API_ENDPOINT ="https://pixe.la/v1/users/pranav1213/graphs"
# Parameters = {
#     "id":"graph00",
#     "name":"Gym Tracker",
#     "unit":"calory",
#     "type":"float",
#     "color":"shibafu"
# }
# headers ={
# "X-USER-TOKEN":"ass12@QWE1@#$VEDW"
# }
# graph_data = requests.post(API_ENDPOINT,json = Parameters , headers = headers)
# print(graph_data.json())
#---------Adding a pixel-------#
api_endpoint = "https://pixe.la/v1/users/pranav1213/graphs/graph00"
headers ={
"X-USER-TOKEN":"ass12@QWE1@#$VEDW"
}
today = datetime.datetime(year = 2025, month =11,day = 30)
date = today.strftime("%Y%m%d")
parameters = {
    "date":date,
    "quantity":"75"
}
# pixel = requests.post(api_endpoint,json = parameters,headers = headers)
# print(pixel.status_code)

api = " https://pixe.la/v1/users/pranav1213/graphs/graph00/20251130"
new_data = {
"quantity" : "45"
}
change = requests.put(api,json = new_data,headers = headers)
print(change.json())


#there are 4 api requests get , post, put ,delete


