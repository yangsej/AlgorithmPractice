import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Stack;

public class P9466 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            int N = sc.nextInt(), answer = N;
            int[] students = new int[N+1], visit = new int[N+1];
            HashSet<Integer> set = new HashSet<>();

            for (int n = 1; n <= N; n++) {
                students[n] = sc.nextInt();

                if(students[n] == n){
                    visit[n] = n;
                    set.add(n);
                    answer--;
                }
            }

            for (int n = 1; n <= N; n++) {
                if(set.contains(visit[n])) continue;
                visit[n] = n;

                Stack<Integer> stack = new Stack<Integer>();
                stack.add(n);

                while(!stack.isEmpty()){
                    int student = stack.peek(), next = students[student];

                    if(n == next){
                        answer -= stack.size();
                        set.add(n);
                        break;
                    }
                    if(set.contains(visit[next])) break;
                    if(visit[student] == visit[next]) break;

                    visit[next] = n;
                    stack.add(students[student]);
                }
            }

            System.out.println(answer);
        }

        sc.close();
    }
}
