#dictionary
task = {"work":"To do work given in college","rest":"To take rest","Gym":"To train your body daily"
}
print(task["work"])
print(task)
task["Coding"] = "To upgrade your skills"
print(task)
#using loop in a dictionary
for i in task:
    print(i,task[i])

#nested list and dictionary
travel_cities = {"India":["Jaipur","Delhi","Manali"],
                 "SriLanka":"Colombo",
                 "America":["Chicago","St.Louis"]}
print(travel_cities)
print(travel_cities["India"][1])

#nested list in a list
India = ["Rajasthan","Punjab","Gujrat",["Andaman","Nicobar"]]
print(India)
print(India[2])
print(India[3][1])
#nested dictionary in dictionary
travel_city = {
    "America":{"No. of times visited":8,
               "Cities_visited":["Chicago","St.louis"]},
    "India":{"No of times visited":12,
             "Cities_visited":["Delhi","Manali"]}
}
print(travel_city)
print(travel_city["America"]["Cities_visited"][0])