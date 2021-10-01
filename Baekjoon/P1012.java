import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P1012 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        for(int t=0; t<T; t++){
            int answer = 0;
            int M = sc.nextInt(), N = sc.nextInt(), K = sc.nextInt();

            boolean[][] map = new boolean[N][M];
            int[][] visit = new int[N][M];

            for(int k=0; k<K; k++){
                int X = sc.nextInt(), Y = sc.nextInt();
                map[Y][X] = true;
            }

            Queue<Integer> rows = new LinkedList<Integer>(), cols = new LinkedList<Integer>();
            for(int n=0; n<N; n++){
                for(int m=0; m<M; m++){
                    if(visit[n][m] == 0){
                        if(!map[n][m]){
                            visit[n][m] = -1;
                            continue;
                        }

                        visit[n][m] = ++answer;

                        rows.add(n);
                        cols.add(m);

                        while(!rows.isEmpty()){
                            int r = rows.poll(), c = cols.poll();

                            for(int[] DIR : DIRS){
                                int nr = r + DIR[0], nc = c + DIR[1];

                                if(0 <= nr && nr < N && 0 <= nc && nc < M){
                                    if(visit[nr][nc] == 0){
                                        if(!map[nr][nc]){
                                            visit[nr][nc] = -1;
                                        } else{
                                            visit[nr][nc] = answer;
                                            rows.add(nr);
                                            cols.add(nc);
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            System.out.println(answer);
        }

        sc.close();
    }
}
