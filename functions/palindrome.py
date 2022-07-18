def is_palindrome(string: str) -> bool:
    """
    accept string as agrugment and return boolean value if string having same meaning after reverse
    :param string: string
    :return: bool
    """
    return string[::-1].lower() == string.lower()


def palindrome_sentence(sentence: str) -> bool:
    """
      accept string sentence as agrugment and return boolean value if string having same meaning after reverse
      :param string: string
      :return: bool
      """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string)


word = input("please string to check palindrome: ")
if palindrome_sentence(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
