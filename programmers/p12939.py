def solution(s):
    num_list = list(map(int, s.split()))
    num_list.sort()
    return str(num_list[0])+" "+str(num_list[-1])
