MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    return_str = []
    for word in code.split("   "):
        for char in word.split(" "):
            print("debug char:", char)
            return_str.append(MORSE[char])
        return_str.append(" ")
    return_str.pop()
    code = str("".join(return_str).capitalize())
    return code

print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
