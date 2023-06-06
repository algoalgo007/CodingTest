import java.util.*;

public class HashMapSort {
    public static HashMap<String, Integer> map = new HashMap<>();
//    public static HashSet<String> set = new HashSet<>();

    public static void main(String[] args) throws Exception {
        map.put("A", 3);
        map.put("C", 1);
        map.put("D", 2);
        map.put("B", 4);

        ArrayList<String> arr = new ArrayList<>(map.keySet());

        // 키 값으로 오름차순
        Collections.sort(arr);

        for (String str : arr) {
            System.out.println(str + " : " + map.get(str));
        }

        System.out.println();

        // 키 값으로 내림차순
        Collections.reverse(arr);

        for (String str : arr) {
            System.out.println(str + " : " + map.get(str));
        }

        System.out.println(

        );
        // value 로 오름차순
        arr.sort((o1, o2) -> map.get(o1).compareTo(map.get(o2)));
        for (String str : arr) {
            System.out.println(str + " : " + map.get(str));
        }

        System.out.println();

        // value 로 내림차순
        arr.sort((o1, o2) -> map.get(o2).compareTo(map.get(o1)));
        for (String str : arr) {
            System.out.println(str + " : " + map.get(str));
        }
    }
}
