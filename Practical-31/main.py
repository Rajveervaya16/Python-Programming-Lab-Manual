print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
import re
text = "Contact us at support@example.com or admin@domain.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)
print("Extracted Email Addresses:")
for email in emails:
    print(email)
