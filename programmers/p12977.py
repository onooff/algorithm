def solution(nums):
    answer = 0

    s = set()
    for i in range(2, 3001):
        s.add(i)
    for i in range(2, 3001):
        n = i*2
        while n <= 3000:
            s.discard(n)
            n += i
    # print(s)

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                tmp = nums[i]+nums[j]+nums[k]
                if tmp in s:
                    answer += 1

    return answer
