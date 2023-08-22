## 문제

https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

## 접근

- 내림차순으로 정렬된 정수 배열 nums1,nums2. 각 배열의 길이 m, n
- 0은 무시한다.
- 결과는 nums1에 포함될 것.

## 풀이

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        del nums1[m:]
        
        nums1 += nums2[:n]
        
        nums1.sort()
```

- nums1에서 m개 만큼이 병합 대상이므로, 인덱스 m-1 이후는 모두 없앤다.
- 마찬가지로 병합 대상은 nums2의 원소 n개이므로, nums1에 nums2의 원소 n개를 더한다.(파이썬 리스트는 + 연산 가능)
- 마지막으로 nums2의 n개 원소가 더해진 nums1을 오름차순으로 정렬한다.

## 회고
처음에는 단순히 새로운 배열 arr = nums1 + nums2를 해서, for문을 사용해서 값이 0일 때는 del 명령어를 사용하여 arr에서 0을 모두 제거했다.

그리고 nums1 = arr로 nums1을 바꾸려고 했지만, 최종 nums1의 길이가 m+n을 보장하지 않았다.

또한 최종 nums1의 길이 m+n에서, m만을 병합해야하므로, 인덱스 m-1 이후에는 버리고 마찬가지로 nums2에서 n개 만큼을 더하는 방법으로 해결했다.

또한 배열에서 원소를 지울 때 del과 remove()의 차이점에 대해서 알게 되었다.

del은 인덱스를 기반으로, remove은 값을 기반으로 배열에서 원소를 제거한다.


