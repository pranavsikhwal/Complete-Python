class instagram():
    def __init__(self,username,userid):     #constructor using in class
        self.user_name = username
        self.id = userid


user_1 = instagram("Pranav","001")
print(user_1.user_name)
print(user_1.id)
user_2 = instagram("Shreyansh","123")
print(user_2.user_name)
print(user_2.id)



#methods
# class Car():
#     def num_of_seats(self):
#         self.seats = 4
# car_1 = Car()
# print(car_1.num_of_seats())
#it will print none because it doesnt return anthing
class Car():
    def num_of_seats(self):
        self.seats = 4
        return self.seats
car_1 = Car()
print(car_1.num_of_seats())