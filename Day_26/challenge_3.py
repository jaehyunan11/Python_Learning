with open("file1.txt") as file1_data:
    file1_new_data = file1_data.readlines()

with open("file2.txt") as file2_data:
    file2_new_data = file2_data.readlines()

result = [int(num) for num in file1_new_data if num in file2_new_data]
print(result)