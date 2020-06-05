
def is_unique_chars(string):
    if not isinstance(string, str):
        raise ValueError("Invalid Value, only str")
    for s in range(len(string)):
        if string.count(string[s]) > 1:
            return False
    return True

data1 = "abcdefg"
data2 = "aasnoijsdofjioj"
data3 = "dajojiojio"
data4 = 2

print(is_unique_chars(data1))
print(is_unique_chars(data2))
print(is_unique_chars(data3))
print(is_unique_chars(data4))

