import java.io.IOException;
import java.util.*;

public class P2447 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        sc.close();

        char[][] answer = new char[N][N];
        for (char[] chars : answer) {
            Arrays.fill(chars, ' ');
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {0, 0, N});

        while (!queue.isEmpty()){
            int[] coord = queue.poll();
            int r = coord[0], c = coord[1], s = coord[2], ns = s / 3;

            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    if(i == 1 && j == 1) continue;

                    int nr = r + ns * i, nc = c + ns * j;

                    if(ns == 1) answer[nr][nc] = '*';
                    else queue.add(new int[] {nr, nc, ns});
                }
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
