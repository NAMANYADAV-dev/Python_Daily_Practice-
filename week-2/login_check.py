saved_username = "admin"
saved_password = "Lab@123"

entered_username = input ("Enter username: ")
entered_password = input ("Enter password: ")
port = int(input("Enter port number: "))


#Write your comparison expressions below
username_matches = saved_username == entered_username
password_matches = saved_password == entered_password
login_allowed = True
valid_port = 443
print(f"Username  matches: {username_matches}")
print(f"Password matches: {password_matches}")
print(f"Login allowed: {login_allowed}")
print(f"Valid port: {valid_port}")

