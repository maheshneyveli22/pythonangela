try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    # print(a_dictionary["ddde"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"key error occurred with message: {error_message}")
else:
    file_content = file.read()
    print(file_content)
finally:
    file.close()
    raise KeyError("invalid key")