import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2576 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));


        int sum = 0, min = 100;

        for(int i=0; i<7; i++){
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

            int N = Integer.parseInt(tokenizer.nextToken());

            if(N % 2 == 1){
                sum += N;
                if(N < min){
                    min = N;
                }
            }
        }

        reader.close();

        if(sum == 0){
            System.out.println(-1);
        } else{
            System.out.println(sum);
            System.out.println(min);
        }

    }
}
