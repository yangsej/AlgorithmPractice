import java.io.IOException;
import java.util.*;

public class P2667 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] arr = new int[N][];
        for (int i = 0; i < N; i++) {
            String str = sc.next();

            int[] nums = Arrays.stream(str.split("")).mapToInt(Integer::parseInt).toArray();
            arr[i] = nums;
        }

        sc.close();

        ArrayList<Integer> answers = new ArrayList<>();
        int[][] DIRS = {{1, 0}, {0,1}, {-1, 0}, {0, -1}};
        boolean[][] visit = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(visit[i][j]) continue;
                visit[i][j] = true;

                if(arr[i][j] == 0) continue;

                Queue<Integer> rq = new LinkedList<>(), cq = new LinkedList<>();
                rq.add(i);
                cq.add(j);

                int count = 1;

                while(!rq.isEmpty()){
                    int r = rq.poll(), c = cq.poll();

                    for (int[] dir : DIRS) {
                        int nr = r + dir[0], nc = c + dir[1];

                        if(nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                        if(visit[nr][nc]) continue;

                        visit[nr][nc] = true;

                        if(arr[nr][nc] == 0) continue;

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
            sb.append('\n');
        }

        System.out.println(sb.toString());
    }
}
