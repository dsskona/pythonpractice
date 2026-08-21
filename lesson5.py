# Dictionary basics

student = {
    "Name": "Dhanya",
    "City": "Pune",
    "Age": 18,
    "RollNo.": 13
}
print(type(student))

print(student)

print(student["Name"])

student["City"] = "Bengaluru"
print(student)

student["FavSubject"] = "Chemistry"
print(student)

student.pop("FavSubject")
print(student)

print(student.keys())
