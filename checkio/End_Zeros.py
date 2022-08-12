def end_zeros(a: int) -> int:
    temp_list = list(str(a))
    temp_list.reverse()
    index = 0
    for i in range(len(temp_list)):
      if temp_list[i] == "0":
        index += 1
      else:
        break
    return(index)

print('Example:')
print(end_zeros(10))

assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
