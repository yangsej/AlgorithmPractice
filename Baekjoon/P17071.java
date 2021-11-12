import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P17071 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), K = sc.nextInt();

        sc.close();

        int[][] visit = new int[3][500001];
        for (int[] v : visit) {
            Arrays.fill(v, -1);
        }
        visit[0][N] = 0;

        for (int index = K, i = 0; index <= 500000;) {
            visit[2][index] = i++;
            index += i;
        }

        int answer = visit[2][N] % 2 == 0 ? 0 : -1;

        Queue<int[]> Q = new LinkedList<>();
        Q.add(new int[] {N, 0});

        while (!Q.isEmpty() && answer == -1){
            int[] coord = Q.poll();
            int n = coord[0], v = coord[1], nv = v + 1;

            int[] nextPoses = {n+1, n-1, n*2};
            for (int nn : nextPoses) {
                if(nn < 0 || nn > 500000) continue;
                if(visit[nv % 2][nn] != -1) continue;

                visit[nv % 2][nn] = visit[v % 2][n] + 1;

                if(visit[nv % 2][nn] <= visit[2][nn] && (visit[2][nn] - visit[nv % 2][nn]) % 2 == 0){
                    answer = visit[2][nn];
                    break;
                }

                Q.add(new int[] {nn, nv});
            }
        }

        System.out.println(answer);
    }
}
