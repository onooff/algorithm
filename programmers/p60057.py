def solution(s):
    answer = len(s)
    l = len(s)//2
    for i in range(1, l+1):
        # if len(s) % i == 0:
        ns = ""
        cnt = 0
        pre = s[0:i]
        # for j in range(0, len(s)+1, i):
        j = 0
        while(j < len(s)):
            cut = s[j:j+i]
            if pre == cut:
                cnt += 1
            else:
                if cnt > 1:
                    ns += str(cnt)
                ns += pre
                cnt = 1
                pre = cut
            j += i
        if cnt > 1:
            ns += str(cnt)
        ns += pre
        cnt = 1
        pre = cut
        # print(i,ns,len(s))
        answer = min(answer, len(ns))
    return answer
