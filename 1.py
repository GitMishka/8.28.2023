#Find the first non-repeated character in a string
def first_non_repeated(s: str) -> str:
    char_count = {}

    for char in s:
        print(char_count)
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
print(first_non_repeated('aaaaaabbbbbbbcccccccceeeeeedddddddddddwwwwwwwwwwwwwl'))