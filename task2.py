import random 

nums = []
for i in range(0,2):
    nums.append(random.randint(0,10))
t1 = tuple(nums)
    
correct_answer = (int)(t1[0] * t1[1] )
print("How much is",t1[0],"times",t1[1])
temp = 0 
while(temp<1):
    user_answer = int(input(""))
    if user_answer==correct_answer:
        print("done")
        temp= temp +1
    else:
        print(t1[0],"times",t1[1],"is not",user_answer,"please try again:")