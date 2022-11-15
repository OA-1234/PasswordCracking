user_pass = str(input("Enter Password: "))

chars = list(user_pass)
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', 
            '7', '8', '9']


final_guess = ""

while (final_guess != user_pass):
    letter = ""
    for char in range(len(chars)):
        letter = str(chars[char])
        for guess in range(len(password)):
            guess_letter = password[guess]
            if guess_letter == letter:
                final_guess = str(final_guess) + str(guess_letter)
                print(final_guess)

print("Your Password is " + final_guess)

            

