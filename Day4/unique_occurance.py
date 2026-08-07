from typing import List
def uniqueOccurrences( arr: List[int]) -> bool:
        seen = {}
        unique = set()
        for ele in arr:
            seen[ele] = seen.get(ele , 0) + 1
        for value in seen.values():
            unique.add(value)
        if len(seen) == len(unique):
            return True
        else :
            return False
print(uniqueOccurrences([1,2,2,1,1,3]))