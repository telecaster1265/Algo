class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int num = numer1 * denom2 + numer2 * denom1; 
        int den = denom1 * denom2; 
        int sol = sol(num,den);
        
        return new int[] {num/sol, den/sol };
    }
    private int sol(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return sol(b, a % b);
        }
    }
}