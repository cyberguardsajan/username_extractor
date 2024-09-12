import re

def is_valid_email(email_address):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.fullmatch(email_pattern, email_address))

def extract_username_and_domain(email_address):
    username, domain = email_address.split('@')
    return username, domain

email_input = input("Enter your email id: ")

if is_valid_email(email_input):
    user_name, domain_name = extract_username_and_domain(email_input)
    print("Username: ", user_name)
    print("Domain: ", domain_name)
else:
    print("Invalid Email!")
