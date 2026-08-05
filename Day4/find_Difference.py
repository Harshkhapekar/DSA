def findTheDifference( s: str, t: str) -> str:
        seen_s = {}
        seen_t = {}
        for index in range(len(t)):
            seen_t[t[index]] = seen_t.get(t[index],0)+1
        for index in range(len(s)):
            seen_s[s[index]] = seen_s.get(s[index] , 0)+1
        for k, v in seen_t.items():
            if v != seen_s.get(k , 0):
                return k
print(findTheDifference("abcd" ,"abcde"))