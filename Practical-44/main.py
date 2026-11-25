print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
import whois
domain = "example.com"
details = whois.whois(domain)
print(f"Domain Registrar for {domain}: {details.registrar}")
