# Demo credentials for local learning only 
saved_username = "naman"
saved_password = "cyber@123"
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")
username_matches = entered_username == saved_username
password_matches = entered_password == saved_password
login_allowed = username_matches and password_matches
print(f"Username correct: {username_matches}")
print(f"Password correct: {password_matches}")
print(f"Login allowed: {login_allowed}")
