def is_acceptable_password(password: str) -> bool:
    if len(password) <= 6:
        return False
    if not any(chr.isdigit() for chr in password):
        return False
    if all(chr.isdigit() for chr in password):
        return False
    return True


print("Example:")
print(is_acceptable_password("short"))

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
print("Coding complete? Click 'Check' to earn cool rewards!")
