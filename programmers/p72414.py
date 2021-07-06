def convert(s="00:00:00"):
    ret = 0
    l = list(map(int, s.split(sep=':')))
    for i in range(l[0]):
        ret += 3600
    for i in range(l[1]):
        ret += 60
    for i in range(l[2]):
        ret += 1
    return ret


def solution(play_time, adv_time, logs):
    pt = convert(play_time)+1
    # board = [0 for i in range(pt)]
    board = list()
    at = convert(adv_time)
    st = list()
    et = list()
    for l in logs:
        s, e = l.split('-')
        st.append(convert(s))
        et.append(convert(e))
    st.sort()
    et.sort()

    viewer = 0
    sti = 0
    eti = 0
    ll = len(logs)
    for i in range(pt):
        while(sti < ll and st[sti] == i):
            sti += 1
            viewer += 1
        while(eti < ll and et[eti] == i):
            eti += 1
            viewer -= 1
        board.append(viewer)

    ans = 0
    ans_viewer = sum(board[:at])
    now_viewer = sum(board[:at])
    for i in range(1, pt-at):
        now_viewer -= board[i-1]
        now_viewer += board[i+at-1]
        if now_viewer > ans_viewer:
            ans = i
            ans_viewer = now_viewer

    answer = str()
    answer += '{0:02d}'.format(ans//3600)
    answer += ':'
    ans = ans % 3600
    answer += '{0:02d}'.format(ans//60)
    answer += ':'
    ans = ans % 60
    answer += '{0:02d}'.format(ans)
    return answer


# print(solution("02:03:55", "00:14:15", [
#       "01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
