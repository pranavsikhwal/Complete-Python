import random
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")
computer_number = random.randint(1,100)
difficulty = input("Choose a difficulty easy or hard : \n").lower()
if difficulty == "easy":
    maximum_attempts = 10
else:
    maximum_attempts = 5
print(f"You have {maximum_attempts} attempts ")
attempts = 0
while attempts < maximum_attempts:
    guess = int(input("Guess the number:"))
    if guess < computer_number :
         print("Too low")
         print("Guess again ")
         attempts += 1
         print(f"You have {maximum_attempts - attempts} attempts  left")
    elif guess >computer_number:
         print("Too high")
         print("Guess again ")
         attempts += 1
         print(f"You have {maximum_attempts - attempts} attempts  left")
    else:
         print(f"you guessed correctly . The answer is { computer_number}")
         break
if attempts == maximum_attempts :
    print("You ran out of guesses ")


