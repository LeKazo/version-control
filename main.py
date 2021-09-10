import random 
attempts = 0
secret_number = random.randint(1,100)
isCorrect = False
guess = int(input("Take a guess: ")) 

while secret_number != guess: 
    if guess < secret_number:
        print("Higher...")
        guess = int(input("Take a guess: "))
        attempts+= 1 
    elif guess > secret_number:
        print("Lower...")
        guess = int(input("Take a guess: "))
        attempts+= 1 
    else:
        print("\nYou guessed it! The number was " ,secret_number)