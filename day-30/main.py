#Error handling
#there are 4 steps to handle the error try,except,else and finally.
# Here’s the clean mental model:
#
# try: code that might fail.
#
# except: what to do if a specific failure happens.
#
# else: runs only if nothing failed.
#
# finally: runs no matter what (closing files, cleaning resources).


#-----Lets try all these------#
# try:
#     file = open("file.txt")
#     dictionary = {"Ram":20}
#     print(dictionary["Shyam"])
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("Except case used")
# except KeyError:
#     print("KeyError")
# else:
#     read =file.readline()
#     print(read)
# finally:
#     file.close()

#Apart from all these we can raise our error too using "raise"
# num = int(input("Enter a number:"))
# if num >56:
#     raise ValueError("Number must be less than 56.")
# print(f"No you entered is :{num}")


#a simple coding exercise to count no of likes
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            # print("Key Error")
            pass

    return total_likes


count_likes(facebook_posts)

