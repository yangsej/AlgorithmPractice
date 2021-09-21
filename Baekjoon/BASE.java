import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class BASE {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        int N = Integer.parseInt(tokenizer.nextToken());

        reader.close();

        int answer = 0;

        System.out.println(answer);
    }
}
