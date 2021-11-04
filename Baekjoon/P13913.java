import java.io.IOException;
import java.util.*;

public class P13913 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), K = sc.nextInt();

        sc.close();

        int answer = -1;

        int[] visit = new int[200001];
        char[] move = new char[200001];
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
                move[nx] = '+';
                Q.add(nx);
            }

            nx = x - 1;
            if(nx >= 0 && visit[nx] > visit[x]){
                visit[nx] = visit[x] + 1;
                move[nx] = '-';
                Q.add(nx);
            }

            nx = 2 * x;
            if(nx <= 200000 && visit[nx] > visit[x]){
                visit[nx] = visit[x] + 1;
                move[nx] = '*';
                Q.add(nx);
            }
        }

        System.out.println(answer);

        Stack<Integer> stack = new Stack<>();

        int x = K;
        stack.add(x);

        while(x != N){
            if(move[x] == '+') x--;
            else if(move[x] == '-') x++;
            else if(move[x] == '*') x /= 2;

            stack.add(x);
        }

        StringBuilder builder = new StringBuilder();
        while(!stack.isEmpty()){
            builder.append(stack.pop());
            builder.append(' ');
        }

        System.out.println(builder);
    }
}
