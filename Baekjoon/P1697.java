import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class P1697 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), K = sc.nextInt();

        int[] visit = new int[100001];
        Arrays.fill(visit, -1);
        visit[N] = 0;

        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(N);

        while(!queue.isEmpty()){
            int pos = queue.poll();

            if(pos == K){
                System.out.println(visit[K]);
                break;
            }

            if(pos+1 < 100001 && visit[pos+1] == -1){
                visit[pos+1] = visit[pos] + 1;
                queue.add(pos+1);
            }
            if(pos-1 >= 0 && visit[pos-1] == -1){
                visit[pos-1] = visit[pos] + 1;
                queue.add(pos-1);
            }
            if(pos*2 < 100001 && visit[pos*2] == -1){
                visit[pos*2] = visit[pos] + 1;
                queue.add(pos*2);
            }
        }

        sc.close();
    }
}
