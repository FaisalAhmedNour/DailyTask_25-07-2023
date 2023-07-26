print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    print((celsius * 9/5) + 32)
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print((fahrenheit - 32) * 5/9)
else:
    print("Invalid choice. Please choose 1 or 2.")