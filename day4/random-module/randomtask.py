import random 
import my_module

# random_integer= random.randint(1,1000000)
# print(random_integer)
# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random()*1000
# print(random_number_0_to_1)

# random_float = random.uniform(1,200)
# print(random_float)

#This will give random number which is either 1 or 0
random_heads_or_tails = random.randint(0,2);
print(random_heads_or_tails);

if(random_heads_or_tails)==0:
    print("Heads")
else: 
    print("tails")
    
