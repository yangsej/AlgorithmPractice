import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2562 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int max = 0, index = 0;
        for(int i=1; i<=9; i++){
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

            int N = Integer.parseInt(tokenizer.nextToken());
            if(max < N){
                max = N;
                index = i;
            }
        }

        reader.close();

        System.out.println(max);
        System.out.println(index);
    }
}
