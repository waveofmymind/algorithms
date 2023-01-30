class Solution {
    static int cnt;
    public int solution(String t, String p) {
        int p_size = p.length();
        int t_size = t.length();
        cnt = 0;
        for (int i=0; i < t_size-p_size+1; i++) {
            String tmp = t.substring(i,i+p_size);
            if (Long.parseLong(tmp)  <= Long.parseLong(p)){
                cnt ++;
            }
        }
        return cnt;
    }
}