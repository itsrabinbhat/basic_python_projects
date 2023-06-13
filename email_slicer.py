import re
#Function to get email as input
def get_email():
    email = input("Enter an email: ").strip()
    return email

#Function to verify email address is correct
def verify_email(email_id):
    pattern = "\w+@\w+\.\w{1,5}"
    if re.match(pattern,email_id):
        return True
    else:

        return False

email = get_email()
is_email = verify_email(email)
if is_email:
    username = email[:email.index('@')]
    domain = email[email.index('@')+1:]
    print("Your username is",username, "and your domain name is", domain)
else:
    print("Enter a valid email!")