day_of_week = input("Enter the day of week : ").lower()

print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("I will learn devops")
else:
    print("I will practice devops")

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))


choice = input("Enter the opearation : (Options +. -, *, /, %) ")
if choice == "+":
    sum = num1 + num2
    print("Addition: ",sum)
elif choice == "-":
    diff = num1 - num2
    print("Subtraction: ",diff)
elif choice == "*":
    product = num1 * num2
    print("Multiplication: ",product)
elif choice == "/":
    div = num1 / num2
    print("Division: ",div)
elif choice == "%":
    rem = num1 % num2
    print("Remainder: ",rem)
else:
    print("Invalid choice")