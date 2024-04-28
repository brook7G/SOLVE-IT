#1: FizzBuzz solution
def fizzbuzz():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output if output else i)
# fizzbuzz()

#-----------------------------------------------------#

#2: Palindrome
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
    
# print(is_palindrome("racecar"))  # Output: True
# print(is_palindrome("hello"))  # Output: False

#-----------------------------------------------------#
#3: 
