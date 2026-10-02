def password_strength(password="Hellofriends"):
    if len(password) >= 12:
        return "Strong"
    elif len(password) >= 8:
        return "Medium"
    else:
        return "Weak"


print(password_strength("Helllo"))
print(password_strength("namanyadav"))
print(password_strength("vivekyadav"))
print(password_strength())