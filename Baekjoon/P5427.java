import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P5427 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int[][] DIRS = {{1,0}, {0,1}, {-1,0}, {0,-1}};
        int T = sc.nextInt();
        for (int t = 0; t < T; t++) {
            int W = sc.nextInt(), H = sc.nextInt();

            char[][] building = new char[H][];
            int[][] visit = new int[H][W], fires = new int[H][W];
            for (int[] ints : visit) {
                Arrays.fill(ints, -1);
            }
            for (int[] ints : fires) {
                Arrays.fill(ints, -1);
            }

            Queue<int[]> Q = new LinkedList<>();

            int[] start = {-1, -1};
            for (int h = 0; h < H; h++) {
                building[h] = sc.next().toCharArray();
                for (int w = 0; w < W; w++) {
                    if(building[h][w] == '@'){
                        start[0] = h;
                        start[1] = w;

                        building[h][w] = '.';
                        visit[h][w] = 0;
                    } else if(building[h][w] == '*'){
                        Q.add(new int[] {h, w});
                        fires[h][w] = 0;
                    }
                }
            }

            // 불 순서
            while(!Q.isEmpty()){
                int[] coord = Q.poll();
                int r = coord[0], c = coord[1];

                for (int[] dir : DIRS) {
                    int nr = r + dir[0], nc = c + dir[1];

                    if(nr < 0 || nr >= H || nc < 0 || nc >= W) continue;
                    if(fires[nr][nc] != -1) continue;
                    if(building[nr][nc] != '.') continue;

                    fires[nr][nc] = fires[r][c] + 1;
                    Q.add(new int[] {nr, nc});
                }
            }

            // 이동 순서
            int answer = -1;

            Q.add(start);

            while(!Q.isEmpty() && answer == -1){
                int[] coord = Q.poll();
                int r = coord[0], c = coord[1];

                for (int[] dir : DIRS) {
                    int nr = r + dir[0], nc = c + dir[1];

                    if(nr < 0 || nr >= H || nc < 0 || nc >= W){
                        answer = visit[r][c] + 1;
                        break;
                    }
                    if(visit[nr][nc] != -1) continue;
                    if(building[nr][nc] != '.') continue;
                    if(fires[nr][nc] != -1 && fires[nr][nc] <= visit[r][c] + 1) continue;

                    visit[nr][nc] = visit[r][c] + 1;

                    Q.add(new int[] {nr, nc});
                }
            }

            System.out.println(answer != -1 ? answer : "IMPOSSIBLE");
        }

        sc.close();

    }
}
