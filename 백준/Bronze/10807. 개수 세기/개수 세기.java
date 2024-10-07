import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = 0;
        int a = sc.nextInt();
        int ary[] = new int [a];

        for(int i = 0; i < a; i++) {    
            ary[i] = sc.nextInt();
        }
        int b = sc.nextInt();
        for(int j = 0; j < ary.length; j++) {
            if(ary[j] == b) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
