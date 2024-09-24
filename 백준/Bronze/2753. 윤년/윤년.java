import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        if(a % 4 == 0) {  // 4의 배수 확인
            if(a % 400 == 0) System.out.println("1");  // 400의 배수면 윤년
            else if(a % 100 == 0) System.out.println("0");  // 100의 배수이면 윤년 x
            else System.out.println("1");  // 100의 배수 아니면 윤년
        }
        else System.out.println("0");  // 4의 배수 아니면 윤년 x

    }
}