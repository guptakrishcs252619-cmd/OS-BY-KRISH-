import pandas as pd


data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 88]
}


df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print("krish 085")

import pandas as pd


data = {
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)


print("Statistical Information:")
print(df.describe())
print("krish 085")




import pandas as pd

student = {
    "Amit": 85,
    "Priya": 90,
    "Rahul": 78,
    "Sneha": 92
}


s = pd.Series(student)

print("Pandas Series:")
print(s)
print("krish 085")


import pandas as pd


marks = pd.Series([85, 90, 78, 88, 92])


result = marks[marks > 85]

print("Original Series:")
print(marks)

print("\nFiltered Series (Marks > 85):")
print(result)
print("kriah 085")








