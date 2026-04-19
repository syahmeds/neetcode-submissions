def print_string_characters(word1: str, word2: str) -> None:
    def loop_print_chars(word):
        for c in word:
            print(c)
    loop_print_chars(word1)
    loop_print_chars(word2)



# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")
