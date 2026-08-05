from typing import List
def destCity( paths: List[List[str]]) -> str:
        cities = set()
        for city in paths:
            for city2 in city:
                cities.add(city2)
        for index in range(len(paths)):
             if paths[index][0]  in cities:
                  cities.remove(paths[index][0])
        return "".join(cities)
            
print(destCity([["B","C"],["D","B"],["C","A"]]))
