# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
#
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# 2. Then check for the number of times the letters in the word LOVE occurs.
#
# 3. Then combine these numbers to make a 2 digit number and print it out.
#
# e.g.
#
# name1 = "Angela Yu" name2 = "Jack Bauer"
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
#
#
# Love Score = 53
#
#
#
#
#
# Example Input
#
# calculate_love_score("Kanye West", "Kim Kardashian")
#
# Example Output
#
# 42

#Solution
def calculate_love_score(name_one, name_two):
    combined = (name_two + name_one).lower()
    truecount = 0
    lovecount = 0
    for ch in "true":
        truecount += combined.count(ch) #this .count tells us how many time a letter is present in this word
    for ch in "love":
        lovecount += combined.count(ch)
    final_count = str(truecount) + str(lovecount)
    print(final_count)


calculate_love_score("Rajesh", "vatika")
