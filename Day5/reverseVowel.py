def reverseVowels( s: str) -> str:
        vowels = []
        for vow in s:
            if vow.lower() in "aeiou":
                vowels.append(vow)
        reversed_vowels = vowels[::-1]
        new_string = ""
        i = 0
        for index in range(len(s)):
            if s[index].lower() in "aeiou":
                new_string += reversed_vowels[i]
                i+=1
            else :
                new_string += s[index]
        return new_string
print(reverseVowels("IceCreAm"))