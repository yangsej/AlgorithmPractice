import java.io.IOException;
import java.util.Scanner;

public class P10799 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        int answer = 0, count = 0;

        for(int i=0; i<str.length(); i++){
            char c = str.charAt(i);

            if (c == '(') {
                count++;
            } else if (c == ')') {
                count--;
                if(i > 0 && str.charAt(i-1) == '('){
                    answer += count;
                } else{
                    answer++;
                }
            }
        }

        sc.close();

        System.out.println(answer);
    }
}
