import random
# states =["india", "China","Australia"]
# print(states)
# states.extend(["vietnam",'Japan'])
# print(states)

#option1 
friends= ["Alice","Bob","Charlie","David","Emanuel"]
fruits= ["apple","orange","pear"]
print(random.choice(friends))
friends_fruits=[friends,fruits]
print(len(friends_fruits))

#option2 
random_index = random.randint(1,4)
print(friends[random_index-1])

