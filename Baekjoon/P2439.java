import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2439 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        int N = Integer.parseInt(tokenizer.nextToken());

        reader.close();

        for(int n = 1; n <= N; n++){
            String line =
                    new String(new char[N - n]).replace("\0", " ") +
                    new String(new char[n]).replace("\0", "*");

            System.out.println(line);
        }
    }
}
