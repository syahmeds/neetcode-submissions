from typing import List

def read_integers() -> List[int]:
    char_int = input().split(",")
    list_int = []
    for c in char_int:
        list_int.append(int(c))
    return list_int    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
