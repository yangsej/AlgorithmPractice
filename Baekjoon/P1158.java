import java.util.LinkedList;
import java.util.Scanner;
import java.io.IOException;
import java.util.Queue;

public class P1158 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), K = sc.nextInt();

        sc.close();

        Queue<Integer> Q = new LinkedList<Integer>();
        for(int n=1; n<=N; n++) {
            Q.add(n);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");

        while(!Q.isEmpty()){
            for(int k=1; k<K; k++){
                Q.add(Q.poll());
            }
            sb.append(Q.poll());
            sb.append(", ");
        }

        sb.delete(sb.length()-2, sb.length());
        sb.append(">");

        System.out.println(sb);
    }
}
