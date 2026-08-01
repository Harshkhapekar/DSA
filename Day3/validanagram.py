def anagram(s , p):
    n= len(p)
    seen = {}
    compare = {}
    window_size = s[:n]
    result = []
    for index in range(n):
        if window_size[index] not in seen:
            seen[window_size[index]] = 1
        else:                                   # seen[ch] = seen.get(ch, 0) + 1   this single line does the work ofentire if else
            seen[window_size[index]] += 1

        if p[index] not in compare:
            compare[p[index]] = 1
        else:
            compare[p[index]] += 1
    
    for index in range(n,len(s)):
        if seen == compare:
            result.append(index - n)
        seen[s[index -n]] -= 1
        if seen[s[index-n]] == 0:
            del seen[s[index-n]]
        if s[index] not in seen:
            seen[s[index]] = 1
        else :
            seen[s[index]] += 1
    if seen == compare:
            result.append(index - n+1)
        
    return result

print(anagram("cbaebabacd","abc"))