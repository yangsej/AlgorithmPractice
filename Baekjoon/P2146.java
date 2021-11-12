import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P2146 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] A = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i][j] = sc.nextInt();
            }
        }

        sc.close();

        int answer = 0, num = 2;
        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int[][] visit = new int[N][N];

        Queue<int[]> landQ = new LinkedList<>(), seaQ = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(A[i][j] != 1) continue;
                if(visit[i][j] != 0) continue;
                A[i][j] = num;
                visit[i][j] = 1;

                landQ.add(new int[] {i, j});

                while (!landQ.isEmpty()){
                    int[] coord = landQ.poll();
                    int r = coord[0], c = coord[1];

                    for (int[] dir : DIRS) {
                        int nr = r + dir[0], nc = c + dir[1];

                        if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

                        if(visit[nr][nc] != 0){
                            if(A[r][c] != A[nr][nc]) {
                                System.out.println(1);
                                return;
                            } else continue;
                        }
                        visit[nr][nc] = 1;

                        if(A[nr][nc] == 0){
                            seaQ.add(new int[] {nr, nc});
                        } else {
                            landQ.add(new int[] {nr, nc});
                        }

                        A[nr][nc] = num;
                    }
                }

                num++;
            }
        }

        while (!seaQ.isEmpty() && answer == 0){
            int[] coord = seaQ.poll();
            int r = coord[0], c = coord[1];

            for (int[] dir : DIRS) {
                int nr = r + dir[0], nc = c + dir[1];

                if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if(visit[nr][nc] == 0 && A[nr][nc] == 0){
                    visit[nr][nc] = visit[r][c] + 1;
                    A[nr][nc] = A[r][c];

                    seaQ.add(new int[] {nr, nc});
                } else if(visit[nr][nc] != 0 && A[r][c] != A[nr][nc]){
                    answer = visit[r][c] + visit[nr][nc];
                    break;
                }
            }
        }

        System.out.println(answer);
    }
}
