
import random
lives = 6
list = ["apple" ,"bottle","camel"]
choice = random.choice(list)
print(choice)
placeholder = ""
for i in range(len(choice)):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letter =[]
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letter:
        print(f"You already guessed letter '{guess}'")
    display = ""
    for letter in choice:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
          display += "_"
    if guess  not in choice:
        lives -= 1
        print(f"You guessed {guess} and it is not in the word . You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print(f"The correct word is {choice} . You lost!")
    print(display)
    if "_" not in display:
        game_over = True
        print("You won!")


