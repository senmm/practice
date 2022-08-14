def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    if text[-1] != ".":
        text = text + "."
    if text[0].islower:
        text = text[0].upper() + text[1:]
    return(text)

print('Example:')
print(correct_sentence("greetings, friends"))

assert correct_sentence('greetings, friends') == 'Greetings, friends.'
assert correct_sentence('Greetings, friends') == 'Greetings, friends.'
assert correct_sentence('Greetings, friends.') == 'Greetings, friends.'
assert correct_sentence('greetings, friends.') == 'Greetings, friends.'

print("The mission is done! Click 'Check Solution' to earn rewards!")
