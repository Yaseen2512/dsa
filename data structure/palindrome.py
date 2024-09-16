# team6
# Name : Mohameed Yaseen M (23110028)
# 2. Write a python program to check Palindrome number using object oriented approach


class PalindromeChecker:
    def __init__(self, number):
        self.number = number

    def is_palindrome(self):
        original = str(self.number)
        reversed_num = original[::-1]
        return original == reversed_num


while True:
    number = int(input("enter a numbers :"))
    
    
    checker = PalindromeChecker(number)
    if checker.is_palindrome():
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")


