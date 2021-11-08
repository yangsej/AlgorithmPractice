import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P2206 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), M = sc.nextInt();
        char[][] arr = new char[N][];
        for (int i = 0; i < N; i++) {
            String str = sc.next();

            arr[i] = str.toCharArray();
        }

        sc.close();

        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        Queue<int[]> Q = new LinkedList<>();
        Q.add(new int[] {0, 0, 0});

        int[][][] visit = new int[2][N][M];
        visit[0][0][0] = 1;
        visit[1][0][0] = 1;

        while(!Q.isEmpty()){
            int[] coord = Q.poll();
            int r = coord[0], c = coord[1], w = coord[2];

            if((r == N-2 && c == M-1) || (r == N-1 && c == M-2)){
                visit[w][N-1][M-1] = visit[w][r][c] + 1;
                break;
            }


            for (int[] dir : DIRS) {
                int nr = r + dir[0], nc = c + dir[1];

                if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

                if(arr[nr][nc] == '0'){
                    if(visit[w][nr][nc] == 0 || visit[w][r][c] + 1 < visit[w][nr][nc]) {
                        visit[w][nr][nc] = visit[w][r][c] + 1;
                        Q.add(new int[] {nr, nc, w});
                    }
                }

                if(arr[nr][nc] == '1' && w == 0){
                    if (visit[1][nr][nc] == 0 || visit[1][r][c] + 1 < visit[1][nr][nc]) {
                        visit[1][nr][nc] = visit[0][r][c] + 1;
                        Q.add(new int[]{nr, nc, 1});
                    }
                }
            }
        }

        int answer = visit[0][N-1][M-1];
        if(answer == 0) answer = visit[1][N-1][M-1];
        if(answer == 0) answer = -1;

        System.out.println(answer);
    }
}
