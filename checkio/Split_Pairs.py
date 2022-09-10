from typing import Iterable
def split_pairs(text: str) -> Iterable[str]:
    return_list = []
    for i in range(0,len(text),2):
        if i + 1 == len(text):
            temp_str = text[i] + "_"
        else:
            temp_str = text[i] + text[i+1]
        return_list.append(temp_str)        
    return return_list


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")