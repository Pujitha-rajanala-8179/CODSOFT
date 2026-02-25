print("-----SIMPLE CALCULATOR -----")

num1 =float(input("Enter first number: "))
num2 =float(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition (+)")
print("2. subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    result = num1 + num2
    print("Result:", result)

elif choice == "2":
    result == num1 - num2
    print("Result:", result)

elif choice == "3":
    result == num1 * num2
    print("Result:", result)

elif choice == "4":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        result = num1 / num2
        print("Result:", result)
    
else:
    print("Invalid choice! Please select 1 , 2 , 3 , or 4.")
