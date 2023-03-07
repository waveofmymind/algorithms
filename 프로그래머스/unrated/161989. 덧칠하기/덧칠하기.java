class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int painted = 0;
        for (int s : section) {
            if (s >= painted) {
                answer += 1;
                painted = s + m;
            }
        }
        return answer;
    }
}