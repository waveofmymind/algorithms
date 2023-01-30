class Solution {
                                    
    static String answer;
    static String lt;
    static String rt;
    public String solution(int[] food) {
        lt = "";
        answer="";
        rt="";
        for (int i = 0; i < food.length; i++) {
            lt += Integer.toString(i).repeat((food[i]/2));
            rt += Integer.toString(food.length-i-1).repeat((food[food.length-i-1]/2));
        }
        answer = lt + '0' + rt;
        return answer;
}
}