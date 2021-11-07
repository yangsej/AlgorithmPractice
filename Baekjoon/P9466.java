import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class P9466 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            int N = sc.nextInt(), answer = N;
            int[] students = new int[N+1], visit = new int[N+1];

            for (int n = 1; n <= N; n++) {
                students[n] = sc.nextInt();

                if(students[n] == n){
                    visit[n] = n;
                    answer--;
                }
            }

            for (int n = 1; n <= N; n++) {
                if(visit[n] != 0) continue;
                visit[n] = n;

                Stack<Integer> stack = new Stack<>();
                stack.add(n);

                while(!stack.isEmpty()){
                    int student = stack.peek(), next = students[student];

                    if(visit[next] == n){
                        while(student != next){
                            student = stack.pop();
                            answer--;
                            visit[student] = next;
                        }
                        break;
                    } else if(visit[next] != 0) {
                        break;
                    } else{
                        visit[next] = n;
                        stack.add(next);
                    }
                }
            }

            System.out.println(answer);
        }

        sc.close();
    }
}
