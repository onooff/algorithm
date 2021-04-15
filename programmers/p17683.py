def remove_sharp(s=str()):
    result = ''
    for i in range(len(s)):
        if s[i] == '#':
            result = result[:len(result)-1]+str.lower(result[len(result)-1])
        else:
            result += s[i]
    return result


def solution(m, musicinfos):
    answer = ['(None)', -1]
    m = remove_sharp(m)
    for music in musicinfos:
        start, end, title, melody = music.split(',')
        start = int(start[:2])*60 + int(start[3:])
        end = int(end[:2])*60 + int(end[3:])
        length = end-start
        melody = remove_sharp(melody)
        played_melody = ''
        while len(played_melody) < length:
            played_melody += melody
        if played_melody == '':
            played_melody = melody
        played_melody = played_melody[:length]
        # print(start, end, length, title, melody, played_melody)

        for i in range(length-len(m)):
            # print(m, played_melody[i:i+len(m)])
            if m == played_melody[i:i+len(m)]:
                if answer[1] < length:
                    answer[0] = title
                    answer[1] = length

    return answer[0]
