import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# def key_gen():
#     key = Fernet.generate_key()
#     with open("key.key",'wb') as f:
#         f.write(key)

# key_gen()

#Get key from key file
# with open("key.key", "rb") as file:
#     key = file.read().decode()
# x = Fernet(key)
#Welcome msg
print("----------------Welcome to the Password Manager!----------------")
#get master password
master_pswd = input("Enter master password: ").strip()
salt = b'\xfe\xa8Q\xea>0\x91\x82:>-8<u-\xf6'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)
key = base64.urlsafe_b64encode(kdf.derive(master_pswd.encode()))
x = Fernet(key)
def add():
    user_name, pswd = input("Enter username and password separated by comma(,): ").split(",")
    #appending data to file
    with open("pswd_mngr.txt", 'a') as f:
        f.write(user_name + '|' + x.encrypt(pswd.encode()).decode() + "\n")

def view():
    with open("pswd_mngr.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user_name,pswd = data.split('|')
            print(f"Username: {user_name} | Password: {x.decrypt(pswd.encode()).decode()}")

while True:
    choice = input("Enter 'add' to add new password or 'view' to view existing one and 'q' to exit: ").lower()
    if choice == "q":
        break
    
    if choice == "add":
        add()
    elif choice == "view":
        view()
    else:
        print("Invalid choice!")
