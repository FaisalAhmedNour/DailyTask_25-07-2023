num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))
if num1 >= num2: 
    if num1 == num2: 
        print("Both numbers are equal.") 
    else:
        print(num1)
else:
    print(num2)