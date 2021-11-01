import java.io.IOException;
import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Arrays;

public class P5014 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int F = sc.nextInt(), S = sc.nextInt(), G = sc.nextInt(), U = sc.nextInt(), D = sc.nextInt();

        sc.close();

        if(S == G){
            System.out.println(0);
            return;
        }

        int answer = 0;

        int[] visit = new int[F+1];
        Arrays.fill(visit, -1);
        visit[S] = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(S);
        while(!queue.isEmpty()){
            int floor = queue.poll(), next_move = visit[floor] + 1;
            int[] next_floors = {floor + U, floor - D};

            for(int next_floor: next_floors){
                if(next_floor < 1 || next_floor > F) continue;
                if(visit[next_floor] != -1) continue;
                if(next_floor == G){
                    answer = next_move;
                    break;
                }
                else if(next_floor <= F){
                    visit[next_floor] = next_move;
                    queue.add(next_floor);
                }
            }
        }

        if(answer != 0){
            System.out.println(answer);
        } else{
            System.out.println("use the stairs");
        }
    }
}
