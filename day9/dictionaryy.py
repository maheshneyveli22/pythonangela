sample_dictionary ={"book1":"sciencebook",
                    "book2":"Mathsbook",
                    775:"jjhggg"}

print(sample_dictionary)
sample_dictionary["book2"]="Environment book"
print(sample_dictionary)

for eachItem in sample_dictionary:
    print(eachItem)
    print(sample_dictionary[eachItem])