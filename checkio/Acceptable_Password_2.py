def is_acceptable_password(password: str) -> bool:
    if len(password) <= 6:
        return False
    if not any(chr.isdigit() for chr in password):
        return False
    return True


print("Example:")
print(is_acceptable_password("short"))

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
