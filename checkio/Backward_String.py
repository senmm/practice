def backward_string(val: str) -> str:
    new_val = ''.join(list(reversed(val)))
    return(new_val)

print('Example:')
print(backward_string('val'))

assert backward_string('val') == 'lav'
assert backward_string('') == ''
assert backward_string('ohho') == 'ohho'
assert backward_string('123456789') == '987654321'

print("The mission is done! Click 'Check Solution' to earn rewards!")
