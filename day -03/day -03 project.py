print("""

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)

print("Welcome to treasure island . Your mission is to find the treasure.")
choice = input("You are at crossroad, where do you want to go left or right? \n").lower()
if choice == "left":
    choice_2 = input("You are in lake, what you want to swim or to wait \n").lower()
    if choice_2 == "wait":
        choice_3 = input("You arrived at island now which door will you choose to escape- Red , yellow or blue \n").lower()
        if choice_3 == "red":
            print("OOPS! You burned by fire. Game over")
        elif choice_3 == "blue":
            print("OOPS! Eaten by beasts. Game over")
        elif choice_3 == "yellow":
            print("Hurrah! You won the game .")
        else:
            print("OOPS! You lost . Game over")
    else:
        print("OOPS! Attacked by trout . Game over")
else :
    print("You fell into a hole . Game over")