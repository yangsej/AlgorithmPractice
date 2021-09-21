import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2443 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        int N = Integer.parseInt(tokenizer.nextToken());

        reader.close();

        for(int n = N; n > 0; n--){
            String line =
                    new String(new char[N - n]).replace("\0", " ") +
                    new String(new char[2 * n - 1]).replace("\0", "*");

            System.out.println(line);
        }
    }
}
