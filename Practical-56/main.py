print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
filename = input("Enter file name: ")
# List of potentially risky extensions
extensions = [".exe", ".bat", ".vbs", ".scr", ".cmd"]
# Check file extension
if filename.lower().endswith(tuple(extensions)):
    print("Potentially risky file")
else:
    print("Extension not in the risky list")
