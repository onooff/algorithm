cube = [i ** 3 for i in range(101)]
inversed_cube = {cube[i]: i for i in range(101)}
is_cube = set(cube)

ans = list()
for i in range(2, 100 - 2):
    for j in range(i, 100 - 1):
        for k in range(j, 100):
            chk = cube[i] + cube[j] + cube[k]
            if chk in is_cube:
                ans.append((inversed_cube[chk], i, j, k))
ans.sort(key=lambda x: x[0])

for a in ans:
    print(f"Cube = {a[0]}, Triple = ({a[1]},{a[2]},{a[3]})")

# import sys
# sys.stdout.write(
#     "Cube = 6, Triple = (3,4,5)\nCube = 12, Triple = (6,8,10)\nCube = 18, Triple = (2,12,16)\nCube = 18, Triple = (9,12,15)\nCube = 19, Triple = (3,10,18)\nCube = 20, Triple = (7,14,17)\nCube = 24, Triple = (12,16,20)\nCube = 25, Triple = (4,17,22)\nCube = 27, Triple = (3,18,24)\nCube = 28, Triple = (18,19,21)\nCube = 29, Triple = (11,15,27)\nCube = 30, Triple = (15,20,25)\nCube = 36, Triple = (4,24,32)\nCube = 36, Triple = (18,24,30)\nCube = 38, Triple = (6,20,36)\nCube = 40, Triple = (14,28,34)\nCube = 41, Triple = (2,17,40)\nCube = 41, Triple = (6,32,33)\nCube = 42, Triple = (21,28,35)\nCube = 44, Triple = (16,23,41)\nCube = 45, Triple = (5,30,40)\nCube = 46, Triple = (3,36,37)\nCube = 46, Triple = (27,30,37)\nCube = 48, Triple = (24,32,40)\nCube = 50, Triple = (8,34,44)\nCube = 53, Triple = (29,34,44)\nCube = 54, Triple = (6,36,48)\nCube = 54, Triple = (12,19,53)\nCube = 54, Triple = (27,36,45)\nCube = 56, Triple = (36,38,42)\nCube = 57, Triple = (9,30,54)\nCube = 58, Triple = (15,42,49)\nCube = 58, Triple = (22,30,54)\nCube = 60, Triple = (21,42,51)\nCube = 60, Triple = (30,40,50)\nCube = 63, Triple = (7,42,56)\nCube = 66, Triple = (33,44,55)\nCube = 67, Triple = (22,51,54)\nCube = 69, Triple = (36,38,61)\nCube = 70, Triple = (7,54,57)\nCube = 71, Triple = (14,23,70)\nCube = 72, Triple = (8,48,64)\nCube = 72, Triple = (34,39,65)\nCube = 72, Triple = (36,48,60)\nCube = 75, Triple = (12,51,66)\nCube = 75, Triple = (38,43,66)\nCube = 76, Triple = (12,40,72)\nCube = 76, Triple = (31,33,72)\nCube = 78, Triple = (39,52,65)\nCube = 80, Triple = (28,56,68)\nCube = 81, Triple = (9,54,72)\nCube = 81, Triple = (25,48,74)\nCube = 82, Triple = (4,34,80)\nCube = 82, Triple = (12,64,66)\nCube = 82, Triple = (19,60,69)\nCube = 84, Triple = (28,53,75)\nCube = 84, Triple = (42,56,70)\nCube = 84, Triple = (54,57,63)\nCube = 85, Triple = (50,61,64)\nCube = 87, Triple = (20,54,79)\nCube = 87, Triple = (26,55,78)\nCube = 87, Triple = (33,45,81)\nCube = 87, Triple = (38,48,79)\nCube = 88, Triple = (21,43,84)\nCube = 88, Triple = (25,31,86)\nCube = 88, Triple = (32,46,82)\nCube = 89, Triple = (17,40,86)\nCube = 90, Triple = (10,60,80)\nCube = 90, Triple = (25,38,87)\nCube = 90, Triple = (45,60,75)\nCube = 90, Triple = (58,59,69)\nCube = 92, Triple = (6,72,74)\nCube = 92, Triple = (54,60,74)\nCube = 93, Triple = (32,54,85)\nCube = 95, Triple = (15,50,90)\nCube = 96, Triple = (19,53,90)\nCube = 96, Triple = (48,64,80)\nCube = 97, Triple = (45,69,79)\nCube = 99, Triple = (11,66,88)\nCube = 100, Triple = (16,68,88)\nCube = 100, Triple = (35,70,85)"
# )
