student_dict = {
    "student": ["Jae", "James", "Lily"],
    "score": [56, 76, 88]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)


# Loop through a data frame

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)


# Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    if row.student == "Jae":
        print(row.score)
    # print(row.student)
    # print(row.score)