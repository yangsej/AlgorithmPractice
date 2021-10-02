import java.io.IOException;
import java.util.*;

public class P2583 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int M = sc.nextInt(), N = sc.nextInt(), K = sc.nextInt();
        int[][] arr = new int[M][N];
        for (int i = 0; i < K; i++) {
            int x1 = sc.nextInt(), y1 = sc.nextInt(), x2 = sc.nextInt(), y2 = sc.nextInt();

            for (int j = y1; j < y2; j++) {
                for (int k = x1; k < x2; k++) {
                    arr[j][k] = 1;
                }
            }
        }

        sc.close();

        ArrayList<Integer> answers = new ArrayList<>();
        int[][] DIRS = {{1, 0}, {0,1}, {-1, 0}, {0, -1}};
        boolean[][] visit = new boolean[N][N];

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if(visit[i][j]) continue;
                visit[i][j] = true;

                if(arr[i][j] == 1) continue;

                Queue<Integer> rq = new LinkedList<>(), cq = new LinkedList<>();
                rq.add(i);
                cq.add(j);

                int count = 1;

                while(!rq.isEmpty()){
                    int r = rq.poll(), c = cq.poll();

                    for (int[] dir : DIRS) {
                        int nr = r + dir[0], nc = c + dir[1];

                        if(nr < 0 || nr >= M || nc < 0 || nc >= N) continue;
                        if(visit[nr][nc]) continue;

                        visit[nr][nc] = true;

                        if(arr[nr][nc] == 1) continue;

                        rq.add(nr);
                        cq.add(nc);

                        count ++;
                    }
                }

                answers.add(count);
            }
        }

        StringBuilder sb = new StringBuilder();

        int length = answers.size();
        sb.append(length);
        sb.append('\n');

        Integer[] sizes = answers.toArray(new Integer[length]);
        Arrays.sort(sizes);
        for (int size : sizes) {
            sb.append(size);
            sb.append(' ');
        }

        System.out.println(sb.toString());
    }
}
