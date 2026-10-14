print("Welcome to the odd or even number checker!")
number = input("Type a number: ")


if int(number) % 2 == 0:
    print(f"{number} is an even number.")

else:
    print("It is an odd number.")