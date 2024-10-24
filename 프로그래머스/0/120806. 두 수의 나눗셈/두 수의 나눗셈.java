class Solution {
    public int solution(int num1, int num2) {
        double answer = ((double)num1 / (double)num2);
        int result = (int)(answer * 1000); 
        return result;
    }
}
