password = "secret123"
attempts = 3

while attempts >  0:
    guess = input("Enter the password: ")

    if guess == password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Access denied. {attempts} attempts remaining.")

if attempts == 0:
    print("Too many attempts. Access denied.")