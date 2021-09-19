import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2490 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        char[] answers = {'E', 'A', 'B', 'C', 'D'};
        for(int j=0; j<3; j++){
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            int counts = 4;
            for(int i=0; i<4; i++){
                counts -= Integer.parseInt(tokenizer.nextToken());
            }
            System.out.println(answers[counts]);
        }

        reader.close();
    }
}
