import sys
inputs = sys.stdin.readlines()

ex = [[906150257, 1], [906150259, 34], [906150295, 12],
      [906150311, 2], [906150315, 1200], [906151517, 58],
      [906154583, 2], [906154605, 0], [906154609, 148],
      [906154763, 0], [906154769, 0], [906154789, 0],
      [906154791, 0], [906154793, 0], [906154825, 0],
      [906154829, 0], [906154837, 0], [906154857, 0],
      [906154865, 16], [906154885, 0], [906154887, 0],
      [906154889, 0], [906154891, 0], [906154893, 0],
      [906154895, 12], [906154909, 2], [906154915, 12],
      [906154947, 2], [906180359, 2], [906180363, 0],
      [906180365, 0], [906180367, 2], [906180371, 2],
      [906180375, 0], [906180391, 126], [906180519, 0],
      [906180525, 8], [906180537, 16], [906180555, 12142],
      [906192847, 18], [906192867, 36], [906192905, 0],
      [906192907, 58], [906192971, 0], [906192979, 4],
      [906192985, 242], [906193229, 4], [906193245, 0],
      [906193247, 0], [906193303, 0], [906193419, 0],
      [906193465, 0], [906193475, 0], [906193477, 0],
      [906194931, 0], [906194933, 12], [906194949, 0],
      [906194951, 16], [906194979, 0], [906195099, 0],
      [906195109, 40], [906195151, 0], [906195297, 0],
      [906195299, 686], [906195989, 0], [906196009, 0],
      [906196011, 2], [906196015, 0], [906196045, 6],
      [906196053, 2], [906196057, 14], [906196077, 2],
      [906196081, 0], [906196083, 8], [906196099, 12612],
      [906208713, 0], [906208731, 0], [906209041, 22],
      [906209067, 0], [906209069, 0], [906209071, 152],
      [906209227, 0], [906209233, 2], [906209237, 0],
      [906209241, 0], [906209243, 28], [906209283, 0],
      [906209285, 268416], [906477735, 76], [906477867, 0],
      [906477869, 0], [906477871, 28], [906477901, 0],
      [906477903, 2], [906477929, 2], [906477933, 0],
      [906477935, 0], [906477937, 8702], [906486805, 0],
      [906486807, 0], [906486817, 0], [906486819, 0],
      [906486821, 10], [906486843, 10], [906486855, 0],
      [906486909, 4], [906486917, 56], [906486975, 26],
      [906487005, 58], [906487065, 0], [906487069, 0],
      [906487071, 0], [906487073, 4], [906487085, 0],
      [906487087, 14], [906487185, 0], [906487187, 2],
      [906487191, 0], [906487193, 0], [906487195, 8],
      [906487205, 0], [906487259, 0], [906487261, 0],
      [906487263, 0], [906487271, 16], [906487933, 0],
      [906487937, 0], [906487949, 24], [906487975, 18],
      [906487995, 6], [906488003, 0], [906488007, 0],
      [906488009, 0], [906488023, 2], [906488027, 38],
      [906488067, 0], [906488077, 2]]

for i in range(1, len(inputs)):
    n = int(inputs[i])
    ans = True
    if n < 906150257:
        if n == 1:
            ans = False
    else:
        for j in range(len(ex)-1, -1, -1):
            if n >= ex[j][0]:
                if n <= ex[j][0]+ex[j][1]:
                    ans = False
                break
    if ans:
        sys.stdout.write('O\n')
    else:
        sys.stdout.write('E\n')