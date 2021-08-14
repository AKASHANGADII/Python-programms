def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

n = int(input("Enter the positive interger>> "))
if(is_prime(n)==False):
    print("The number is not a prime number")

else:
    print("The number is a prime number")