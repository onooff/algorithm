def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append('')
        str1 = ('{0:0'+str(n)+'}').format(int(format(arr1[i], 'b')))
        str2 = ('{0:0'+str(n)+'}').format(int(format(arr2[i], 'b')))
        # print(str1, str2)
        for j in range(n):
            if str1[j] == '0' and str2[j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'

    return answer
