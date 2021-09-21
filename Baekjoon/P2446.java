import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2446 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int N = Integer.parseInt(tokenizer.nextToken());
        reader.close();


        for(int n = N-1; n >= 0; n--){
            String line = "";

            for(int c = 0; c < N - n - 1; c++){
                line += " ";
            }
            for(int c = 0; c < n; c++){
                line += "*";
            }
            line += "*";
            for(int c = 0; c < n; c++){
                line += "*";
            }
            System.out.println(line);
        }

        for(int n = 1; n < N; n++){
            String line = "";

            for(int c = 0; c < N - n - 1; c++){
                line += " ";
            }
            for(int c = 0; c < n; c++){
                line += "*";
            }
            line += "*";
            for(int c = 0; c < n; c++){
                line += "*";
            }
            System.out.println(line);
        }
    }
}
