def isPalindrome( s: str) -> bool:
        new_string = ""
        for ele in s:
            if  ele.isalnum():
               new_string += ele
        return new_string.lower() == new_string[::-1].lower()
print(isPalindrome("A man, a plan, a canal: Panama"))