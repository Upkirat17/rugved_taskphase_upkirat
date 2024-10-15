n=int(input("Enter n value: "))

def fibonacci(n):
    
    n1=1
    n2=1
    i=1
    sum=0
    print("0")
    for p in range(n):
        n2 = n1
        n1 = sum
        sum = n1+n2

        print(sum)

fibonacci(n)
