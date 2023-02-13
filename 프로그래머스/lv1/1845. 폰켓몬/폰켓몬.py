def solution(nums):
    size = len(nums)//2
    s = set(nums)
    if len(s) > size:
        return size
    else:
        return len(s)