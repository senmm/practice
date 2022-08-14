def between_markers(text: str, start: str, end: str) -> str:
    length = len(text)
    flag = 0
    for i in range(length):
        if text[i] == start:
            flag = i + 1
        elif flag != 0 and text[i] == end:
            return(text[flag:i])
    return None

print('Example:')
print(between_markers('What is >apple<', '>', '<'))

assert between_markers('What is >apple<', '>', '<') == 'apple'
assert between_markers('What is [apple]', '[', ']') == 'apple'
assert between_markers('What is ><', '>', '<') == ''
assert between_markers('[an apple]', '[', ']') == 'an apple'

print("The mission is done! Click 'Check Solution' to earn rewards!")