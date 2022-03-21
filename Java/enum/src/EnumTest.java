public class EnumTest {
    public static void main(String[] args) {
        Week today = Week.SUNDAY;

        String name1 = today.name();
        System.out.println(today);

        int a = today.ordinal();
        System.out.println(a);

        Week today2 = Week.TUESDAY;
        int b = today.compareTo(today2);
        System.out.println(b);

        today2 = today.valueOf("MONDAY");
        System.out.println(today2);

        Week[] weeks = today.values();

        for (Week today3:weeks) {
            System.out.println(today3);
        }

    }

}

