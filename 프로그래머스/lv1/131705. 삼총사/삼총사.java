class Solution {
    static int numArr[];
    static int N;
    static int temp[] = new int[3];
    static int count = 0;
    
    public int solution(int[] number) {
        int answer = 0;
        N = number.length;
        numArr = number;        
        dfs(0,0);
        return count;

    }
    private static void dfs(int idx,int depth){
          if (depth == 3) {
              int sum = 0;
              for(int i = 0; i<3; i++) {
                  sum += temp[i];
              }
              if (sum == 0) {
                  count ++;
              }
              return;
          }
      
    
    for(int i = idx; i < N; i++){
            temp[depth] = numArr[i];
            dfs(i+1, depth + 1);
        }
            
    }
}
