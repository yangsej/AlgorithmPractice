import java.io.IOException;
import java.util.Scanner;

public class P11729 {
    static StringBuilder builder = new StringBuilder();
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        sc.close();

        int answer = (int)Math.pow(2, N) - 1;

        hanoi(N, 1, 2, 3);

        System.out.println(answer);
        System.out.println(builder);
    }

    private static void hanoi(int n, int l, int m, int r){
        if(n == 1) {
            builder.append(l);
            builder.append(' ');
            builder.append(r);
            builder.append('\n');
            return;
        }

        hanoi(n-1, l, r, m);

        builder.append(l);
        builder.append(' ');
        builder.append(r);
        builder.append('\n');

        hanoi(n-1, m, l, r);
    }
}
