import java.io.IOException;
import java.util.Scanner;

public class P9012 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int t=0; t<T; t++) {
            String str = sc.next();

            int count = 0;
            for (char c : str.toCharArray()) {
                if (c == '(') {
                    count++;
                } else if (c == ')') {
                    count--;
                }

                if (count < 0) {
                    break;
                }
            }

            if (count != 0) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }

        sc.close();

    }
}
