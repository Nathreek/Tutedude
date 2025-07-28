def factorial(n):
    if n<0:
        print("Enter positive numbers only")
    elif n==0 or n==1 :
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter a number: "))
print("Factorial of",n ,"is", factorial(n))
