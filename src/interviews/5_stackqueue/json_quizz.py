"""
Input {'key1': 'value', 'key2': [1, 2, 3], 'key3': (1, 2, 3)} Output True
Input {'key1': ['value', 'key2': [1, 2, 3], 'key3': (1, 2, 3)} Output False
"""


def validate_format(chars: str) -> bool:
    lookup = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False
    if stack:
        return True

    return True


if __name__ == '__main__':
    chars = "{'key1': 'value', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"
    print(validate_format(chars))

    chars = "{'key1': ['value', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"
    print(validate_format(chars))



