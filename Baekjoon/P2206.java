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

        Queue<Integer> rq = new LinkedList<>(), cq = new LinkedList<>(), destq = new LinkedList<>();
        rq.add(0);
        cq.add(0);
        destq.add(1);

        int[][] visit = new int[N][M], visit_used = new int[N][M];
        visit[0][0] = 1;

        while(!rq.isEmpty()){
            int r = rq.poll(), c = cq.poll(), d = destq.poll();

            for (int[] dir : DIRS) {
                int nr = r + dir[0], nc = c + dir[1], nd = d;

                if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

                if(arr[nr][nc] == '1'){
                    if(nd == 0) continue;
                    nd = 0;

                    if(visit_used[nr][nc] > 0) continue;
                    visit_used[nr][nc] = visit[r][c] + 1;
                } else{
                    if(nd == 1) {
                        if(visit[nr][nc] > 0) continue;
                        visit[nr][nc] = visit[r][c] + 1;
                    }
                    else {
                        if(visit_used[nr][nc] > 0) continue;
                        visit_used[nr][nc] = visit_used[r][c] + 1;
                    }
                }

                if(nr == N-1 && nc == M-1){
                    break;
                }

                rq.add(nr);
                cq.add(nc);
                destq.add(nd);
            }
        }

        int answer = visit[N-1][M-1];
        if(answer == 0) answer = visit_used[N-1][M-1];
        if(answer == 0) answer = -1;

        System.out.println(answer);
    }
}
