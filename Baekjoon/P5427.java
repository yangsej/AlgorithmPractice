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

            Queue<Integer> R = new LinkedList<>(), C = new LinkedList<>();

            int rs = 0, cs = 0;
            for (int h = 0; h < H; h++) {
                building[h] = sc.next().toCharArray();
                for (int w = 0; w < W; w++) {
                    if(building[h][w] == '@'){
                        rs = h;
                        cs = w;
//                        R.add(h);
//                        C.add(w);
                        building[h][w] = '.';
                        visit[h][w] = 0;
                    } else if(building[h][w] == '*'){
                        R.add(h);
                        C.add(w);
                        fires[h][w] = 0;
                    }
                }
            }

            // 불 순서
            while(!R.isEmpty()){
                int r = R.poll(), c = C.poll();

                for (int[] dir : DIRS) {
                    int nr = r + dir[0], nc = c + dir[1];

                    if(nr < 0 || nr >= H || nc < 0 || nc >= W) continue;
                    if(fires[nr][nc] != -1) continue;
                    if(building[nr][nc] != '.') continue;

                    fires[nr][nc] = fires[r][c] + 1;
                    R.add(nr);
                    C.add(nc);
                }
            }

            // 이동 순서
            int answer = 0;

            R.add(rs);
            C.add(cs);

            while(!R.isEmpty()){
                int r = R.poll(), c = C.poll();

                for (int[] dir : DIRS) {
                    int nr = r + dir[0], nc = c + dir[1];

                    if(nr < 0 || nr >= H || nc < 0 || nc >= W){
                        answer = visit[r][c] + 1;
                        break;
                    }
                    if(visit[nr][nc] != -1) continue;
                    if(building[nr][nc] != '.') continue;
                    if(fires[nr][nc] < visit[r][c]) continue;

                    visit[nr][nc] = visit[r][c] + 1;
                    R.add(nr);
                    C.add(nc);
                }
            }

            System.out.println(answer != -1 ? answer : "IMPOSSIBLE");
        }

        sc.close();

    }
}
