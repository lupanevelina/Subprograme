n=int(input('n='))
m=int(input('m='))
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact= fact*i
    return fact
C=(factorial(n))/((factorial(m))*(factorial(n-m)))
print(C)