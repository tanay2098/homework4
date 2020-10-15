import random

def is_prime(n):
    if n>1:
        for i in range(2,n):
            if((n%i)==0):
                return False
        else:
            return True
    else:
        return False                    

for i in range(0,6):
    n=random.randrange(1,101)
    ans=is_prime(n)
    if ans==True:
        print('The random number',n,'is a prime number')
    else:
        print('The random number',n,'is not a prime number')
