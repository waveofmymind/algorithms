class Solution {
    static double answer;
    public int solution(int num1, int num2) {
        answer = (double) num1/(double) num2;
        answer *= 1000;
        
        return (int)answer;
    }
}