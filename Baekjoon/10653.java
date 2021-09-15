import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

import java.util.Hashtable;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Map.Entry;

class P10653 {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(), K = scanner.nextInt();

        int[][] checkpoints = new int[N+1][2];

        for(int i=1; i<=N; i++){
            int x = scanner.nextInt(), y = scanner.nextInt();
            checkpoints[i][0] = x;
            checkpoints[i][1] = y;
        }

        int[][] dist = new int[N+1][N+1];
        int[][] dp = new int[N+1][K+1];
        for(int i=1; i<=N; i++){
            for(int j=i+1; j<=N; j++){
                dist[i][j] = Math.abs(checkpoints[i][0] - checkpoints[j][0]) + Math.abs(checkpoints[i][1] - checkpoints[j][1]);
            }
            Arrays.fill(dp[i], 1000000);
            dp[i][0] = dp[i-1][0] + dist[i-1][i];
        }
        for(int i=1; i<N; i++){
            for(int j=1; j<=K; j++){
                for(int k=0; k<j; k++){
                    dp[i+j+1][j] = Math.min(dp[i+j+1][j], dp[i][0] + dist[i][i+j+1]);
                }
//                dp[i][j] = Math.min(dp[i][j], dp[i-j][0] + dist[i-j][i]);
            }
        }

//
//        int answer = dp[N];
//
        System.out.println();
    }
}