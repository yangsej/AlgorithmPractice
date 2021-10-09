import java.io.IOException;
import java.util.*;

public class P10026 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        char[][] arr = new char[N][];
        for (int i = 0; i < N; i++) {
            String str = sc.next();

            arr[i] = str.toCharArray();
        }

        sc.close();

        int ans1 = 0, ans2 = 0;
        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        boolean[][] visit1 = new boolean[N][N], visit2 = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(visit1[i][j]) continue;
                visit1[i][j] = true;

                ans1++;

                Queue<Integer> rq = new LinkedList<>(), cq = new LinkedList<>();
                rq.add(i);
                cq.add(j);

                while(!rq.isEmpty()){
                    int r = rq.poll(), c = cq.poll();

                    for (int[] dir : DIRS) {
                        int nr = r + dir[0], nc = c + dir[1];

                        if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

                        if(visit1[nr][nc]) continue;
                        if(arr[i][j] != arr[nr][nc]) continue;

                        visit1[nr][nc] = true;

                        rq.add(nr);
                        cq.add(nc);
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(visit2[i][j]) continue;
                visit2[i][j] = true;

                ans2++;

                Queue<Integer> rq = new LinkedList<>(), cq = new LinkedList<>();
                rq.add(i);
                cq.add(j);

                while(!rq.isEmpty()){
                    int r = rq.poll(), c = cq.poll();

                    for (int[] dir : DIRS) {
                        int nr = r + dir[0], nc = c + dir[1];

                        if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

                        if(visit2[nr][nc]) continue;
                        if(arr[i][j] == 'B' && arr[i][j] != arr[nr][nc]) continue;
                        else if((arr[i][j] == 'R' || arr[i][j] == 'G') && arr[nr][nc] == 'B') continue;

                        visit2[nr][nc] = true;

                        rq.add(nr);
                        cq.add(nc);
                    }
                }
            }
        }

        System.out.println(ans1 + " " + ans2);
    }
}
