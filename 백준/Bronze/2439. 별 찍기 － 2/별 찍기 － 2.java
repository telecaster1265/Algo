import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 5 입력

        for(int i = 1; i <= n; i++) {  // 1부터 5까지 반복
            for(int j = n; j > i ; j--) { // 5부터 1까지 공백 출력 반복
                System.out.print(" ");
            }
            for(int j = 0; j < i; j++) { // 1부터 5까지 별표 출력 반복
                System.out.print("*");
            }
            System.out.println(); //줄바꿈
        }
    }
}