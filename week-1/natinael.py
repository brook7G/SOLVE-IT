def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def simple_calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return " Invalid operation"

def reverse_string(s):
    return s[::-1]

def main():
    print("Menu")
    print("choose what to run")
    print("1. FizzBuzz")
    print("2. Palindrome Checker")
    print("3. Factorial Calculator")
    print("4. Simple Calculator")
    print("5. String Reversal")

    choice = input("Enter(1-5): ")

    if choice == '1':
        print("\n FizzBuzz ...\n")
        fizz_buzz()
    elif choice == '2':
        print("\n Palindrome Checker \n")
        s = input("Enter a string: ")
        print(is_palindrome(s))
    elif choice == '3':
        print("\nFactorial Calculator \n")
        n = int(input("Enter a number: "))
        print(factorial(n))
    elif choice == '4':
        print("\nSimple Calculator \n")
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        print(simple_calculator(num1, operator, num2))
    elif choice == '5':
        print("\n String Reversal \n")
        s = input("Enter a string: ")
        print(reverse_string(s))
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        main()

if __name__ == "__main__":
    main()
