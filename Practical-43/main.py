print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
import whois
domain_name = input("Enter domain name: ")
info = whois.whois(domain_name)
print("Domain Name:", info.domain_name)
print("Registrar:", info.registrar)
print("Creation Date:", info.creation_date)
print("Expiration Date:", info.expiration_date)
