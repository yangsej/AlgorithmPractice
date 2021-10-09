import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P2468 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] A = new int[N][N];
        boolean[] numbers = new boolean[101];
        int max = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i][j] = sc.nextInt();
                numbers[A[i][j]] = true;
                if(max < A[i][j]) max = A[i][j];
            }
        }

        sc.close();

        int answer = 0;

        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        for (int h = 1; h <= max; h++) {
            if(!numbers[h]) continue;
            int count = 0;
            boolean[][] visit = new boolean[N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if(visit[i][j]) continue;
                    visit[i][j] = true;

                    if(A[i][j] < h) continue;
                    Queue<Integer> R = new LinkedList<Integer>(), C = new LinkedList<>();
                    R.add(i);
                    C.add(j);
                    count++;

                    while(!R.isEmpty()){
                        int r = R.poll(), c = C.poll();

                        for (int[] dir : DIRS) {
                            int nr = r + dir[0], nc = c + dir[1];

                            if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                            if(visit[nr][nc]) continue;
                            visit[nr][nc] = true;

                            if(A[nr][nc] < h) continue;
                            R.add(nr);
                            C.add(nc);
                        }
                    }
                }
            }

            if(answer < count){
                answer = count;
            }
        }

        System.out.println(answer);
    }
}
