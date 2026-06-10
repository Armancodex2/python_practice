student = {
    "name": "Rahul",
    "age": 35,
    "gender": "Male",
    "city": "Surat",
}
print(student, id(student))

# student.pop("namee")
# student.clear()
del student["age"]

print(student, id(student))
