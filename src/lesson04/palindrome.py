phrase = "А роза упала на лапу азора"
# дом мод
# иди
# ротор
# Киборгу гробик

def prepareStringForPalindromeCheck(s):
    s = s.upper()
    for c in list(string.punctuation) + [' ']:
        s = s.replace(c, "")
    return s

# Версия 1

palindrome = True
phraseWithoutSpaces = prepareStringForPalindromeCheck(phrase)
for i in range(0, len(phraseWithoutSpaces)):
    if phraseWithoutSpaces[i] != phraseWithoutSpaces[-i-1]:
        palindrome = False
        break

print(phrase,
      "является" if palindrome else "не является",
      "палиндромом")

# Версия 2

def isPalindrome(phrase):
    phrase = prepareStringForPalindromeCheck(phrase)
    for i in range(0, len(phrase)):
        if phrase[i] != phrase[-i-1]:
            return False
    return True

print(phrase,
      "является" if isPalindrome(phrase) else "не является",
      "палиндромом")

