mind=4
match_not_found=True
while match_not_found==True:
    guess=int(input("enter your guess"))
    if guess==mind:
        print("Your Guess is right")
    elif guess>mind:
        print("Your Guess is higher")
    elif guess<mind:
        print("Your Guess is lower")
