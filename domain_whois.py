import whois
from domain_validator import is_registered
domain_name = input("Enter the Domain Name : ")
if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    print("Domain registrar:",whois_info .registrar)
    print("WHOIS server:",whois_info.whois_serverdate)
    print("Domain creation date:",whois_info.creation_date)
    print("Expiration date:",whois_info.expiration_date)
    print(whois_info)

else:
    print("""

Check the Domain Name again.
If it's correct then it might not exists
in WHOIS database till last update."""
)
