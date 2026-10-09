security_event = (
    "2026-10-09 14:30:00",
    "192.168.1.10",
    "LOGIN_ATTEMPT",
    "FAILED"
)

timestamp, source_ip, event_type,status = security_event

print("Timestamp:",timestamp)
print("Source IP:",source_ip)
print("Event:",event_type)
print("Status:",status)