import random #importing random 

def is_prime(n):# defining is_prime function 
    if n>1:
        for i in range(2,n):
            if((n%i)==0): # Checking divisibility of the number
                return False # returns False boolean value if number is not prime
        else:
            return True # returns True boolean value if number is prime
    else:
        return False  # # returns False boolean value if number is not prime                  

for i in range(0,6): # Loop for 6 numbers
    n=random.randrange(1,101) # generating 6 random numbers between 1 and 101, so 1 and 100 are included. 
    ans=is_prime(n)# applying n in the is_prime function and assigning its value to ans.
    if ans==True: # if is_prime returns true 
        print('The random number',n,'is a prime number')
    else:# if is_prime returns false
        print('The random number',n,'is not a prime number')
