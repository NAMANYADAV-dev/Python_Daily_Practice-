events = [
    ["Failed Login", "HIGH"],
    ["Port Scan", "MEDIUM"],
    ["Normal Login","LOW"]
]

for event in events:
    print("Events:",event[0])
    print("severity:",events[1])