import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P3197 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int R = sc.nextInt(), C = sc.nextInt(), MAX = R * C;
        char[][] A = new char[R][];
        int[][] DIRS = {{1,0}, {0, 1}, {-1, 0}, {0, -1}};
        int[][] starts = {{-1, -1}, {-1, -1}};
        int[][] visit = new int[R][C];
        Queue<int[]> Q = new LinkedList<>(), NQ = new LinkedList<>();

        for (int r = 0; r < R; r++) {
            String str = sc.next();
            A[r] = str.toCharArray();

            for (int c = 0; c < C; c++) {
                if(A[r][c] == 'L'){
                    if(starts[0][0] == -1){
                        starts[0][0] = r;
                        starts[0][1] = c;
                        visit[r][c] = 1;
                    } else{
                        starts[1][0] = r;
                        starts[1][1] = c;
                        visit[r][c] = 2;
                    }
                    A[r][c] = '.';
                } else if(A[r][c] == 'X'){
                    visit[r][c] = -1;
                }
            }
        }

        sc.close();

        int answer = 0;

        Q.add(starts[0]);
        Q.add(starts[1]);
        while(!Q.isEmpty()){
            int[] coord = Q.poll();
            int r = coord[0], c = coord[1];

            for (int[] dir : DIRS) {
                int nr = r + dir[0], nc = c + dir[1];

                if(nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

                if((visit[r][c] == 1 && visit[nr][nc] == 2) || (visit[r][c] == 2 && visit[nr][nc] == 1) ){
                    System.out.println(answer);
                    return;
                }

                if(visit[nr][nc] > 0) continue;

                if(visit[nr][nc] == -1) NQ.add(new int[] {nr, nc});
                else Q.add(new int[] {nr, nc});

                visit[nr][nc] = visit[r][c];
            }
        }

        answer++;
        for (; !NQ.isEmpty(); answer++) {
            for (int[] coord : NQ) {
                int r = coord[0], c = coord[1];

                for (int[] dir : DIRS) {
                    int nr = r + dir[0], nc = c + dir[1];

                    if(nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

                    if((visit[r][c] == 1 && visit[nr][nc] == 2) || (visit[r][c] == 2 && visit[nr][nc] == 1) ){
                        System.out.println(answer);
                        return;
                    }
                }
            }

            Q = NQ;
            NQ = new LinkedList<>();

            while(!Q.isEmpty()){
                int[] coord = Q.poll();
                int r = coord[0], c = coord[1];

                for (int[] dir : DIRS) {
                    int nr = r + dir[0], nc = c + dir[1];

                    if(nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

//                    if((visit[r][c] == 1 && visit[nr][nc] == 2) || (visit[r][c] == 2 && visit[nr][nc] == 1) ){
//                        System.out.println(answer);
//                        return;
//                    } else
                    if(visit[nr][nc] > 0) continue;

                    if(visit[nr][nc] == -1) NQ.add(new int[] {nr, nc});
                    else Q.add(new int[] {nr, nc});

                    visit[nr][nc] = visit[r][c];
                }
            }
        }
        System.out.println(answer);
    }
}
