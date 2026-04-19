from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    char_counter = {}
    for c in word:
        if c not in char_counter:
            char_counter[c] = 0
        char_counter[c] += 1
    return char_counter



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
