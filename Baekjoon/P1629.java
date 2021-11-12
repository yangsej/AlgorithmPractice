import java.io.IOException;
import java.util.Scanner;

public class P1629 {
    static int A, B, C;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();

        sc.close();

        long answer = pow(A, B) % C;

        System.out.println(answer);
    }

    private static long pow(long a, long b){
        if(b == 0) return 1;
        if(b == 1) return a;

        if(b % 2 == 0) {
            long half = pow(a, b / 2) % C;

            return (half * half) % C;
        }
        else return (pow(a, b - 1) * a) % C;
    }
}
