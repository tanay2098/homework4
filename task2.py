import random # importing package random

nums = [] # initializing an empty list called nums
for i in range(0,2): # Loop for 2 elements  
    nums.append(random.randint(0,10)) # generating 2 numbers between 0 to 10 and appending them in the list
t1 = tuple(nums) # converting list into a tuple named t1
    
correct_answer = (int)(t1[0] * t1[1] )# converting product of first and second element of tuple into integer and storing it
print("How much is",t1[0],"times",t1[1],"? ") # Displaying the question
temp = 0 # a variable to store sentinel value
while(temp<1):
    user_answer = int(input("->"))# prompting user to enter the answer
    if user_answer==correct_answer: # Comparing the user's answer with correct answer
        print("done") # If answer is right then display done
        temp= temp +1 # incrementing the value in variable by 1, so as to exit the loop
    else:
        print(t1[0],"times",t1[1],"is not,",user_answer,"please try again: ")# if answer is wrong then prompt user to enter the correct answer