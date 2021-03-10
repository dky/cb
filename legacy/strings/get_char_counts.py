def get_char_counts(my_string):
    counts_dictionary = {}
    for char in my_string:
        # Initialize char in the dictionary if it does not exist already
        if counts_dictionary.get(char):
            counts_dictionary[char] = 0
        counts_dictionary[char] += 1
    return counts_dictionary



get_char_counts("Subsuperficial")
