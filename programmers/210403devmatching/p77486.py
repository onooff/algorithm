'''
개당100원
'''


def solution(enroll, referral, seller, amount):
    answer = []
    tree = dict()
    earn = dict()
    tree.setdefault("-", False)
    earn.setdefault("-", 0)
    num = len(enroll)
    for i in range(num):
        tree.setdefault(enroll[i], referral[i])
        earn.setdefault(enroll[i], 0)
    num = len(seller)
    for i in range(num):
        now = seller[i]
        get_money = amount[i]*100
        while True:
            pre = tree[now]
            give_money = get_money//10
            get_money = get_money-give_money
            earn[now] += get_money
            if give_money == 0:
                break
            if pre not in tree:
                earn[now] += give_money
                break
            now = pre
            get_money = give_money
    for e in enroll:
        answer.append(earn[e])

    return answer


print(solution(	["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary",
                                                                                       "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print('[360, 958, 108, 0, 450, 18, 180, 1080]')
