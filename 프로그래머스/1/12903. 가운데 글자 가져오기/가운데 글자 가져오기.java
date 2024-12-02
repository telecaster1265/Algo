class Solution {
    public String solution(String s) {
        int length = s.length();
        
        if(length % 2 == 0){
            int mid = length / 2;
            return s.substring(mid - 1, mid + 1);
        }
        
        else {
            int mid = length / 2;
            return s.substring(mid, mid + 1);
        }
    }
}