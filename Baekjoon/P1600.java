import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P1600 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int K = sc.nextInt(), W = sc.nextInt(), H = sc.nextInt();

        int[][] A = new int[H][W];
        for (int h = 0; h < H; h++) {
            for (int w = 0; w < W; w++) {
                A[h][w] = sc.nextInt();
            }
        }

        sc.close();

        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int[][] HORSE = {{2, 1}, {2, -1}, {-2, 1}, {-2, -1}, {1, 2}, {1, -2}, {-1, 2}, {-1, -2}};

        int answer = -1;
        if(W == 1 && H == 1) answer = 0;

        int[][][] visit = new int[K+1][H][W];
        int MAX = H * W;
        for (int[][] kv : visit) {
            for (int[] hv : kv) {
                Arrays.fill(hv,MAX);
            }
        }
        visit[K][0][0] = 0;


        Queue<int[]> Q = new LinkedList<>();
        Q.add(new int[] {0, 0, K});

        while (!Q.isEmpty() && answer == -1){
            int[] coord = Q.poll();
            int r = coord[0], c = coord[1], k = coord[2];

            for (int[] dir : DIRS) {
                int nr = r + dir[0], nc = c + dir[1];

                if(nr < 0 || nr >= H || nc < 0 || nc >= W) continue;
                if(visit[k][nr][nc] != MAX) continue;
                if(A[nr][nc] == 1) continue;

                if(nr == H-1 && nc == W-1){
                    answer = visit[k][r][c] + 1;
                    break;
                }

                visit[k][nr][nc] = visit[k][r][c] + 1;
                Q.add(new int[] {nr, nc, k});
            }

            if(k == 0) continue;
            for (int[] dir : HORSE) {
                int nr = r + dir[0], nc = c + dir[1], nk = k - 1;

                if(nr < 0 || nr >= H || nc < 0 || nc >= W) continue;
                if(visit[nk][nr][nc] != MAX) continue;
                if(A[nr][nc] == 1) continue;

                if(nr == H-1 && nc == W-1){
                    answer = visit[k][r][c] + 1;
                    break;
                }

                visit[nk][nr][nc] = visit[k][r][c] + 1;
                Q.add(new int[] {nr, nc, nk});
            }
        }

        System.out.println(answer);
    }
}
