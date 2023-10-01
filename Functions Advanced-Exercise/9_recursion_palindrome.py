def palindrome(word, index):
    if index == len(word):
        return f"{word} is a palindrome"
    if word[index] != word[- index - 1]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))