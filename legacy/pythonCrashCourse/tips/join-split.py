# With strings, we can join and split to convert to and from lists and strings.

sentence_with_dashes = "The-fox-jumped-over-the-moon"
words = sentence_with_dashes.split("-")
print(words)
space_character = " "
sentence_with_spaces = space_character.join(words)
print(sentence_with_spaces)
