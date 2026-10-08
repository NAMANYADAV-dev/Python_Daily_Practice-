def security_event(event, severity="INFO", *tags, **details):
    print("Event:", event)
    print("Severity:", severity)
    print("Tags:")
    for tag in tags:
        print(tag)
    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")


security_event(
    "Failed Login",
    "HIGH",
    "authentication",
    "bruteforce",
    username="admin",
    ip="192.168.1.10"
)