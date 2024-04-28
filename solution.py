#1: FizzBuzz solution
def fizzbuzz():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output if output else i)
fizzbuzz()

#-----------------------------------------------------#

#2: Palindrome
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
    
# print(is_palindrome("racecar"))  # Output: True
# print(is_palindrome("hello"))  # Output: False

#-----------------------------------------------------#
#3: Factorial calculator
def factorial(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        elif n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    except ValueError as e:
        return f"Error: {e}"

# print(factorial(5))

#-----------------------------------------------------#
#4: 

