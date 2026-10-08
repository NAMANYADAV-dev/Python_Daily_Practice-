def user_info(name, age):
    print(name, age)


user_data = {
    "name": "Naman",
    "age": 18
}

# Example usage
user_info(**user_data)