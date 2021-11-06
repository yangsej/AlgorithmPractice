import java.io.IOException;
import java.util.*;

public class P11967 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), M = sc.nextInt();
        ArrayList<int[]>[][] buttons = new ArrayList[N][N];
        for (ArrayList<int[]>[] button : buttons) {
            for (int i = 0; i < N; i++) {
                button[i] = new ArrayList<int[]>();
            }
        }

        for (int m = 0; m < M; m++) {
            int x = sc.nextInt() - 1, y = sc.nextInt() - 1, a = sc.nextInt() - 1, b = sc.nextInt() - 1;

            buttons[x][y].add(new int[] {a, b});
        }

        sc.close();

        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        int answer = 1;

        boolean[][] lights = new boolean[N][N], visit = new boolean[N][N];
        lights[0][0] = true;
        visit[0][0] = true;

        Queue<int[]> Q = new LinkedList<>(), LQ = new LinkedList<>();
        Q.add(new int[] {0, 0});

        while (!Q.isEmpty()){
            int[] coord = Q.poll();
            int r = coord[0], c = coord[1];

            for (int[] sw : buttons[r][c]) {
                int swr = sw[0], swc = sw[1];

                if(!lights[swr][swc]){
                    lights[swr][swc] = true;
                    LQ.add(new int[] {swr, swc});
                    answer++;
                }
            }

            for (int[] dir : DIRS) {
                int nr = r + dir[0], nc = c + dir[1];

                if(nr < 0 || nc < 0 || nr >= N || nc >= N) continue;
                if(visit[nr][nc]) continue;
                if(!lights[nr][nc]) continue;

                visit[nr][nc] = true;

                Q.add(new int[] {nr, nc});
            }

            Queue<int[]> NLQ = new LinkedList<>();
            for (int[] ints : LQ) {
                int lr = ints[0], lc = ints[1];

                if(visit[lr][lc]) continue;

                for (int[] dir : DIRS) {
                    int nlr = lr + dir[0], nlc = lc + dir[1];

                    if(nlr < 0 || nlc < 0 || nlr >= N || nlc >= N) continue;
                    if(visit[nlr][nlc]) {
                        visit[lr][lc] = true;
                        Q.add(ints);
                        break;
                    }
                }

                if(Q.peek() != ints) NLQ.add(ints);
            }
            LQ = NLQ;
        }

        System.out.println(answer);
    }
}
