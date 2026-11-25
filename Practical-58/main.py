print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()
# Read second file
file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()
# Compare file contents
if data1 == data2:
    print("Both files are identical")
else:
    print("Files are different")
