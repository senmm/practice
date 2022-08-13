def beginning_zeros(a: str) -> int:
    a_list = list(a)
    index = 0
    for i in range(len(a_list)):
      if a_list[i] == "0":
        index += 1
      else:
        break
    return(index)

print('Example:')
print(beginning_zeros('10'))

assert beginning_zeros('100') == 0
assert beginning_zeros('001') == 2
assert beginning_zeros('100100') == 0
assert beginning_zeros('001001') == 2
assert beginning_zeros('012345679') == 1
assert beginning_zeros('0000') == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
