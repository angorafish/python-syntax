def print_upper_words(words):
    """
    Prints out list up words in all uppercase, 
    giving each word a separate line

    Params: Words, a list of strings
    Returns: None, just prints the words in uppercase.
    """
    for word in words:
        print(word.upper())

test_words = ["hello", "goodbye", "goodmorning", "goodnight"]
print_upper_words(test_words)