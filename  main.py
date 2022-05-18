'''function takes a string and checks if it is a palindrome'''
from logging import raiseExceptions


def isPalindrome(word):
    try:
        if word == word[::-1]:
            print(f"{word} is palindrome")

        else:
            print(f"{word} is not palindrome")
    except:
        raiseExceptions("expected string")

if __name__:
    word=input("Please enter string to check if its palindrome:")
    isPalindrome(word)
