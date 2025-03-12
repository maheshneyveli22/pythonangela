import os
cwd = os.getcwd()
print(cwd)



file = open("python_mahe_readme.txt")
contents = file.read()
print(contents)
file.close()
