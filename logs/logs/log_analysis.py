failed_attempts = 0

with open("../logs/auth.log", "r") as log:
    for line in log:
        if "Failed password" in line:
            failed_attempts += 1

print("Total failed login attempts:", failed_attempts)

if failed_attempts >= 3:
    print("⚠️ Possible brute-force attack detected!")
