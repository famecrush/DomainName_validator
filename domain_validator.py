import whois
def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
        

if __name__ == "__main__":

    n = input("Enter the Domain Name : ")
    print(is_registered(n))

   
    
