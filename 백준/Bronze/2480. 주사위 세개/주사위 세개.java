import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int max;
        max = a;
        if(b > max) max = b;
        if(c > max) max = c;

        if (a == b && b == c) {                     //숫자 3개 모두 같은 경우
            System.out.println(10000 + a * 1000);
        } else if (a == b || b == c || c == a) {    //2개 같은경우
            if (a == b || a == c) {
                System.out.println(1000 + a * 100);
            }else {
                System.out.println(1000 + b * 100);
            }
        }
        else {
            System.out.println(max * 100);
        }

    }
}