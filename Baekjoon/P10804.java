import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class P10804 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int[] cards = new int[21];
        Arrays.setAll(cards, i -> i);

        for(int i=0; i<10; i++){
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

            int a = Integer.parseInt(tokenizer.nextToken()), b = Integer.parseInt(tokenizer.nextToken());

            for(int j = 0; j <= Math.ceil((b - a) / 2); j++){
                int A = cards[a + j], B = cards[b - j];

                cards[a + j] = B;
                cards[b - j] = A;
            }
        }

        reader.close();

        System.out.println(Arrays.stream(Arrays.copyOfRange(cards, 1, 21)).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
    }
}
