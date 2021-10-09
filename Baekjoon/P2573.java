import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P2573 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), M = sc.nextInt();
        int[][] A = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                A[i][j] = sc.nextInt();
            }
        }

        sc.close();

        int answer = 0;

        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        int count = 0;
        while(count < 2){
            count = 0;

            answer++;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if(A[i][j] == 0) continue;

                    if(i > 0 && A[i-1][j] == 0) A[i][j]--;
                    if(i < N-1 && A[i+1][j] == 0) A[i][j]--;
                    if(j > 0 && A[i][j-1] == 0) A[i][j]--;
                    if(j < M-1 && A[i][j+1] == 0) A[i][j]--;

                    if(A[i][j] <= 0) A[i][j] = -1;
                }
            }

            boolean[][] visit = new boolean[N][M];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if(visit[i][j]) continue;
                    visit[i][j] = true;

                    if(A[i][j] == -1) A[i][j] = 0;
                    if(A[i][j] == 0) continue;
                    Queue<Integer> R = new LinkedList<>(), C = new LinkedList<>();
                    R.add(i);
                    C.add(j);
                    count++;

                    while(!R.isEmpty()){
                        int r = R.poll(), c = C.poll();

                        for (int[] dir : DIRS) {
                            int nr = r + dir[0], nc = c + dir[1];

                            if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                            if(visit[nr][nc]) continue;
                            visit[nr][nc] = true;

                            if(A[nr][nc] == -1) A[nr][nc] = 0;
                            if(A[nr][nc] == 0) continue;
                            R.add(nr);
                            C.add(nc);
                        }
                    }
                }
            }

            if(count == 0) {
                answer = 0;
                break;
            }
        }


        System.out.println(answer);
    }
}
