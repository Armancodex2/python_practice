student = {"name": "Rahul", "age": 21}
print(student, id(student))

# Update
student["age"] = 30

# Add
student["gender"] = "Male"

student.update(
    {
        "city": "Surat",
        "phone": 321312312,
        "state": "Gujarat",
        "age": 35,
    }
)
print(student, id(student))
