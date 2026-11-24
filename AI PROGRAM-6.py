import pandas as pd

n = int(input("Enter number of students: "))

roll = []
names = []
dept = []
marks = []

for i in range(n):
    print("\nStudent", i + 1)

    r = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    d = input("Enter Department: ")
    m = int(input("Enter Mark: "))

    roll.append(r)
    names.append(name)
    dept.append(d)
    marks.append(m)

series = pd.Series(marks, index=names)

print("\n--- Pandas Series ---")
print(series)

data = {
    "RollNo": roll,
    "Name": names,
    "Department": dept,
    "Mark": marks
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

print("\nAverage Mark:", round(df["Mark"].mean(), 2))

print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])