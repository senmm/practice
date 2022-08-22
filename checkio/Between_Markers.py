def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text and end in text:
        if text.find(begin) < text.find(end):
            return text[int(text.find(begin) + int(len(begin))):int(text.find(end))]
        else:
            return ''
    elif begin in text:
        return text[int(text.find(begin) + (len(begin))):]
    elif end in text:
        return text[:int(text.find(end))]
    # your code here
    else:
        return text
    return ''


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

