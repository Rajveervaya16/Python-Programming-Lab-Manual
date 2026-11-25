print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
import os
path = "."
files = os.listdir(path)
print(f"Files and Directory Contents in '{os.path.abspath(path)}':")
for file in files:
    print(file)
