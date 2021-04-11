def solution(cacheSize, cities):
    answer = 0
    cache = list()
    for city in cities:
        city = str.lower(city)
        if city not in cache:
            answer += 5
            if len(cache) >= cacheSize:
                if cacheSize == 0:
                    continue
                cache.pop(0)
            cache.append(city)
        else:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)

    return answer


print(solution(5, ["SEOUL", "SEOUL", "SEOUL"]))
