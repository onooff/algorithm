def solution(nums):
    s = set()
    for n in nums:
        s.add(n)
    return min(len(nums)//2, len(s))
