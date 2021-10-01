import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P7569 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int[][] DIRS = {{1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1}};

        int M = sc.nextInt(), N = sc.nextInt(), H = sc.nextInt();

        int[][][] map = new int[H][N][M], visit = new int[H][N][M];
        Queue<Integer> hq = new LinkedList<Integer>(), mq = new LinkedList<Integer>(), nq = new LinkedList<Integer>();
        int answer = 0, total = 0, ripe = 0, count = 0;

        for(int h=0; h<H; h++){
            for(int n=0; n<N; n++){
                Arrays.fill(visit[h][n], -1);
                for (int m = 0; m < M; m++) {
                    map[h][n][m] = sc.nextInt();
                    if(map[h][n][m] != -1) total++;
                    if(map[h][n][m] == 1) {
                        ripe++;

                        visit[h][n][m] = 0;
                        hq.add(h);
                        nq.add(n);
                        mq.add(m);
                    }
                }
            }
        }

        if(total == ripe) {
            System.out.println(0);
            return;
        }

        sc.close();


        while(!hq.isEmpty()){
            int h = hq.poll(), n = nq.poll(), m = mq.poll();

            for(int[] DIR : DIRS){
                int nh = h + DIR[0], nn = n + DIR[1], nm = m + DIR[2];

                if(nh < 0 || nh >= H || nn < 0 || nn >= N || nm < 0 || nm >= M) continue;
                if(visit[nh][nn][nm] != -1) continue;
                if(map[nh][nn][nm] != 0) continue;

                count++;
                visit[nh][nn][nm] = visit[h][n][m] + 1;
                if(answer < visit[nh][nn][nm]){
                    answer = visit[nh][nn][nm];
                }

                hq.add(nh);
                nq.add(nn);
                mq.add(nm);
            }
        }

        if(total != ripe + count) answer = -1;
        System.out.println(answer);
    }
}
