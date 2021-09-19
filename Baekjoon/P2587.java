import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P2587 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int[] numbers = {0, 0, 0, 0, 0};
        int sum = 0;
        for(int i=0; i<5; i++){
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            int number = Integer.parseInt(tokenizer.nextToken());
            numbers[i] = number;
            sum += number;
        }

        reader.close();

        Arrays.sort(numbers);
        System.out.println(sum / 5);
        System.out.println(numbers[2]);
    }
}
