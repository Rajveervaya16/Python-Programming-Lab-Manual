print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
import whois
domain = "python.org"
details = whois.whois(domain)
print(f"Creation Date for {domain}: {details.creation_date}")
