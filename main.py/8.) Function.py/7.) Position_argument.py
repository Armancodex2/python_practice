# Keyword Arguments
def calculate_marks(maths, eng, hindi, comp, history=0):
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"hindi = {hindi}")
    print(f"comp = {comp}")
    print(f"history = {history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"Total marks scored = {total_marks}")


calculate_marks(11, 22, comp=22, history=11, hindi=199)
print("Hello", end=" ")
