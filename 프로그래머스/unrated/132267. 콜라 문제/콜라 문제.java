class Solution {
    static int cnt;
    public int solution(int a, int b, int n) {
        cnt = 0;
        int cola = 0;
        while (n >= a) {
            cola += n/a*b;
            n = cola + n%a;
            cnt += cola;
            cola = 0;
        }
        
        
        return cnt;
    }
}