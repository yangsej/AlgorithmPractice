import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Queue;

public class P6593 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int[][] DIRS = {{1, 0 ,0}, {0, 1, 0}, {0, 0, 1}, {-1, 0, 0}, {0, -1, 0}, {0, 0, -1}};
        int L = sc.nextInt(), R = sc.nextInt(), C = sc.nextInt();
        while(!(L == 0 && R == 0 && C == 0)){
            char[][][] building = new char[L][R][C];
            int[] start = {0, 0, 0}, end = {0, 0, 0};

            for (int l = 0; l < L; l++) {
                for (int r = 0; r < R; r++) {
                    String line = sc.next();
                    building[l][r] = line.toCharArray();

                    for (int c = 0; c < C; c++) {
                        if(building[l][r][c] == 'S') {
                            start[0] = l;
                            start[1] = r;
                            start[2] = c;
                        } else if(building[l][r][c] == 'E') {
                            end[0] = l;
                            end[1] = r;
                            end[2] = c;
                        }
                    }
                }
            }

            int answer = 0;

            int[][][] visit = new int[L][R][C];
            for (int[][] lv : visit) {
                for (int[] rv : lv) {
                    Arrays.fill(rv, -1);
                }
            }
            visit[start[0]][start[1]][start[2]] = 0;

            Queue<int[]> queue = new LinkedList<>();
            queue.add(start);

            while (!queue.isEmpty()){
                int[] coord = queue.poll();
                int l = coord[0], r = coord[1], c = coord[2];

                for (int[] dir : DIRS) {
                    int nl = l + dir[0], nr = r + dir[1], nc = c + dir[2];

                    if(nl < 0 || nl >= L || nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
                    if(visit[nl][nr][nc] != -1) continue;
                    if(building[nl][nr][nc] == '#') continue;
                    if(building[nl][nr][nc] == 'E'){
                        answer = visit[l][r][c] + 1;
                        break;
                    }

                    visit[nl][nr][nc] = visit[l][r][c] + 1;
                    queue.add(new int[] {nl, nr, nc});
                }
            }

            if(answer > 0) System.out.printf("Escaped in %d minute(s).\n", answer);
            else System.out.println("Trapped!");

            L = sc.nextInt();
            R = sc.nextInt();
            C = sc.nextInt();
        }
        sc.close();
    }
}
