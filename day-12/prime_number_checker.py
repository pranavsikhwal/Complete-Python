number = int(input("Enter a number: \n"))
def num_checker(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number%i == 0:
            return False
        # else:
        #     return True
        #     At first glance it seems okay — but this version is actually wrong.
        # Let’s reason it out with an example: say num = 9.
        #
        # The loop starts: i = 2
        #
        # 9 % 2 ≠ 0 → it goes to the else → returns True immediately!
        #
        # But we never checked i = 3, which does divide 9.
        #
        # So the loop ends too early.
    return  True
print(num_checker(number))