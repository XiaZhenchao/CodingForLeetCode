class LeetCode75_GreatestCommonDivisorOfStrings {
    public static void main(String[] args)
    {
        String word1 = "ABABAB";
        String word2 = "ABAB";
        String find_result = gcdOfStrings(word1,word2);
        System.out.println(find_result);
    }

    public static String gcdOfStrings(String str1, String str2) {
        String result = "";
        if((str1+str2).equals(str2+str1))
        {
            int common = findGCD(str1.length(),str2.length());
            for(int i = 0; i< common; i++)
            {
                result += str1.charAt(i);
            }
        }
        return result;
    }

    public static int findGCD(int a, int b){
        while(b!=0)
        {
            int temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }

}
