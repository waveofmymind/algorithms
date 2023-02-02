from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    brg = [0]*bridge_length
    brg = deque(brg)
    truck_weights = deque(truck_weights)
    brg_sum = 0
    while brg:
        cnt += 1
        tmp = brg.popleft()
        brg_sum -= tmp
        if truck_weights:
            if brg_sum + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                brg_sum += t
                brg.append(t)
            else:
                brg.append(0)
    return cnt
        
            