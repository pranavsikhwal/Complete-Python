#for loop in python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print(fruits)

scores = [12,34,5,6,67,234,65,4567,3236,3242]
sum = 0
for score in scores:
    sum += score
print(sum)

max_score = max(scores)              #one method
print(max_score)

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score
print(max_score)

#loop in range
range_score = 0
for score in range(1,101):
    range_score += score
print(range_score)


