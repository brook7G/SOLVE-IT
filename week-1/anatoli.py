
def FizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)



def Palindrome():
    s = input()
    alphanum = ''
    for v in s:
        if v.isalnum():
            alphanum += v.lower()
    
    return alphanum == alphanum[::-1]



# raises an error for a negative number cuz factorial for negatives is not defined
# uses dynamic programming (memoization ) for efficiency
factorials ={
    0:0,
    1:1
}
def factorial(n):
    if n < 0:
        raise("Negative number input")
    if n in factorials:
        return factorials[n]
    temp = n * factorial(n -1)
    factorials[n] = temp
    return temp


def calculator():
    firstNum = float(input('Please input the first number'))
    op = input('Please input the operator').strip()
    secondNum = float(input('Please input the second num'))

    if op == '+':
        print('result:',firstNum + secondNum)
    elif op =='-':
        print('result:',firstNum - secondNum)
    elif op == "*":
        print('result:',firstNum * secondNum)
    elif op == '/' or op =='%':
        if int(secondNum )!= 0:
            print('result:',firstNum - secondNum)
        else:
            print ("Divisoon by zero not allowed")

def reverseString():
    s = input()
    return s[::-1]
