import random
user_choice = int(input("Enter the number 0,1 or 2 where 0 is rock ,1 is paper and  2 is scissor \n"))
system_choice = random.randint(0,2)
print(f"Computer choice is {system_choice}")
if user_choice == system_choice :
    print("Match draw")
elif user_choice >= 3 or user_choice < 0:
    print("Invalid choice")
elif user_choice > system_choice :
    print("You win")
elif user_choice < system_choice :
    print("You lose")
elif usesr_choice == 0 and system_choice == 2:
    print("You won")
elif user_choice == 2 and system_choice == 0:
    print("You Lose")