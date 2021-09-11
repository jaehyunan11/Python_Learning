# File not found
with open("a_file.txt") as file:
    file.read()

# KeyError

a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# IndexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

# TypeError
text = "abc"
print(text + 5)

"""
1. Try : Something that might cause an exception
2. Except : Do this if there was an exception
3. Else : Do this if there were no exceptions
4. Finally : Do this no matter what happens

"""