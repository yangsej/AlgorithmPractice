import java.io.IOException;
import java.util.Scanner;

class P13699 {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        long[] dp = new long[N+1];
        dp[0] = 1;

        for(int i=1; i<=N; i++){
            for(int j=0; j<i; j++){
                dp[i] += dp[j] * dp[i-j-1];
            }
        }

        long answer = dp[N];

        System.out.println(answer);
    }
}