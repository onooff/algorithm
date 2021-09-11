'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
'''

import sys
inputs = sys.stdin.readlines()
a = set(inputs[1].rstrip().split())
b = list(inputs[3].rstrip().split())
for chk in b:
    if chk in a:
        print("1 ", end='')
    else:
        print("0 ", end='')
