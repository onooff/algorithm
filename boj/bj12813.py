n_to_b = {'1': True, '0': False}
b_to_n = {True: '1', False: '0'}
a = input()
b = input()

answer = [list(), list(), list(), list(), list()]
andd, orr, xorr, not_a, not_b = answer

for i in range(len(a)):
    ai = n_to_b[a[i]]
    bi = n_to_b[b[i]]
    andd.append(b_to_n[ai & bi])
    orr.append(b_to_n[ai | bi])
    xorr.append(b_to_n[ai ^ bi])
    not_a.append(b_to_n[not ai])
    not_b.append(b_to_n[not bi])

for ans in answer:
    print(''.join(ans))
