import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P13549 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), K = sc.nextInt();

        sc.close();

        int answer = -1;

        int[] visit = new int[200001];
        Arrays.fill(visit, 200000);
        visit[N] = 0;

        Queue<Integer> Q = new LinkedList<>();
        Q.add(N);

        while(!Q.isEmpty()){
            int x = Q.poll();

            if(x == K) {
                answer = visit[x];
                break;
            }

            int nx = x + 1;
            if(nx <= 100000 && visit[nx] > visit[x]){
                visit[nx] = visit[x] + 1;
                Q.add(nx);
            }

            nx = x - 1;
            if(nx >= 0 && visit[nx] > visit[x]){
                visit[nx] = visit[x] + 1;
                Q.add(nx);
            }

            nx = 2 * x;
            if(nx <= 200000 && visit[nx] > visit[x]){
                visit[nx] = visit[x];
                Q.add(nx);
            }
        }

        System.out.println(answer);
    }
}
