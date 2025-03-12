#Absolute path example 
# with open("/Users/gs1-maheswarane/OneDrive - Expeditors International of Washington Inc/Desktop/pi1_items.txt") as file:
#     content = file.read()
#     print(content)
    
    
#Relative path example 
with open("./day24/rmy_file.txt") as file:
    content = file.read()
    print(content)
    
with open("../../rmy_file.txt") as file:
    content = file.read()
    print(content)