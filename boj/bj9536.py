import sys
inputs = sys.stdin.readlines()
idx = 1
while idx < len(inputs):
    sound = inputs[idx].strip().split()
    idx += 1
    other_animal_sound = set()
    while inputs[idx].strip() != "what does the fox say?":
        tmp = inputs[idx].split()
        idx += 1
        other_animal_sound.add(tmp[2])
    ans = list()
    for s in sound:
        if s not in other_animal_sound:
            ans.append(s)
    print(' '.join(ans))
    idx += 1
