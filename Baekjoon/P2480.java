import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2480 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        int[] counts = {0, 0, 0, 0, 0, 0, 0};

        for(int i=0; i<3; i++){
            counts[Integer.parseInt(tokenizer.nextToken())]++;
        }

        reader.close();

        int answer = 0;

        for(int i=1; i<7; i++){
            if(counts[i] == 3){
                answer = 10000 + i * 1000;
                break;
            } else if (counts[i] == 2){
                answer = 1000 + i * 100;
                break;
            } else if (counts[i] == 1){
                answer = i * 100;
            }
        }

        System.out.println(answer);
    }
}
