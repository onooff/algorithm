def solution(dartResult):
    parse = ['']
    index = 0
    for c in dartResult:
        if len(parse) % 2 == 1 and c.isdigit() == False:
            parse.append('')
            index += 1
        elif len(parse) % 2 == 0 and c.isdigit() == True:
            parse.append('')
            index += 1
        parse[index] += c
    # print(parse)

    point = list()
    index = 0
    tmpPoint = 0
    while index < len(parse):
        tmpPoint = int(parse[index])
        if parse[index+1][0] == 'D':
            tmpPoint **= 2
        elif parse[index+1][0] == 'T':
            tmpPoint **= 3
        if len(parse[index+1]) == 2:
            if parse[index+1][1] == '*':
                tmpPoint *= 2
                if index > 0:
                    point[(index//2)-1] *= 2
            else:  # parse[index+1][1] == '#':
                tmpPoint *= -1
        point.append(tmpPoint)
        tmpPoint = 0
        index += 2
    print(point)
    return sum(point)


# print(solution('1D2S#10S'))  # (1,D) (2,S#), (10,S)


# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
# print(solution('1D2S3T*'))
