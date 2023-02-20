import getpass

MAX_ATTEMPTS = 3
pin = "7884"  # hard-coded PIN
attempts = 0

while attempts < MAX_ATTEMPTS:
    attempts += 1
    attempt = getpass.getpass("Enter your PIN: ")
    if attempt == pin:
        print("PIN accepted. Time to clean out your bank account")
        break
    else:
        remaining_attempts = MAX_ATTEMPTS - attempts
        if remaining_attempts > 0:
            print(f"Incorrect PIN. You have {remaining_attempts} attempts remaining.")
        else:
            print(f"You have exceeded the maximum number of attempts ({MAX_ATTEMPTS}). Please contact your bank for assistance.")
