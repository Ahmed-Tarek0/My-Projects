#Welcome message
print("welcome to our program")

#The running of the program
while True:
    try:
        #the number that the user will enter
        number = int(input("Enter an integer positive number: "))
        # Validate the entered number to be positive integer
        if number <= 0:
            print("please enter a valid positive integer number")
            continue
        else:
            break
    #if the user entered a letter or float show a message for him to enter integer number
    except ValueError:
        print("please enter a valid positive integer number")

print("\nThe Factors of", number,":")
#finding the factors of the number
for i in range(1,number+1):
    if number % i == 0:
        print(i)

