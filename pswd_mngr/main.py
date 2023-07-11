from cryptography.fernet import Fernet
# def key_gen():
#     key = Fernet.generate_key()
#     with open("key.key",'wb') as f:
#         f.write(key)

# key_gen()

#Get key from key file
with open("key.key", "rb") as file:
    key = file.read().decode()
x = Fernet(key)
#Welcome msg
print("----------------Welcome to the Password Manager!----------------")
#get master password
# master_pswd = input("Enter master password: ").strip()

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
