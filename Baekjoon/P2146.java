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

        int num = 2;
        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int[][] visit = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(visit[i][j] == 1) continue;
                visit[i][j] = 1;

                if(A[i][j] == 0) continue;
                A[i][j] = num;

                Queue<Integer> R = new LinkedList<>(), C = new LinkedList<>();
                R.add(i);
                C.add(j);

                while (!R.isEmpty()){
                    int r = R.poll(), c = C.poll();

                    for (int[] dir : DIRS) {
                        int nr = r + dir[0], nc = c + dir[1];

                        if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

                        if(visit[nr][nc] == 1) continue;
                        visit[nr][nc] = 1;

                        if(A[nr][nc] == 0) continue;
                        A[nr][nc] = num;

                        R.add(nr);
                        C.add(nc);
                    }
                }

                num++;
            }
        }


        visit = new int[N][N];
        for (int[] ints : visit) {
            Arrays.fill(ints, -1);
        }

        Queue<Integer> R = new LinkedList<>(), C = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(A[i][j] == 0) continue;
                visit[i][j] = 0;

                R.add(i);
                C.add(j);
            }
        }

        int answer = 0;

        while (!R.isEmpty()){
            int r = R.poll(), c = C.poll();

            for (int[] dir : DIRS) {
                int nr = r + dir[0], nc = c + dir[1];

                if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

                if(A[r][c] != A[nr][nc]){
                    if(A[nr][nc] == 0){
                        if(visit[nr][nc] != -1) continue;
                        visit[nr][nc] = visit[r][c] + 1;
                        A[nr][nc] = A[r][c];

                        R.add(nr);
                        C.add(nc);
                    } else {
                        answer = visit[r][c] + visit[nr][nc];
                        R.clear();
                        break;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
