def add_two_numbers() -> int:
    char_nums = input().split(",")
    total = 0
    for c in char_nums:
        total += int(c)
    return total


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
