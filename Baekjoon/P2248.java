import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P2248 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        sc.close();

        int R = N, C = 2 * N - 1;

        char[][] answer = new char[R][C];
        for (char[] chars : answer) {
            Arrays.fill(chars, ' ');
        }

        int[][] coords = {{0, 0}, {1, -1}, {1, 1}, {2, -2}, {2, -1}, {2, 0}, {2, 1}, {2, 2}};

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, C / 2, R});

        while (!queue.isEmpty()){
            int[] coord = queue.poll();
            int r = coord[0], c = coord[1], s = coord[2], ns = s / 2;

            if(s == 3){
                for (int[] crd : coords) {
                    int nr = r + crd[0], nc = c + crd[1];

                    answer[nr][nc] = '*';
                }
            } else{
                queue.add(new int[] {r, c, ns});
                queue.add(new int[] {r + ns, c - s / 2, ns});
                queue.add(new int[] {r + ns, c + s / 2, ns});
            }
        }
        
        StringBuilder builder = new StringBuilder();
        for (char[] chars : answer) {
            builder.append(chars);
            builder.append('\n');
        }

        System.out.println(builder);
    }
}
