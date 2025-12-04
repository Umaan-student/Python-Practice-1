    print("Hello, There!")
    print("Welcome to Temperature Converter Program.")
    print("Press: 1 To convert Celsius to Fahrenheit")
    print("Press: 2 To convert Fahrenheit to Celsius")

    user_choice = int(input("Enter Your Choice: "))
    
    print("You chose option: {user_choice}")

    if user_choice == 1:
        celsius = float(input("Enter Celsius Input: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Your Result =", round(fahrenheit, 2))

    elif user_choice == 2:
        fahrenheit = float(input("Enter Fahrenheit Input: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Your Result =", round(celsius, 2))

    else:
        print("Invalid choice. Please try again.")