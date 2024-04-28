

a,b = map(int,input().split())

oper = input()

if oper == '+':
    print(a+b)
elif oper =='-':
    print(a-b)
elif oper == '*':
    print(a*b)
elif oper =='/':
    if b ==0:
        print('ZeroDivisionError')
    else:
        print(a/b)

    