import java.util.*;
import java.io.*;

public class PermCombSubs {
    public static int n, m, totalCnt;
    public static int[] a;
    public static boolean[] isSelected;
    public static int[] numbers;

    public static void perm(int cnt) {
        if(cnt == m) {
            totalCnt += 1;
            System.out.println(Arrays.toString(numbers));
            return;
        }

        for(int i = 0; i < n; i++) {
            if(isSelected[i])
                continue;
            isSelected[i] = true;
            numbers[cnt] = a[i];
            perm(cnt + 1);
            isSelected[i] = false;
        }
    }

    public static void comb(int start, int cnt) {
        if (cnt == m){
            totalCnt += 1;
            System.out.println(Arrays.toString(numbers));
            return;
        }

        for(int i = start; i < n; i++) {
            numbers[cnt] = a[i];
            comb(i + 1, cnt + 1);
        }
    }

    public static void subs(int cnt) {
        if (cnt == n) {
            totalCnt += 1;
            for(int i = 0; i < n; i++) {
                System.out.print(isSelected[i]?a[i]:"X");
            }
            System.out.println();
            return;
        }
        isSelected[cnt] = true;
        subs(cnt + 1);
        isSelected[cnt] = false;
        subs(cnt + 1);
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        a = new int[n];
        isSelected = new boolean[n];
        numbers = new int[m];

        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        totalCnt = 0;
        perm(0);
        System.out.println(totalCnt);

        System.out.println();

        totalCnt = 0;
        comb(0, 0);
        System.out.println(totalCnt);

        System.out.println();

        totalCnt = 0;
        subs(0);
        System.out.println(totalCnt);
    }
}
