'''function takes a string and checks if it is a palindrome'''
from logging import raiseExceptions


def isPalindrome(word):
    try:
        if word == word[::-1]:
            return True

        else:
            return False
    except:
        raiseExceptions("expected string")

if __name__:
    word=input("Please enter string to check if its palindrome:")
    isPalindrome(word)
