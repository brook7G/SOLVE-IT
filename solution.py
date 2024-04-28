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

#2: 
