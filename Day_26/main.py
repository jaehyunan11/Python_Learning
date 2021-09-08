numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

new_list = [n+1 for n in numbers]
print(new_list)

# new_list = [new_item for item in list]
"""
1. new_list = [new_item for item in list]
-> [num * 2 for num in numbers]

2. new_list = [new_item for item in list if test]
-> [name for name in names if len(name) > 5]

3. new_list = {new_key:new_value for item in list}
-> {student:random.randint(1,100) for student in names}

4. new_list = {new_key:new_value for (key, value) in dictionary.items() if test)}

"""


