# count = 1     #declared globally
# def let_check():
#      count = 2
#      return count
# print(count)     #gives global   / if we remove count from global it will throw  an error because it can't print outside its scope its function
# print(let_check())  #gives_function
#
# def another_count():
#     def let_count():
#         count = 4
#         return count
#     return let_count()
#
# print(count)
# #print(let_count())   #it will throw an error because its scope is inside its parent function we have to call its parent function
# print(another_count())

#global scope
enemies = 1
def anything():
    global enemies
    enemies = 2
    return enemies
print(anything())
print(enemies)