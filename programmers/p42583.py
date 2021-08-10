def solution(bridge_length, weight, truck_weights):
    complete = sum(truck_weights)

    # truck_weights.sort()
    time = 0
    bridge = [0 for i in range(bridge_length)]
    b_sum = 0
    while complete > 0:
        time += 1
        p = bridge.pop(0)
        b_sum -= p
        complete -= p
        nxt = 0
        if len(truck_weights) > 0:
            if truck_weights[len(truck_weights)-1]+b_sum <= weight:
                nxt = truck_weights.pop()
            # elif truck_weights[0]+b_sum <= weight:
            #     nxt = truck_weights.pop(0)
        bridge.append(nxt)
        b_sum += nxt
        # print(bridge, b_sum, weight)

    return time
