 # Take a email address and print username  domain and reversed domain
email = input("Enter Email:")
at_position = email.find("@")
username = email[:at_position]
domain = email[at_position + 1:]
rev_domain = domain[::-1]
print("Username:",username)
print("Domain:",domain)
print('Reversed domain: ',rev_domain)