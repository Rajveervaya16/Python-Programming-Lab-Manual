print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
# Import random module
import random
# Define characters for password
characters = "abcdefghijk123456789@#$"
# Create an empty password
password = ""
# Generate 8 characters
for i in range(8):
    password = password + random.choice(characters)
# Display password
print("Generated Password:", password)
