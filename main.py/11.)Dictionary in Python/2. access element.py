marks = {
    "science": 99,
    "maths": 100,
    "comp": 88,
    "hindi": 43,
    "history": 71,
}
# print(marks["science"])
# print(marks.get("science", -1))

subject = "dwadwa"

ans = marks.get(subject)
if ans is None:
    print("Subject not found")
else:
    print(f"Marks scored = {ans}")
