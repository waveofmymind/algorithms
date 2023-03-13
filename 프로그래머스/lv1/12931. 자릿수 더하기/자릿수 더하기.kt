class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        var str = n.toString()
    for (i in str) {
        answer += Integer.parseInt(i.toString())
    }
    return answer
    }
}