import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P9498 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        int N = Integer.parseInt(tokenizer.nextToken());

        reader.close();

        String answer = "F";

        if (N >= 90){
            answer = "A";
        } else if (N >= 80){
            answer = "B";
        } else if (N >= 70){
            answer = "C";
        } else if (N >= 60){
            answer = "D";
        }

        System.out.println(answer);
    }
}
