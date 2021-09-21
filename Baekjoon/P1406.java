import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;
import java.util.stream.Collectors;

public class P1406 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        char[] init = sc.next().toCharArray();

        Stack<Character> left = new Stack<Character>(), right = new Stack<Character>();
        for (char c : init) {
            left.push(c);
        }

        int M = sc.nextInt();
        for(int m=0; m<M; m++){
            String command = sc.next();

            if(command.equals("L") && !left.isEmpty()){
                right.push(left.pop());
            } else if(command.equals("D") && !right.isEmpty()){
                left.push(right.pop());
            } else if(command.equals("B") && !left.isEmpty()){
                left.pop();
            } else if(command.equals("P")){
                left.push(sc.next().charAt(0));
            }
        }

        sc.close();

        StringBuilder sb = new StringBuilder();
        for (Character c : left) {
            sb.append(c);
        }

        while(!right.isEmpty()){
            sb.append(right.pop());
        }

        System.out.println(sb);
    }
}
