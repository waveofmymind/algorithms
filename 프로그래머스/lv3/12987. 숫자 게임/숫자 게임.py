def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer = 0
    idx = 0
    for i in A:
        if i < B[idx]:
            answer += 1
            idx += 1
    return answer