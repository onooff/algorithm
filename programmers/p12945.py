def solution(n):
    fb_0 = 0
    fb_1 = 1
    if n == 0:
        return fb_0
    elif n == 1:
        return fb_1
    else:
        now = 1
        ret = 0
        while now != n:
            now += 1
            ret = fb_0+fb_1
            fb_0 = fb_1
            fb_1 = ret
        return now
