print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
import whois
domain = "google.com"
w = whois.whois(domain)
print("WHOIS Lookup Result:")
print(w)
