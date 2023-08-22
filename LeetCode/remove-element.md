## 문제

https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

## 접근

- 주어진 배열 nums에서 val을 지우면 된다.
- 지워지지 않은 수를 카운트해서 반환한다.

## 풀이

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)
        return len(nums)
```

- nums 배열에 val이 있을 때 까지 반복문을 돈다.
- 인덱스를 사용해서 값을 지워나갈 경우, 배열의 길이가 달라지기 때문에 정답이 될 수 없다.

## 회고

처음에는 for문을 사용해서 nums 원소의 값과 val 값이 다를 경우에 새로운 배열에 넣어서, 최종적으로 새로운 배열의 길이를 반환했다.

그러나 문제 해결이 되지 않았고  `Custom Judge`를 보았다.

removeElement()를 통해 구한 k개 만큼 nums의 원소를 검사하기 때문에 nums를 이용해야 했다.

즉, 새로운 arr을 사용할 경우 통과되지 않는 것이 당연했고, 주어진 nums를 사용해서 k값을 구하고, nums를 변환시켜야한다.

그래서 while문 조건으로 val이 nums 배열에 포함되어 있을 때는 계속해서 remove() 해주었다.







