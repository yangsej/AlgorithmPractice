import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2417 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        long N = Long.parseLong(reader.readLine());

        reader.close();

        long answer = (long)Math.ceil(Math.sqrt(N));

        System.out.println(answer);
    }
}
