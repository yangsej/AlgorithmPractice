import java.io.IOException;
import java.util.Scanner;

public class P1074 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(), R = sc.nextInt(), C = sc.nextInt();

        sc.close();

        int answer = 0;

        int r = 0, c = 0, size = (int) Math.pow(2, N);
        for(int i = 0; i < N; i++){
            size /= 2;

            if(R < r + size && C < c + size) continue;
            else if(R < r + size && C >= c + size) {
                c += size;
                answer += size * size;
            }
            else if(R >= r + size && C < c + size){
                r += size;
                answer += size * size * 2;
            }
            else {
                r += size;
                c += size;
                answer += size * size * 3;
            }
        }

        System.out.println(answer);
    }
}
