def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    set1 = set()
    set2 = set()
    dict1 = dict()
    dict2 = dict()

    idx = 0
    l = len(str1)-2
    while idx <= l:
        if (not(str1[idx].isalpha()) or not(str1[idx+1].isalpha())):
            idx += 1
            continue
        el = str1[idx:idx+2]
        if el in set1:
            dict1[el] += 1
        else:
            set1.add(el)
            dict1[el] = 1

        idx += 1

    idx = 0
    l = len(str2)-2
    while idx <= l:
        if (not(str2[idx].isalpha()) or not(str2[idx+1].isalpha())):
            idx += 1
            continue
        el = str2[idx:idx+2]
        if el in set2:
            dict2[el] += 1
        else:
            set2.add(el)
            dict2[el] = 1
        idx += 1

    # print(dict1)
    # print(dict2)
    # print(set1)
    # print(set2)

    andset = set1 & set2
    orset = set1 | set2

    and_size = 0
    or_size = 0

    for el in andset:
        and_size += min(dict1[el], dict2[el])
    for el in orset:
        if not(dict1.get(el)):
            or_size += dict2[el]
        elif not(dict2.get(el)):
            or_size += dict1[el]
        else:
            or_size += max(dict1[el], dict2[el])
    # print(and_size)
    # print(or_size)

    if or_size == 0:
        return 65536
    return int((and_size/or_size)*65536)


# solution("aa1+aa2", "AAAA12")
print(solution("FRANCE", "french"))
# print(int(3.9))
